from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class CodeStarParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-codestarparameters.html
    Properties:
        - Name: ArtifactPath
        - Name: Repository
        - Name: Branch
        - Name: ConnectionArn
    
    """
    
    ArtifactPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-codestarparameters.html#cfn-servicecatalog-cloudformationproduct-codestarparameters-artifactpath""", alias="ArtifactPath")
    Repository_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-codestarparameters.html#cfn-servicecatalog-cloudformationproduct-codestarparameters-repository""", alias="Repository")
    Branch_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-codestarparameters.html#cfn-servicecatalog-cloudformationproduct-codestarparameters-branch""", alias="Branch")
    ConnectionArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-codestarparameters.html#cfn-servicecatalog-cloudformationproduct-codestarparameters-connectionarn""", alias="ConnectionArn")
    


    @property
    def tropo_type(self) -> troposphere.servicecatalog.CodeStarParameters:
        from troposphere.servicecatalog import CodeStarParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConnectionParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-sourceconnection-connectionparameters.html
    Properties:
        - Name: CodeStar
    
    """
    
    CodeStar_: Optional['CodeStarParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-sourceconnection-connectionparameters.html#cfn-servicecatalog-cloudformationproduct-sourceconnection-connectionparameters-codestar""", alias="CodeStar")
    


    @property
    def tropo_type(self) -> troposphere.servicecatalog.ConnectionParameters:
        from troposphere.servicecatalog import ConnectionParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProvisioningArtifactProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties.html
    Properties:
        - Name: Type
        - Name: Description
        - Name: DisableTemplateValidation
        - Name: Info
        - Name: Name
    
    """
    
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties.html#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-type""", alias="Type")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties.html#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-description""", alias="Description")
    DisableTemplateValidation_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties.html#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-disabletemplatevalidation""", alias="DisableTemplateValidation")
    Info_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties.html#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-info""", alias="Info")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties.html#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.servicecatalog.ProvisioningArtifactProperties:
        from troposphere.servicecatalog import ProvisioningArtifactProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SourceConnection(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-sourceconnection.html
    Properties:
        - Name: Type
        - Name: ConnectionParameters
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-sourceconnection.html#cfn-servicecatalog-cloudformationproduct-sourceconnection-type""", alias="Type")
    ConnectionParameters_: 'ConnectionParameters' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-sourceconnection.html#cfn-servicecatalog-cloudformationproduct-sourceconnection-connectionparameters""", alias="ConnectionParameters")
    


    @property
    def tropo_type(self) -> troposphere.servicecatalog.SourceConnection:
        from troposphere.servicecatalog import SourceConnection as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProvisioningParameter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningparameter.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningparameter.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningparameter-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningparameter.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningparameter-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.servicecatalog.ProvisioningParameter:
        from troposphere.servicecatalog import ProvisioningParameter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProvisioningPreferences(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html
    Properties:
        - Name: StackSetAccounts
        - Name: StackSetFailureToleranceCount
        - Name: StackSetMaxConcurrencyPercentage
        - Name: StackSetMaxConcurrencyCount
        - Name: StackSetRegions
        - Name: StackSetOperationType
        - Name: StackSetFailureTolerancePercentage
    
    """
    
    StackSetAccounts_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetaccounts""", alias="StackSetAccounts")
    StackSetFailureToleranceCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetfailuretolerancecount""", alias="StackSetFailureToleranceCount")
    StackSetMaxConcurrencyPercentage_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetmaxconcurrencypercentage""", alias="StackSetMaxConcurrencyPercentage")
    StackSetMaxConcurrencyCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetmaxconcurrencycount""", alias="StackSetMaxConcurrencyCount")
    StackSetRegions_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetregions""", alias="StackSetRegions")
    StackSetOperationType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetoperationtype""", alias="StackSetOperationType")
    StackSetFailureTolerancePercentage_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetfailuretolerancepercentage""", alias="StackSetFailureTolerancePercentage")
    


    @property
    def tropo_type(self) -> troposphere.servicecatalog.ProvisioningPreferences:
        from troposphere.servicecatalog import ProvisioningPreferences as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DefinitionParameter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-serviceaction-definitionparameter.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-serviceaction-definitionparameter.html#cfn-servicecatalog-serviceaction-definitionparameter-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-serviceaction-definitionparameter.html#cfn-servicecatalog-serviceaction-definitionparameter-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.servicecatalog.DefinitionParameter:
        from troposphere.servicecatalog import DefinitionParameter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class AcceptedPortfolioShare(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-acceptedportfolioshare.html
    Properties:
        - Name: AcceptLanguage
        - Name: PortfolioId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AcceptLanguage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-acceptedportfolioshare.html#cfn-servicecatalog-acceptedportfolioshare-acceptlanguage""", alias="AcceptLanguage")
    PortfolioId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-acceptedportfolioshare.html#cfn-servicecatalog-acceptedportfolioshare-portfolioid""", alias="PortfolioId")
    

    @property
    def tropo_type(self) -> troposphere.servicecatalog.AcceptedPortfolioShare:
        from troposphere.servicecatalog import AcceptedPortfolioShare as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.servicecatalog import AcceptedPortfolioShare as TropoT
        return resource_to_troposphere(self, TropoT)


class CloudFormationProduct(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html
    Properties:
        - Name: Owner
        - Name: Description
        - Name: SupportEmail
        - Name: ProductType
        - Name: Name
        - Name: ReplaceProvisioningArtifacts
        - Name: SupportDescription
        - Name: Distributor
        - Name: AcceptLanguage
        - Name: SupportUrl
        - Name: SourceConnection
        - Name: Tags
        - Name: ProvisioningArtifactParameters
    Attributes:
        - Name: ProductName
        - Name: ProvisioningArtifactIds
        - Name: ProvisioningArtifactNames
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Owner_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-owner""", alias="Owner")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-description""", alias="Description")
    SupportEmail_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-supportemail""", alias="SupportEmail")
    ProductType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-producttype""", alias="ProductType")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-name""", alias="Name")
    ReplaceProvisioningArtifacts_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-replaceprovisioningartifacts""", alias="ReplaceProvisioningArtifacts")
    SupportDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-supportdescription""", alias="SupportDescription")
    Distributor_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-distributor""", alias="Distributor")
    AcceptLanguage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-acceptlanguage""", alias="AcceptLanguage")
    SupportUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-supporturl""", alias="SupportUrl")
    SourceConnection_: Optional['SourceConnection'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-sourceconnection""", alias="SourceConnection")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-tags""", alias="Tags")
    ProvisioningArtifactParameters_: Optional[List['ProvisioningArtifactProperties']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-provisioningartifactparameters""", alias="ProvisioningArtifactParameters")
    

    @property
    def tropo_type(self) -> troposphere.servicecatalog.CloudFormationProduct:
        from troposphere.servicecatalog import CloudFormationProduct as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.servicecatalog import CloudFormationProduct as TropoT
        return resource_to_troposphere(self, TropoT)


class CloudFormationProvisionedProduct(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html
    Properties:
        - Name: PathId
        - Name: ProvisioningParameters
        - Name: ProvisioningPreferences
        - Name: ProductName
        - Name: ProvisioningArtifactName
        - Name: NotificationArns
        - Name: AcceptLanguage
        - Name: ProductId
        - Name: PathName
        - Name: Tags
        - Name: ProvisionedProductName
        - Name: ProvisioningArtifactId
    Attributes:
        - Name: CloudformationStackArn
        - Name: Outputs
        - Name: ProvisionedProductId
        - Name: RecordId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PathId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-pathid""", alias="PathId")
    ProvisioningParameters_: Optional[List['ProvisioningParameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningparameters""", alias="ProvisioningParameters")
    ProvisioningPreferences_: Optional['ProvisioningPreferences'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences""", alias="ProvisioningPreferences")
    ProductName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-productname""", alias="ProductName")
    ProvisioningArtifactName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningartifactname""", alias="ProvisioningArtifactName")
    NotificationArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-notificationarns""", alias="NotificationArns")
    AcceptLanguage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-acceptlanguage""", alias="AcceptLanguage")
    ProductId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-productid""", alias="ProductId")
    PathName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-pathname""", alias="PathName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-tags""", alias="Tags")
    ProvisionedProductName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisionedproductname""", alias="ProvisionedProductName")
    ProvisioningArtifactId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningartifactid""", alias="ProvisioningArtifactId")
    

    @property
    def tropo_type(self) -> troposphere.servicecatalog.CloudFormationProvisionedProduct:
        from troposphere.servicecatalog import CloudFormationProvisionedProduct as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.servicecatalog import CloudFormationProvisionedProduct as TropoT
        return resource_to_troposphere(self, TropoT)


