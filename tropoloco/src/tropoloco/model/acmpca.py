from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class ApiPassthrough(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-apipassthrough.html
    Properties:
        - Name: Extensions
        - Name: Subject
    
    """
    
    Extensions_: Optional['Extensions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-apipassthrough.html#cfn-acmpca-certificate-apipassthrough-extensions""", alias="Extensions")
    Subject_: Optional['Subject'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-apipassthrough.html#cfn-acmpca-certificate-apipassthrough-subject""", alias="Subject")
    


    @property
    def tropo_type(self) -> troposphere.acmpca.ApiPassthrough:
        from troposphere.acmpca import ApiPassthrough as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomAttribute(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-customattribute.html
    Properties:
        - Name: Value
        - Name: ObjectIdentifier
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-customattribute.html#cfn-acmpca-certificate-customattribute-value""", alias="Value")
    ObjectIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-customattribute.html#cfn-acmpca-certificate-customattribute-objectidentifier""", alias="ObjectIdentifier")
    


    @property
    def tropo_type(self) -> troposphere.acmpca.CustomAttribute:
        from troposphere.acmpca import CustomAttribute as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomExtension(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-customextension.html
    Properties:
        - Name: Value
        - Name: Critical
        - Name: ObjectIdentifier
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-customextension.html#cfn-acmpca-certificate-customextension-value""", alias="Value")
    Critical_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-customextension.html#cfn-acmpca-certificate-customextension-critical""", alias="Critical")
    ObjectIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-customextension.html#cfn-acmpca-certificate-customextension-objectidentifier""", alias="ObjectIdentifier")
    


    @property
    def tropo_type(self) -> troposphere.acmpca.CustomExtension:
        from troposphere.acmpca import CustomExtension as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EdiPartyName(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-edipartyname.html
    Properties:
        - Name: PartyName
        - Name: NameAssigner
    
    """
    
    PartyName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-edipartyname.html#cfn-acmpca-certificate-edipartyname-partyname""", alias="PartyName")
    NameAssigner_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-edipartyname.html#cfn-acmpca-certificate-edipartyname-nameassigner""", alias="NameAssigner")
    


    @property
    def tropo_type(self) -> troposphere.acmpca.EdiPartyName:
        from troposphere.acmpca import EdiPartyName as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ExtendedKeyUsage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-extendedkeyusage.html
    Properties:
        - Name: ExtendedKeyUsageType
        - Name: ExtendedKeyUsageObjectIdentifier
    
    """
    
    ExtendedKeyUsageType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-extendedkeyusage.html#cfn-acmpca-certificate-extendedkeyusage-extendedkeyusagetype""", alias="ExtendedKeyUsageType")
    ExtendedKeyUsageObjectIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-extendedkeyusage.html#cfn-acmpca-certificate-extendedkeyusage-extendedkeyusageobjectidentifier""", alias="ExtendedKeyUsageObjectIdentifier")
    


    @property
    def tropo_type(self) -> troposphere.acmpca.ExtendedKeyUsage:
        from troposphere.acmpca import ExtendedKeyUsage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Extensions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-extensions.html
    Properties:
        - Name: CustomExtensions
        - Name: CertificatePolicies
        - Name: KeyUsage
        - Name: SubjectAlternativeNames
        - Name: ExtendedKeyUsage
    
    """
    
    CustomExtensions_: Optional[List['CustomExtension']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-extensions.html#cfn-acmpca-certificate-extensions-customextensions""", alias="CustomExtensions")
    CertificatePolicies_: Optional[List['PolicyInformation']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-extensions.html#cfn-acmpca-certificate-extensions-certificatepolicies""", alias="CertificatePolicies")
    KeyUsage_: Optional['KeyUsage'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-extensions.html#cfn-acmpca-certificate-extensions-keyusage""", alias="KeyUsage")
    SubjectAlternativeNames_: Optional[List['GeneralName']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-extensions.html#cfn-acmpca-certificate-extensions-subjectalternativenames""", alias="SubjectAlternativeNames")
    ExtendedKeyUsage_: Optional[List['ExtendedKeyUsage']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-extensions.html#cfn-acmpca-certificate-extensions-extendedkeyusage""", alias="ExtendedKeyUsage")
    


    @property
    def tropo_type(self) -> troposphere.acmpca.Extensions:
        from troposphere.acmpca import Extensions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GeneralName(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-generalname.html
    Properties:
        - Name: UniformResourceIdentifier
        - Name: DnsName
        - Name: EdiPartyName
        - Name: RegisteredId
        - Name: Rfc822Name
        - Name: OtherName
        - Name: IpAddress
        - Name: DirectoryName
    
    """
    
    UniformResourceIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-generalname.html#cfn-acmpca-certificate-generalname-uniformresourceidentifier""", alias="UniformResourceIdentifier")
    DnsName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-generalname.html#cfn-acmpca-certificate-generalname-dnsname""", alias="DnsName")
    EdiPartyName_: Optional['EdiPartyName'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-generalname.html#cfn-acmpca-certificate-generalname-edipartyname""", alias="EdiPartyName")
    RegisteredId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-generalname.html#cfn-acmpca-certificate-generalname-registeredid""", alias="RegisteredId")
    Rfc822Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-generalname.html#cfn-acmpca-certificate-generalname-rfc822name""", alias="Rfc822Name")
    OtherName_: Optional['OtherName'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-generalname.html#cfn-acmpca-certificate-generalname-othername""", alias="OtherName")
    IpAddress_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-generalname.html#cfn-acmpca-certificate-generalname-ipaddress""", alias="IpAddress")
    DirectoryName_: Optional['Subject'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-generalname.html#cfn-acmpca-certificate-generalname-directoryname""", alias="DirectoryName")
    


    @property
    def tropo_type(self) -> troposphere.acmpca.GeneralName:
        from troposphere.acmpca import GeneralName as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KeyUsage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-keyusage.html
    Properties:
        - Name: KeyEncipherment
        - Name: DataEncipherment
        - Name: DigitalSignature
        - Name: KeyCertSign
        - Name: DecipherOnly
        - Name: KeyAgreement
        - Name: NonRepudiation
        - Name: CRLSign
        - Name: EncipherOnly
    
    """
    
    KeyEncipherment_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-keyusage.html#cfn-acmpca-certificate-keyusage-keyencipherment""", alias="KeyEncipherment")
    DataEncipherment_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-keyusage.html#cfn-acmpca-certificate-keyusage-dataencipherment""", alias="DataEncipherment")
    DigitalSignature_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-keyusage.html#cfn-acmpca-certificate-keyusage-digitalsignature""", alias="DigitalSignature")
    KeyCertSign_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-keyusage.html#cfn-acmpca-certificate-keyusage-keycertsign""", alias="KeyCertSign")
    DecipherOnly_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-keyusage.html#cfn-acmpca-certificate-keyusage-decipheronly""", alias="DecipherOnly")
    KeyAgreement_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-keyusage.html#cfn-acmpca-certificate-keyusage-keyagreement""", alias="KeyAgreement")
    NonRepudiation_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-keyusage.html#cfn-acmpca-certificate-keyusage-nonrepudiation""", alias="NonRepudiation")
    CRLSign_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-keyusage.html#cfn-acmpca-certificate-keyusage-crlsign""", alias="CRLSign")
    EncipherOnly_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-keyusage.html#cfn-acmpca-certificate-keyusage-encipheronly""", alias="EncipherOnly")
    


    @property
    def tropo_type(self) -> troposphere.acmpca.KeyUsage:
        from troposphere.acmpca import KeyUsage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OtherName(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-othername.html
    Properties:
        - Name: TypeId
        - Name: Value
    
    """
    
    TypeId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-othername.html#cfn-acmpca-certificate-othername-typeid""", alias="TypeId")
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-othername.html#cfn-acmpca-certificate-othername-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.acmpca.OtherName:
        from troposphere.acmpca import OtherName as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PolicyInformation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-policyinformation.html
    Properties:
        - Name: CertPolicyId
        - Name: PolicyQualifiers
    
    """
    
    CertPolicyId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-policyinformation.html#cfn-acmpca-certificate-policyinformation-certpolicyid""", alias="CertPolicyId")
    PolicyQualifiers_: Optional[List['PolicyQualifierInfo']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-policyinformation.html#cfn-acmpca-certificate-policyinformation-policyqualifiers""", alias="PolicyQualifiers")
    


    @property
    def tropo_type(self) -> troposphere.acmpca.PolicyInformation:
        from troposphere.acmpca import PolicyInformation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PolicyQualifierInfo(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-policyqualifierinfo.html
    Properties:
        - Name: Qualifier
        - Name: PolicyQualifierId
    
    """
    
    Qualifier_: 'Qualifier' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-policyqualifierinfo.html#cfn-acmpca-certificate-policyqualifierinfo-qualifier""", alias="Qualifier")
    PolicyQualifierId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-policyqualifierinfo.html#cfn-acmpca-certificate-policyqualifierinfo-policyqualifierid""", alias="PolicyQualifierId")
    


    @property
    def tropo_type(self) -> troposphere.acmpca.PolicyQualifierInfo:
        from troposphere.acmpca import PolicyQualifierInfo as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Qualifier(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-qualifier.html
    Properties:
        - Name: CpsUri
    
    """
    
    CpsUri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-qualifier.html#cfn-acmpca-certificate-qualifier-cpsuri""", alias="CpsUri")
    


    @property
    def tropo_type(self) -> troposphere.acmpca.Qualifier:
        from troposphere.acmpca import Qualifier as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Subject(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html
    Properties:
        - Name: Organization
        - Name: OrganizationalUnit
        - Name: Locality
        - Name: Title
        - Name: GivenName
        - Name: GenerationQualifier
        - Name: Initials
        - Name: CustomAttributes
        - Name: SerialNumber
        - Name: State
        - Name: Country
        - Name: Surname
        - Name: DistinguishedNameQualifier
        - Name: CommonName
        - Name: Pseudonym
    
    """
    
    Organization_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-organization""", alias="Organization")
    OrganizationalUnit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-organizationalunit""", alias="OrganizationalUnit")
    Locality_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-locality""", alias="Locality")
    Title_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-title""", alias="Title")
    GivenName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-givenname""", alias="GivenName")
    GenerationQualifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-generationqualifier""", alias="GenerationQualifier")
    Initials_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-initials""", alias="Initials")
    CustomAttributes_: Optional[List['CustomAttribute']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-customattributes""", alias="CustomAttributes")
    SerialNumber_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-serialnumber""", alias="SerialNumber")
    State_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-state""", alias="State")
    Country_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-country""", alias="Country")
    Surname_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-surname""", alias="Surname")
    DistinguishedNameQualifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-distinguishednamequalifier""", alias="DistinguishedNameQualifier")
    CommonName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-commonname""", alias="CommonName")
    Pseudonym_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-pseudonym""", alias="Pseudonym")
    


    @property
    def tropo_type(self) -> troposphere.acmpca.Subject:
        from troposphere.acmpca import Subject as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Validity(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-validity.html
    Properties:
        - Name: Type
        - Name: Value
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-validity.html#cfn-acmpca-certificate-validity-type""", alias="Type")
    Value_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-validity.html#cfn-acmpca-certificate-validity-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.acmpca.Validity:
        from troposphere.acmpca import Validity as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AccessDescription(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-accessdescription.html
    Properties:
        - Name: AccessMethod
        - Name: AccessLocation
    
    """
    
    AccessMethod_: 'AccessMethod' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-accessdescription.html#cfn-acmpca-certificateauthority-accessdescription-accessmethod""", alias="AccessMethod")
    AccessLocation_: 'GeneralName' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-accessdescription.html#cfn-acmpca-certificateauthority-accessdescription-accesslocation""", alias="AccessLocation")
    


    @property
    def tropo_type(self) -> troposphere.acmpca.AccessDescription:
        from troposphere.acmpca import AccessDescription as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AccessMethod(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-accessmethod.html
    Properties:
        - Name: CustomObjectIdentifier
        - Name: AccessMethodType
    
    """
    
    CustomObjectIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-accessmethod.html#cfn-acmpca-certificateauthority-accessmethod-customobjectidentifier""", alias="CustomObjectIdentifier")
    AccessMethodType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-accessmethod.html#cfn-acmpca-certificateauthority-accessmethod-accessmethodtype""", alias="AccessMethodType")
    


    @property
    def tropo_type(self) -> troposphere.acmpca.AccessMethod:
        from troposphere.acmpca import AccessMethod as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CrlConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-crlconfiguration.html
    Properties:
        - Name: CustomCname
        - Name: S3ObjectAcl
        - Name: ExpirationInDays
        - Name: Enabled
        - Name: S3BucketName
    
    """
    
    CustomCname_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-crlconfiguration.html#cfn-acmpca-certificateauthority-crlconfiguration-customcname""", alias="CustomCname")
    S3ObjectAcl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-crlconfiguration.html#cfn-acmpca-certificateauthority-crlconfiguration-s3objectacl""", alias="S3ObjectAcl")
    ExpirationInDays_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-crlconfiguration.html#cfn-acmpca-certificateauthority-crlconfiguration-expirationindays""", alias="ExpirationInDays")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-crlconfiguration.html#cfn-acmpca-certificateauthority-crlconfiguration-enabled""", alias="Enabled")
    S3BucketName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-crlconfiguration.html#cfn-acmpca-certificateauthority-crlconfiguration-s3bucketname""", alias="S3BucketName")
    


    @property
    def tropo_type(self) -> troposphere.acmpca.CrlConfiguration:
        from troposphere.acmpca import CrlConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CsrExtensions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-csrextensions.html
    Properties:
        - Name: KeyUsage
        - Name: SubjectInformationAccess
    
    """
    
    KeyUsage_: Optional['KeyUsage'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-csrextensions.html#cfn-acmpca-certificateauthority-csrextensions-keyusage""", alias="KeyUsage")
    SubjectInformationAccess_: Optional[List['AccessDescription']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-csrextensions.html#cfn-acmpca-certificateauthority-csrextensions-subjectinformationaccess""", alias="SubjectInformationAccess")
    


    @property
    def tropo_type(self) -> troposphere.acmpca.CsrExtensions:
        from troposphere.acmpca import CsrExtensions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomAttribute(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-customattribute.html
    Properties:
        - Name: Value
        - Name: ObjectIdentifier
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-customattribute.html#cfn-acmpca-certificateauthority-customattribute-value""", alias="Value")
    ObjectIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-customattribute.html#cfn-acmpca-certificateauthority-customattribute-objectidentifier""", alias="ObjectIdentifier")
    


    @property
    def tropo_type(self) -> troposphere.acmpca.CustomAttribute:
        from troposphere.acmpca import CustomAttribute as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EdiPartyName(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-edipartyname.html
    Properties:
        - Name: PartyName
        - Name: NameAssigner
    
    """
    
    PartyName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-edipartyname.html#cfn-acmpca-certificateauthority-edipartyname-partyname""", alias="PartyName")
    NameAssigner_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-edipartyname.html#cfn-acmpca-certificateauthority-edipartyname-nameassigner""", alias="NameAssigner")
    


    @property
    def tropo_type(self) -> troposphere.acmpca.EdiPartyName:
        from troposphere.acmpca import EdiPartyName as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GeneralName(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-generalname.html
    Properties:
        - Name: UniformResourceIdentifier
        - Name: DnsName
        - Name: EdiPartyName
        - Name: RegisteredId
        - Name: Rfc822Name
        - Name: OtherName
        - Name: IpAddress
        - Name: DirectoryName
    
    """
    
    UniformResourceIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-generalname.html#cfn-acmpca-certificateauthority-generalname-uniformresourceidentifier""", alias="UniformResourceIdentifier")
    DnsName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-generalname.html#cfn-acmpca-certificateauthority-generalname-dnsname""", alias="DnsName")
    EdiPartyName_: Optional['EdiPartyName'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-generalname.html#cfn-acmpca-certificateauthority-generalname-edipartyname""", alias="EdiPartyName")
    RegisteredId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-generalname.html#cfn-acmpca-certificateauthority-generalname-registeredid""", alias="RegisteredId")
    Rfc822Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-generalname.html#cfn-acmpca-certificateauthority-generalname-rfc822name""", alias="Rfc822Name")
    OtherName_: Optional['OtherName'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-generalname.html#cfn-acmpca-certificateauthority-generalname-othername""", alias="OtherName")
    IpAddress_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-generalname.html#cfn-acmpca-certificateauthority-generalname-ipaddress""", alias="IpAddress")
    DirectoryName_: Optional['Subject'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-generalname.html#cfn-acmpca-certificateauthority-generalname-directoryname""", alias="DirectoryName")
    


    @property
    def tropo_type(self) -> troposphere.acmpca.GeneralName:
        from troposphere.acmpca import GeneralName as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KeyUsage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-keyusage.html
    Properties:
        - Name: KeyEncipherment
        - Name: DataEncipherment
        - Name: DigitalSignature
        - Name: KeyCertSign
        - Name: DecipherOnly
        - Name: KeyAgreement
        - Name: NonRepudiation
        - Name: CRLSign
        - Name: EncipherOnly
    
    """
    
    KeyEncipherment_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-keyusage.html#cfn-acmpca-certificateauthority-keyusage-keyencipherment""", alias="KeyEncipherment")
    DataEncipherment_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-keyusage.html#cfn-acmpca-certificateauthority-keyusage-dataencipherment""", alias="DataEncipherment")
    DigitalSignature_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-keyusage.html#cfn-acmpca-certificateauthority-keyusage-digitalsignature""", alias="DigitalSignature")
    KeyCertSign_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-keyusage.html#cfn-acmpca-certificateauthority-keyusage-keycertsign""", alias="KeyCertSign")
    DecipherOnly_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-keyusage.html#cfn-acmpca-certificateauthority-keyusage-decipheronly""", alias="DecipherOnly")
    KeyAgreement_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-keyusage.html#cfn-acmpca-certificateauthority-keyusage-keyagreement""", alias="KeyAgreement")
    NonRepudiation_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-keyusage.html#cfn-acmpca-certificateauthority-keyusage-nonrepudiation""", alias="NonRepudiation")
    CRLSign_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-keyusage.html#cfn-acmpca-certificateauthority-keyusage-crlsign""", alias="CRLSign")
    EncipherOnly_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-keyusage.html#cfn-acmpca-certificateauthority-keyusage-encipheronly""", alias="EncipherOnly")
    


    @property
    def tropo_type(self) -> troposphere.acmpca.KeyUsage:
        from troposphere.acmpca import KeyUsage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OcspConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-ocspconfiguration.html
    Properties:
        - Name: OcspCustomCname
        - Name: Enabled
    
    """
    
    OcspCustomCname_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-ocspconfiguration.html#cfn-acmpca-certificateauthority-ocspconfiguration-ocspcustomcname""", alias="OcspCustomCname")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-ocspconfiguration.html#cfn-acmpca-certificateauthority-ocspconfiguration-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.acmpca.OcspConfiguration:
        from troposphere.acmpca import OcspConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OtherName(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-othername.html
    Properties:
        - Name: TypeId
        - Name: Value
    
    """
    
    TypeId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-othername.html#cfn-acmpca-certificateauthority-othername-typeid""", alias="TypeId")
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-othername.html#cfn-acmpca-certificateauthority-othername-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.acmpca.OtherName:
        from troposphere.acmpca import OtherName as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RevocationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-revocationconfiguration.html
    Properties:
        - Name: OcspConfiguration
        - Name: CrlConfiguration
    
    """
    
    OcspConfiguration_: Optional['OcspConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-revocationconfiguration.html#cfn-acmpca-certificateauthority-revocationconfiguration-ocspconfiguration""", alias="OcspConfiguration")
    CrlConfiguration_: Optional['CrlConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-revocationconfiguration.html#cfn-acmpca-certificateauthority-revocationconfiguration-crlconfiguration""", alias="CrlConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.acmpca.RevocationConfiguration:
        from troposphere.acmpca import RevocationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Subject(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html
    Properties:
        - Name: Organization
        - Name: OrganizationalUnit
        - Name: Locality
        - Name: Title
        - Name: GivenName
        - Name: GenerationQualifier
        - Name: Initials
        - Name: CustomAttributes
        - Name: SerialNumber
        - Name: State
        - Name: Country
        - Name: Surname
        - Name: DistinguishedNameQualifier
        - Name: CommonName
        - Name: Pseudonym
    
    """
    
    Organization_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-organization""", alias="Organization")
    OrganizationalUnit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-organizationalunit""", alias="OrganizationalUnit")
    Locality_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-locality""", alias="Locality")
    Title_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-title""", alias="Title")
    GivenName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-givenname""", alias="GivenName")
    GenerationQualifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-generationqualifier""", alias="GenerationQualifier")
    Initials_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-initials""", alias="Initials")
    CustomAttributes_: Optional[List['CustomAttribute']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-customattributes""", alias="CustomAttributes")
    SerialNumber_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-serialnumber""", alias="SerialNumber")
    State_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-state""", alias="State")
    Country_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-country""", alias="Country")
    Surname_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-surname""", alias="Surname")
    DistinguishedNameQualifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-distinguishednamequalifier""", alias="DistinguishedNameQualifier")
    CommonName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-commonname""", alias="CommonName")
    Pseudonym_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-pseudonym""", alias="Pseudonym")
    


    @property
    def tropo_type(self) -> troposphere.acmpca.Subject:
        from troposphere.acmpca import Subject as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Certificate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html
    Properties:
        - Name: TemplateArn
        - Name: CertificateAuthorityArn
        - Name: Validity
        - Name: CertificateSigningRequest
        - Name: SigningAlgorithm
        - Name: ApiPassthrough
        - Name: ValidityNotBefore
    Attributes:
        - Name: Arn
        - Name: Certificate
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TemplateArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html#cfn-acmpca-certificate-templatearn""", alias="TemplateArn")
    CertificateAuthorityArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html#cfn-acmpca-certificate-certificateauthorityarn""", alias="CertificateAuthorityArn")
    Validity_: 'Validity' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html#cfn-acmpca-certificate-validity""", alias="Validity")
    CertificateSigningRequest_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html#cfn-acmpca-certificate-certificatesigningrequest""", alias="CertificateSigningRequest")
    SigningAlgorithm_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html#cfn-acmpca-certificate-signingalgorithm""", alias="SigningAlgorithm")
    ApiPassthrough_: Optional['ApiPassthrough'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html#cfn-acmpca-certificate-apipassthrough""", alias="ApiPassthrough")
    ValidityNotBefore_: Optional['Validity'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html#cfn-acmpca-certificate-validitynotbefore""", alias="ValidityNotBefore")
    

    @property
    def tropo_type(self) -> troposphere.acmpca.Certificate:
        from troposphere.acmpca import Certificate as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.acmpca import Certificate as TropoT
        return resource_to_troposphere(self, TropoT)


class CertificateAuthority(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html
    Properties:
        - Name: CsrExtensions
        - Name: Type
        - Name: RevocationConfiguration
        - Name: UsageMode
        - Name: SigningAlgorithm
        - Name: KeyStorageSecurityStandard
        - Name: Subject
        - Name: Tags
        - Name: KeyAlgorithm
    Attributes:
        - Name: CertificateSigningRequest
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CsrExtensions_: Optional['CsrExtensions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-csrextensions""", alias="CsrExtensions")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-type""", alias="Type")
    RevocationConfiguration_: Optional['RevocationConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-revocationconfiguration""", alias="RevocationConfiguration")
    UsageMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-usagemode""", alias="UsageMode")
    SigningAlgorithm_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-signingalgorithm""", alias="SigningAlgorithm")
    KeyStorageSecurityStandard_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-keystoragesecuritystandard""", alias="KeyStorageSecurityStandard")
    Subject_: 'Subject' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-subject""", alias="Subject")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-tags""", alias="Tags")
    KeyAlgorithm_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-keyalgorithm""", alias="KeyAlgorithm")
    

    @property
    def tropo_type(self) -> troposphere.acmpca.CertificateAuthority:
        from troposphere.acmpca import CertificateAuthority as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.acmpca import CertificateAuthority as TropoT
        return resource_to_troposphere(self, TropoT)


class CertificateAuthorityActivation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthorityactivation.html
    Properties:
        - Name: Status
        - Name: CertificateAuthorityArn
        - Name: CertificateChain
        - Name: Certificate
    Attributes:
        - Name: CompleteCertificateChain
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthorityactivation.html#cfn-acmpca-certificateauthorityactivation-status""", alias="Status")
    CertificateAuthorityArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthorityactivation.html#cfn-acmpca-certificateauthorityactivation-certificateauthorityarn""", alias="CertificateAuthorityArn")
    CertificateChain_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthorityactivation.html#cfn-acmpca-certificateauthorityactivation-certificatechain""", alias="CertificateChain")
    Certificate_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthorityactivation.html#cfn-acmpca-certificateauthorityactivation-certificate""", alias="Certificate")
    

    @property
    def tropo_type(self) -> troposphere.acmpca.CertificateAuthorityActivation:
        from troposphere.acmpca import CertificateAuthorityActivation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.acmpca import CertificateAuthorityActivation as TropoT
        return resource_to_troposphere(self, TropoT)


class Permission(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-permission.html
    Properties:
        - Name: CertificateAuthorityArn
        - Name: Actions
        - Name: SourceAccount
        - Name: Principal
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CertificateAuthorityArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-permission.html#cfn-acmpca-permission-certificateauthorityarn""", alias="CertificateAuthorityArn")
    Actions_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-permission.html#cfn-acmpca-permission-actions""", alias="Actions")
    SourceAccount_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-permission.html#cfn-acmpca-permission-sourceaccount""", alias="SourceAccount")
    Principal_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-permission.html#cfn-acmpca-permission-principal""", alias="Principal")
    

    @property
    def tropo_type(self) -> troposphere.acmpca.Permission:
        from troposphere.acmpca import Permission as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.acmpca import Permission as TropoT
        return resource_to_troposphere(self, TropoT)

