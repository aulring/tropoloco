from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class BorrowConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-borrowconfiguration.html
    Properties:
        - Name: AllowEarlyCheckIn
        - Name: MaxTimeToLiveInMinutes
    
    """
    
    AllowEarlyCheckIn_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-borrowconfiguration.html#cfn-licensemanager-license-borrowconfiguration-allowearlycheckin""", alias="AllowEarlyCheckIn")
    MaxTimeToLiveInMinutes_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-borrowconfiguration.html#cfn-licensemanager-license-borrowconfiguration-maxtimetoliveinminutes""", alias="MaxTimeToLiveInMinutes")
    


    @property
    def tropo_type(self) -> troposphere.licensemanager.BorrowConfiguration:
        from troposphere.licensemanager import BorrowConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConsumptionConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-consumptionconfiguration.html
    Properties:
        - Name: BorrowConfiguration
        - Name: RenewType
        - Name: ProvisionalConfiguration
    
    """
    
    BorrowConfiguration_: Optional['BorrowConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-consumptionconfiguration.html#cfn-licensemanager-license-consumptionconfiguration-borrowconfiguration""", alias="BorrowConfiguration")
    RenewType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-consumptionconfiguration.html#cfn-licensemanager-license-consumptionconfiguration-renewtype""", alias="RenewType")
    ProvisionalConfiguration_: Optional['ProvisionalConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-consumptionconfiguration.html#cfn-licensemanager-license-consumptionconfiguration-provisionalconfiguration""", alias="ProvisionalConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.licensemanager.ConsumptionConfiguration:
        from troposphere.licensemanager import ConsumptionConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Entitlement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-entitlement.html
    Properties:
        - Name: AllowCheckIn
        - Name: Overage
        - Name: Value
        - Name: MaxCount
        - Name: Unit
        - Name: Name
    
    """
    
    AllowCheckIn_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-entitlement.html#cfn-licensemanager-license-entitlement-allowcheckin""", alias="AllowCheckIn")
    Overage_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-entitlement.html#cfn-licensemanager-license-entitlement-overage""", alias="Overage")
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-entitlement.html#cfn-licensemanager-license-entitlement-value""", alias="Value")
    MaxCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-entitlement.html#cfn-licensemanager-license-entitlement-maxcount""", alias="MaxCount")
    Unit_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-entitlement.html#cfn-licensemanager-license-entitlement-unit""", alias="Unit")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-entitlement.html#cfn-licensemanager-license-entitlement-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.licensemanager.Entitlement:
        from troposphere.licensemanager import Entitlement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IssuerData(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-issuerdata.html
    Properties:
        - Name: SignKey
        - Name: Name
    
    """
    
    SignKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-issuerdata.html#cfn-licensemanager-license-issuerdata-signkey""", alias="SignKey")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-issuerdata.html#cfn-licensemanager-license-issuerdata-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.licensemanager.IssuerData:
        from troposphere.licensemanager import IssuerData as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Metadata(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-metadata.html
    Properties:
        - Name: Value
        - Name: Name
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-metadata.html#cfn-licensemanager-license-metadata-value""", alias="Value")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-metadata.html#cfn-licensemanager-license-metadata-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.licensemanager.Metadata:
        from troposphere.licensemanager import Metadata as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProvisionalConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-provisionalconfiguration.html
    Properties:
        - Name: MaxTimeToLiveInMinutes
    
    """
    
    MaxTimeToLiveInMinutes_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-provisionalconfiguration.html#cfn-licensemanager-license-provisionalconfiguration-maxtimetoliveinminutes""", alias="MaxTimeToLiveInMinutes")
    


    @property
    def tropo_type(self) -> troposphere.licensemanager.ProvisionalConfiguration:
        from troposphere.licensemanager import ProvisionalConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ValidityDateFormat(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-validitydateformat.html
    Properties:
        - Name: Begin
        - Name: End
    
    """
    
    Begin_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-validitydateformat.html#cfn-licensemanager-license-validitydateformat-begin""", alias="Begin")
    End_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-validitydateformat.html#cfn-licensemanager-license-validitydateformat-end""", alias="End")
    


    @property
    def tropo_type(self) -> troposphere.licensemanager.ValidityDateFormat:
        from troposphere.licensemanager import ValidityDateFormat as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Grant(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html
    Properties:
        - Name: Status
        - Name: Principals
        - Name: HomeRegion
        - Name: AllowedOperations
        - Name: LicenseArn
        - Name: GrantName
    Attributes:
        - Name: GrantArn
        - Name: Version
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html#cfn-licensemanager-grant-status""", alias="Status")
    Principals_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html#cfn-licensemanager-grant-principals""", alias="Principals")
    HomeRegion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html#cfn-licensemanager-grant-homeregion""", alias="HomeRegion")
    AllowedOperations_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html#cfn-licensemanager-grant-allowedoperations""", alias="AllowedOperations")
    LicenseArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html#cfn-licensemanager-grant-licensearn""", alias="LicenseArn")
    GrantName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html#cfn-licensemanager-grant-grantname""", alias="GrantName")
    

    @property
    def tropo_type(self) -> troposphere.licensemanager.Grant:
        from troposphere.licensemanager import Grant as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.licensemanager import Grant as TropoT
        return resource_to_troposphere(self, TropoT)


class License(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html
    Properties:
        - Name: ProductSKU
        - Name: Status
        - Name: ConsumptionConfiguration
        - Name: Validity
        - Name: ProductName
        - Name: Issuer
        - Name: HomeRegion
        - Name: Entitlements
        - Name: LicenseMetadata
        - Name: LicenseName
        - Name: Beneficiary
    Attributes:
        - Name: Version
        - Name: LicenseArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ProductSKU_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-productsku""", alias="ProductSKU")
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-status""", alias="Status")
    ConsumptionConfiguration_: 'ConsumptionConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-consumptionconfiguration""", alias="ConsumptionConfiguration")
    Validity_: 'ValidityDateFormat' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-validity""", alias="Validity")
    ProductName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-productname""", alias="ProductName")
    Issuer_: 'IssuerData' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-issuer""", alias="Issuer")
    HomeRegion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-homeregion""", alias="HomeRegion")
    Entitlements_: List['Entitlement'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-entitlements""", alias="Entitlements")
    LicenseMetadata_: Optional[List['Metadata']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-licensemetadata""", alias="LicenseMetadata")
    LicenseName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-licensename""", alias="LicenseName")
    Beneficiary_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-beneficiary""", alias="Beneficiary")
    

    @property
    def tropo_type(self) -> troposphere.licensemanager.License:
        from troposphere.licensemanager import License as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.licensemanager import License as TropoT
        return resource_to_troposphere(self, TropoT)