class LaunchNotificationConstraint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html
    Properties:
        - Name: Description
        - Name: NotificationArns
        - Name: AcceptLanguage
        - Name: PortfolioId
        - Name: ProductId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-description""", alias="Description")
    NotificationArns_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-notificationarns""", alias="NotificationArns")
    AcceptLanguage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-acceptlanguage""", alias="AcceptLanguage")
    PortfolioId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-portfolioid""", alias="PortfolioId")
    ProductId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-productid""", alias="ProductId")
    

    @property
    def tropo_type(self) -> troposphere.servicecatalog.LaunchNotificationConstraint:
        from troposphere.servicecatalog import LaunchNotificationConstraint as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.servicecatalog import LaunchNotificationConstraint as TropoT
        return resource_to_troposphere(self, TropoT)


class LaunchRoleConstraint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html
    Properties:
        - Name: Description
        - Name: LocalRoleName
        - Name: AcceptLanguage
        - Name: PortfolioId
        - Name: ProductId
        - Name: RoleArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-description""", alias="Description")
    LocalRoleName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-localrolename""", alias="LocalRoleName")
    AcceptLanguage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-acceptlanguage""", alias="AcceptLanguage")
    PortfolioId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-portfolioid""", alias="PortfolioId")
    ProductId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-productid""", alias="ProductId")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-rolearn""", alias="RoleArn")
    

    @property
    def tropo_type(self) -> troposphere.servicecatalog.LaunchRoleConstraint:
        from troposphere.servicecatalog import LaunchRoleConstraint as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.servicecatalog import LaunchRoleConstraint as TropoT
        return resource_to_troposphere(self, TropoT)


class LaunchTemplateConstraint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html
    Properties:
        - Name: Description
        - Name: AcceptLanguage
        - Name: PortfolioId
        - Name: ProductId
        - Name: Rules
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-description""", alias="Description")
    AcceptLanguage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-acceptlanguage""", alias="AcceptLanguage")
    PortfolioId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-portfolioid""", alias="PortfolioId")
    ProductId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-productid""", alias="ProductId")
    Rules_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-rules""", alias="Rules")
    

    @property
    def tropo_type(self) -> troposphere.servicecatalog.LaunchTemplateConstraint:
        from troposphere.servicecatalog import LaunchTemplateConstraint as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.servicecatalog import LaunchTemplateConstraint as TropoT
        return resource_to_troposphere(self, TropoT)


