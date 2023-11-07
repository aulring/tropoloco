from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class ExpiryEventsConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-certificatemanager-account-expiryeventsconfiguration.html
    Properties:
        - Name: DaysBeforeExpiry
    
    """
    
    DaysBeforeExpiry_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-certificatemanager-account-expiryeventsconfiguration.html#cfn-certificatemanager-account-expiryeventsconfiguration-daysbeforeexpiry""", alias="DaysBeforeExpiry")
    


    @property
    def tropo_type(self) -> troposphere.certificatemanager.ExpiryEventsConfiguration:
        from troposphere.certificatemanager import ExpiryEventsConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DomainValidationOption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-certificatemanager-certificate-domainvalidationoption.html
    Properties:
        - Name: DomainName
        - Name: HostedZoneId
        - Name: ValidationDomain
    
    """
    
    DomainName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-certificatemanager-certificate-domainvalidationoption.html#cfn-certificatemanager-certificate-domainvalidationoptions-domainname""", alias="DomainName")
    HostedZoneId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-certificatemanager-certificate-domainvalidationoption.html#cfn-certificatemanager-certificate-domainvalidationoption-hostedzoneid""", alias="HostedZoneId")
    ValidationDomain_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-certificatemanager-certificate-domainvalidationoption.html#cfn-certificatemanager-certificate-domainvalidationoption-validationdomain""", alias="ValidationDomain")
    


    @property
    def tropo_type(self) -> troposphere.certificatemanager.DomainValidationOption:
        from troposphere.certificatemanager import DomainValidationOption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Account(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-account.html
    Properties:
        - Name: ExpiryEventsConfiguration
    Attributes:
        - Name: AccountId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ExpiryEventsConfiguration_: 'ExpiryEventsConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-account.html#cfn-certificatemanager-account-expiryeventsconfiguration""", alias="ExpiryEventsConfiguration")
    

    @property
    def tropo_type(self) -> troposphere.certificatemanager.Account:
        from troposphere.certificatemanager import Account as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.certificatemanager import Account as TropoT
        return resource_to_troposphere(self, TropoT)


class Certificate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html
    Properties:
        - Name: CertificateAuthorityArn
        - Name: CertificateTransparencyLoggingPreference
        - Name: DomainName
        - Name: DomainValidationOptions
        - Name: KeyAlgorithm
        - Name: SubjectAlternativeNames
        - Name: Tags
        - Name: ValidationMethod
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CertificateAuthorityArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-certificateauthorityarn""", alias="CertificateAuthorityArn")
    CertificateTransparencyLoggingPreference_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-certificatetransparencyloggingpreference""", alias="CertificateTransparencyLoggingPreference")
    DomainName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-domainname""", alias="DomainName")
    DomainValidationOptions_: Optional[List['DomainValidationOption']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-domainvalidationoptions""", alias="DomainValidationOptions")
    KeyAlgorithm_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-keyalgorithm""", alias="KeyAlgorithm")
    SubjectAlternativeNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-subjectalternativenames""", alias="SubjectAlternativeNames")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-tags""", alias="Tags")
    ValidationMethod_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-validationmethod""", alias="ValidationMethod")
    

    @property
    def tropo_type(self) -> troposphere.certificatemanager.Certificate:
        from troposphere.certificatemanager import Certificate as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.certificatemanager import Certificate as TropoT
        return resource_to_troposphere(self, TropoT)