class Portfolio(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html
    Properties:
        - Name: ProviderName
        - Name: Description
        - Name: DisplayName
        - Name: AcceptLanguage
        - Name: Tags
    Attributes:
        - Name: PortfolioName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ProviderName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-providername""", alias="ProviderName")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-description""", alias="Description")
    DisplayName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-displayname""", alias="DisplayName")
    AcceptLanguage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-acceptlanguage""", alias="AcceptLanguage")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.servicecatalog.Portfolio:
        from troposphere.servicecatalog import Portfolio as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.servicecatalog import Portfolio as TropoT
        return resource_to_troposphere(self, TropoT)


class PortfolioPrincipalAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html
    Properties:
        - Name: PrincipalARN
        - Name: AcceptLanguage
        - Name: PortfolioId
        - Name: PrincipalType
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PrincipalARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html#cfn-servicecatalog-portfolioprincipalassociation-principalarn""", alias="PrincipalARN")
    AcceptLanguage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html#cfn-servicecatalog-portfolioprincipalassociation-acceptlanguage""", alias="AcceptLanguage")
    PortfolioId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html#cfn-servicecatalog-portfolioprincipalassociation-portfolioid""", alias="PortfolioId")
    PrincipalType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html#cfn-servicecatalog-portfolioprincipalassociation-principaltype""", alias="PrincipalType")
    

    @property
    def tropo_type(self) -> troposphere.servicecatalog.PortfolioPrincipalAssociation:
        from troposphere.servicecatalog import PortfolioPrincipalAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.servicecatalog import PortfolioPrincipalAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class PortfolioProductAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html
    Properties:
        - Name: SourcePortfolioId
        - Name: AcceptLanguage
        - Name: PortfolioId
        - Name: ProductId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SourcePortfolioId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html#cfn-servicecatalog-portfolioproductassociation-sourceportfolioid""", alias="SourcePortfolioId")
    AcceptLanguage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html#cfn-servicecatalog-portfolioproductassociation-acceptlanguage""", alias="AcceptLanguage")
    PortfolioId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html#cfn-servicecatalog-portfolioproductassociation-portfolioid""", alias="PortfolioId")
    ProductId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html#cfn-servicecatalog-portfolioproductassociation-productid""", alias="ProductId")
    

    @property
    def tropo_type(self) -> troposphere.servicecatalog.PortfolioProductAssociation:
        from troposphere.servicecatalog import PortfolioProductAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.servicecatalog import PortfolioProductAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class PortfolioShare(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html
    Properties:
        - Name: AccountId
        - Name: AcceptLanguage
        - Name: PortfolioId
        - Name: ShareTagOptions
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AccountId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html#cfn-servicecatalog-portfolioshare-accountid""", alias="AccountId")
    AcceptLanguage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html#cfn-servicecatalog-portfolioshare-acceptlanguage""", alias="AcceptLanguage")
    PortfolioId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html#cfn-servicecatalog-portfolioshare-portfolioid""", alias="PortfolioId")
    ShareTagOptions_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html#cfn-servicecatalog-portfolioshare-sharetagoptions""", alias="ShareTagOptions")
    

    @property
    def tropo_type(self) -> troposphere.servicecatalog.PortfolioShare:
        from troposphere.servicecatalog import PortfolioShare as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.servicecatalog import PortfolioShare as TropoT
        return resource_to_troposphere(self, TropoT)


class ResourceUpdateConstraint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html
    Properties:
        - Name: Description
        - Name: AcceptLanguage
        - Name: TagUpdateOnProvisionedProduct
        - Name: PortfolioId
        - Name: ProductId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-description""", alias="Description")
    AcceptLanguage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-acceptlanguage""", alias="AcceptLanguage")
    TagUpdateOnProvisionedProduct_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-tagupdateonprovisionedproduct""", alias="TagUpdateOnProvisionedProduct")
    PortfolioId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-portfolioid""", alias="PortfolioId")
    ProductId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-productid""", alias="ProductId")
    

    @property
    def tropo_type(self) -> troposphere.servicecatalog.ResourceUpdateConstraint:
        from troposphere.servicecatalog import ResourceUpdateConstraint as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.servicecatalog import ResourceUpdateConstraint as TropoT
        return resource_to_troposphere(self, TropoT)


class ServiceAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceaction.html
    Properties:
        - Name: Description
        - Name: Definition
        - Name: AcceptLanguage
        - Name: DefinitionType
        - Name: Name
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceaction.html#cfn-servicecatalog-serviceaction-description""", alias="Description")
    Definition_: List['DefinitionParameter'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceaction.html#cfn-servicecatalog-serviceaction-definition""", alias="Definition")
    AcceptLanguage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceaction.html#cfn-servicecatalog-serviceaction-acceptlanguage""", alias="AcceptLanguage")
    DefinitionType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceaction.html#cfn-servicecatalog-serviceaction-definitiontype""", alias="DefinitionType")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceaction.html#cfn-servicecatalog-serviceaction-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.servicecatalog.ServiceAction:
        from troposphere.servicecatalog import ServiceAction as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.servicecatalog import ServiceAction as TropoT
        return resource_to_troposphere(self, TropoT)


class ServiceActionAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html
    Properties:
        - Name: ServiceActionId
        - Name: ProductId
        - Name: ProvisioningArtifactId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ServiceActionId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html#cfn-servicecatalog-serviceactionassociation-serviceactionid""", alias="ServiceActionId")
    ProductId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html#cfn-servicecatalog-serviceactionassociation-productid""", alias="ProductId")
    ProvisioningArtifactId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html#cfn-servicecatalog-serviceactionassociation-provisioningartifactid""", alias="ProvisioningArtifactId")
    

    @property
    def tropo_type(self) -> troposphere.servicecatalog.ServiceActionAssociation:
        from troposphere.servicecatalog import ServiceActionAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.servicecatalog import ServiceActionAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class StackSetConstraint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html
    Properties:
        - Name: Description
        - Name: StackInstanceControl
        - Name: AcceptLanguage
        - Name: PortfolioId
        - Name: ProductId
        - Name: RegionList
        - Name: AdminRole
        - Name: AccountList
        - Name: ExecutionRole
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-description""", alias="Description")
    StackInstanceControl_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-stackinstancecontrol""", alias="StackInstanceControl")
    AcceptLanguage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-acceptlanguage""", alias="AcceptLanguage")
    PortfolioId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-portfolioid""", alias="PortfolioId")
    ProductId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-productid""", alias="ProductId")
    RegionList_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-regionlist""", alias="RegionList")
    AdminRole_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-adminrole""", alias="AdminRole")
    AccountList_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-accountlist""", alias="AccountList")
    ExecutionRole_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-executionrole""", alias="ExecutionRole")
    

    @property
    def tropo_type(self) -> troposphere.servicecatalog.StackSetConstraint:
        from troposphere.servicecatalog import StackSetConstraint as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.servicecatalog import StackSetConstraint as TropoT
        return resource_to_troposphere(self, TropoT)


class TagOption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoption.html
    Properties:
        - Name: Active
        - Name: Value
        - Name: Key
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Active_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoption.html#cfn-servicecatalog-tagoption-active""", alias="Active")
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoption.html#cfn-servicecatalog-tagoption-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoption.html#cfn-servicecatalog-tagoption-key""", alias="Key")
    

    @property
    def tropo_type(self) -> troposphere.servicecatalog.TagOption:
        from troposphere.servicecatalog import TagOption as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.servicecatalog import TagOption as TropoT
        return resource_to_troposphere(self, TropoT)


class TagOptionAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoptionassociation.html
    Properties:
        - Name: TagOptionId
        - Name: ResourceId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TagOptionId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoptionassociation.html#cfn-servicecatalog-tagoptionassociation-tagoptionid""", alias="TagOptionId")
    ResourceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoptionassociation.html#cfn-servicecatalog-tagoptionassociation-resourceid""", alias="ResourceId")
    

    @property
    def tropo_type(self) -> troposphere.servicecatalog.TagOptionAssociation:
        from troposphere.servicecatalog import TagOptionAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.servicecatalog import TagOptionAssociation as TropoT
        return resource_to_troposphere(self, TropoT)

