from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AccessRules(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-bucket-accessrules.html
    Properties:
        - Name: AllowPublicOverrides
        - Name: GetObject
    
    """
    
    AllowPublicOverrides_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-bucket-accessrules.html#cfn-lightsail-bucket-accessrules-allowpublicoverrides""", alias="AllowPublicOverrides")
    GetObject_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-bucket-accessrules.html#cfn-lightsail-bucket-accessrules-getobject""", alias="GetObject")
    


    @property
    def tropo_type(self) -> troposphere.lightsail.AccessRules:
        from troposphere.lightsail import AccessRules as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Container(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-container.html
    Properties:
        - Name: ContainerName
        - Name: Command
        - Name: Environment
        - Name: Ports
        - Name: Image
    
    """
    
    ContainerName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-container.html#cfn-lightsail-container-container-containername""", alias="ContainerName")
    Command_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-container.html#cfn-lightsail-container-container-command""", alias="Command")
    Environment_: Optional[List['EnvironmentVariable']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-container.html#cfn-lightsail-container-container-environment""", alias="Environment")
    Ports_: Optional[List['PortInfo']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-container.html#cfn-lightsail-container-container-ports""", alias="Ports")
    Image_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-container.html#cfn-lightsail-container-container-image""", alias="Image")
    


    @property
    def tropo_type(self) -> troposphere.lightsail.Container:
        from troposphere.lightsail import Container as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ContainerServiceDeployment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-containerservicedeployment.html
    Properties:
        - Name: Containers
        - Name: PublicEndpoint
    
    """
    
    Containers_: Optional[List['Container']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-containerservicedeployment.html#cfn-lightsail-container-containerservicedeployment-containers""", alias="Containers")
    PublicEndpoint_: Optional['PublicEndpoint'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-containerservicedeployment.html#cfn-lightsail-container-containerservicedeployment-publicendpoint""", alias="PublicEndpoint")
    


    @property
    def tropo_type(self) -> troposphere.lightsail.ContainerServiceDeployment:
        from troposphere.lightsail import ContainerServiceDeployment as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EcrImagePullerRole(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-ecrimagepullerrole.html
    Properties:
        - Name: PrincipalArn
        - Name: IsActive
    
    """
    
    PrincipalArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-ecrimagepullerrole.html#cfn-lightsail-container-ecrimagepullerrole-principalarn""", alias="PrincipalArn")
    IsActive_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-ecrimagepullerrole.html#cfn-lightsail-container-ecrimagepullerrole-isactive""", alias="IsActive")
    


    @property
    def tropo_type(self) -> troposphere.lightsail.EcrImagePullerRole:
        from troposphere.lightsail import EcrImagePullerRole as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EnvironmentVariable(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-environmentvariable.html
    Properties:
        - Name: Variable
        - Name: Value
    
    """
    
    Variable_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-environmentvariable.html#cfn-lightsail-container-environmentvariable-variable""", alias="Variable")
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-environmentvariable.html#cfn-lightsail-container-environmentvariable-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.lightsail.EnvironmentVariable:
        from troposphere.lightsail import EnvironmentVariable as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HealthCheckConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-healthcheckconfig.html
    Properties:
        - Name: Path
        - Name: TimeoutSeconds
        - Name: SuccessCodes
        - Name: UnhealthyThreshold
        - Name: HealthyThreshold
        - Name: IntervalSeconds
    
    """
    
    Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-healthcheckconfig.html#cfn-lightsail-container-healthcheckconfig-path""", alias="Path")
    TimeoutSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-healthcheckconfig.html#cfn-lightsail-container-healthcheckconfig-timeoutseconds""", alias="TimeoutSeconds")
    SuccessCodes_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-healthcheckconfig.html#cfn-lightsail-container-healthcheckconfig-successcodes""", alias="SuccessCodes")
    UnhealthyThreshold_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-healthcheckconfig.html#cfn-lightsail-container-healthcheckconfig-unhealthythreshold""", alias="UnhealthyThreshold")
    HealthyThreshold_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-healthcheckconfig.html#cfn-lightsail-container-healthcheckconfig-healthythreshold""", alias="HealthyThreshold")
    IntervalSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-healthcheckconfig.html#cfn-lightsail-container-healthcheckconfig-intervalseconds""", alias="IntervalSeconds")
    


    @property
    def tropo_type(self) -> troposphere.lightsail.HealthCheckConfig:
        from troposphere.lightsail import HealthCheckConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PortInfo(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-portinfo.html
    Properties:
        - Name: Port
        - Name: Protocol
    
    """
    
    Port_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-portinfo.html#cfn-lightsail-container-portinfo-port""", alias="Port")
    Protocol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-portinfo.html#cfn-lightsail-container-portinfo-protocol""", alias="Protocol")
    


    @property
    def tropo_type(self) -> troposphere.lightsail.PortInfo:
        from troposphere.lightsail import PortInfo as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PrivateRegistryAccess(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-privateregistryaccess.html
    Properties:
        - Name: EcrImagePullerRole
    
    """
    
    EcrImagePullerRole_: Optional['EcrImagePullerRole'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-privateregistryaccess.html#cfn-lightsail-container-privateregistryaccess-ecrimagepullerrole""", alias="EcrImagePullerRole")
    


    @property
    def tropo_type(self) -> troposphere.lightsail.PrivateRegistryAccess:
        from troposphere.lightsail import PrivateRegistryAccess as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PublicDomainName(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-publicdomainname.html
    Properties:
        - Name: CertificateName
        - Name: DomainNames
    
    """
    
    CertificateName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-publicdomainname.html#cfn-lightsail-container-publicdomainname-certificatename""", alias="CertificateName")
    DomainNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-publicdomainname.html#cfn-lightsail-container-publicdomainname-domainnames""", alias="DomainNames")
    


    @property
    def tropo_type(self) -> troposphere.lightsail.PublicDomainName:
        from troposphere.lightsail import PublicDomainName as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PublicEndpoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-publicendpoint.html
    Properties:
        - Name: ContainerName
        - Name: ContainerPort
        - Name: HealthCheckConfig
    
    """
    
    ContainerName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-publicendpoint.html#cfn-lightsail-container-publicendpoint-containername""", alias="ContainerName")
    ContainerPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-publicendpoint.html#cfn-lightsail-container-publicendpoint-containerport""", alias="ContainerPort")
    HealthCheckConfig_: Optional['HealthCheckConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-publicendpoint.html#cfn-lightsail-container-publicendpoint-healthcheckconfig""", alias="HealthCheckConfig")
    


    @property
    def tropo_type(self) -> troposphere.lightsail.PublicEndpoint:
        from troposphere.lightsail import PublicEndpoint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RelationalDatabaseParameter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html
    Properties:
        - Name: ApplyMethod
        - Name: IsModifiable
        - Name: ApplyType
        - Name: AllowedValues
        - Name: Description
        - Name: ParameterValue
        - Name: DataType
        - Name: ParameterName
    
    """
    
    ApplyMethod_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-applymethod""", alias="ApplyMethod")
    IsModifiable_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-ismodifiable""", alias="IsModifiable")
    ApplyType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-applytype""", alias="ApplyType")
    AllowedValues_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-allowedvalues""", alias="AllowedValues")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-description""", alias="Description")
    ParameterValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-parametervalue""", alias="ParameterValue")
    DataType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-datatype""", alias="DataType")
    ParameterName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-parametername""", alias="ParameterName")
    


    @property
    def tropo_type(self) -> troposphere.lightsail.RelationalDatabaseParameter:
        from troposphere.lightsail import RelationalDatabaseParameter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AddOn(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-addon.html
    Properties:
        - Name: Status
        - Name: AddOnType
        - Name: AutoSnapshotAddOnRequest
    
    """
    
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-addon.html#cfn-lightsail-disk-addon-status""", alias="Status")
    AddOnType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-addon.html#cfn-lightsail-disk-addon-addontype""", alias="AddOnType")
    AutoSnapshotAddOnRequest_: Optional['AutoSnapshotAddOn'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-addon.html#cfn-lightsail-disk-addon-autosnapshotaddonrequest""", alias="AutoSnapshotAddOnRequest")
    


    @property
    def tropo_type(self) -> troposphere.lightsail.AddOn:
        from troposphere.lightsail import AddOn as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AutoSnapshotAddOn(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-autosnapshotaddon.html
    Properties:
        - Name: SnapshotTimeOfDay
    
    """
    
    SnapshotTimeOfDay_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-autosnapshotaddon.html#cfn-lightsail-disk-autosnapshotaddon-snapshottimeofday""", alias="SnapshotTimeOfDay")
    


    @property
    def tropo_type(self) -> troposphere.lightsail.AutoSnapshotAddOn:
        from troposphere.lightsail import AutoSnapshotAddOn as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Location(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-location.html
    Properties:
        - Name: RegionName
        - Name: AvailabilityZone
    
    """
    
    RegionName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-location.html#cfn-lightsail-disk-location-regionname""", alias="RegionName")
    AvailabilityZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-location.html#cfn-lightsail-disk-location-availabilityzone""", alias="AvailabilityZone")
    


    @property
    def tropo_type(self) -> troposphere.lightsail.Location:
        from troposphere.lightsail import Location as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CacheBehavior(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachebehavior.html
    Properties:
        - Name: Behavior
    
    """
    
    Behavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachebehavior.html#cfn-lightsail-distribution-cachebehavior-behavior""", alias="Behavior")
    


    @property
    def tropo_type(self) -> troposphere.lightsail.CacheBehavior:
        from troposphere.lightsail import CacheBehavior as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CacheBehaviorPerPath(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachebehaviorperpath.html
    Properties:
        - Name: Path
        - Name: Behavior
    
    """
    
    Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachebehaviorperpath.html#cfn-lightsail-distribution-cachebehaviorperpath-path""", alias="Path")
    Behavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachebehaviorperpath.html#cfn-lightsail-distribution-cachebehaviorperpath-behavior""", alias="Behavior")
    


    @property
    def tropo_type(self) -> troposphere.lightsail.CacheBehaviorPerPath:
        from troposphere.lightsail import CacheBehaviorPerPath as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CacheSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachesettings.html
    Properties:
        - Name: ForwardedCookies
        - Name: MinimumTTL
        - Name: CachedHTTPMethods
        - Name: AllowedHTTPMethods
        - Name: MaximumTTL
        - Name: ForwardedHeaders
        - Name: DefaultTTL
        - Name: ForwardedQueryStrings
    
    """
    
    ForwardedCookies_: Optional['CookieObject'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachesettings.html#cfn-lightsail-distribution-cachesettings-forwardedcookies""", alias="ForwardedCookies")
    MinimumTTL_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachesettings.html#cfn-lightsail-distribution-cachesettings-minimumttl""", alias="MinimumTTL")
    CachedHTTPMethods_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachesettings.html#cfn-lightsail-distribution-cachesettings-cachedhttpmethods""", alias="CachedHTTPMethods")
    AllowedHTTPMethods_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachesettings.html#cfn-lightsail-distribution-cachesettings-allowedhttpmethods""", alias="AllowedHTTPMethods")
    MaximumTTL_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachesettings.html#cfn-lightsail-distribution-cachesettings-maximumttl""", alias="MaximumTTL")
    ForwardedHeaders_: Optional['HeaderObject'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachesettings.html#cfn-lightsail-distribution-cachesettings-forwardedheaders""", alias="ForwardedHeaders")
    DefaultTTL_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachesettings.html#cfn-lightsail-distribution-cachesettings-defaultttl""", alias="DefaultTTL")
    ForwardedQueryStrings_: Optional['QueryStringObject'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachesettings.html#cfn-lightsail-distribution-cachesettings-forwardedquerystrings""", alias="ForwardedQueryStrings")
    


    @property
    def tropo_type(self) -> troposphere.lightsail.CacheSettings:
        from troposphere.lightsail import CacheSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CookieObject(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cookieobject.html
    Properties:
        - Name: CookiesAllowList
        - Name: Option
    
    """
    
    CookiesAllowList_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cookieobject.html#cfn-lightsail-distribution-cookieobject-cookiesallowlist""", alias="CookiesAllowList")
    Option_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cookieobject.html#cfn-lightsail-distribution-cookieobject-option""", alias="Option")
    


    @property
    def tropo_type(self) -> troposphere.lightsail.CookieObject:
        from troposphere.lightsail import CookieObject as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HeaderObject(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-headerobject.html
    Properties:
        - Name: HeadersAllowList
        - Name: Option
    
    """
    
    HeadersAllowList_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-headerobject.html#cfn-lightsail-distribution-headerobject-headersallowlist""", alias="HeadersAllowList")
    Option_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-headerobject.html#cfn-lightsail-distribution-headerobject-option""", alias="Option")
    


    @property
    def tropo_type(self) -> troposphere.lightsail.HeaderObject:
        from troposphere.lightsail import HeaderObject as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InputOrigin(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-inputorigin.html
    Properties:
        - Name: RegionName
        - Name: ProtocolPolicy
        - Name: Name
    
    """
    
    RegionName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-inputorigin.html#cfn-lightsail-distribution-inputorigin-regionname""", alias="RegionName")
    ProtocolPolicy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-inputorigin.html#cfn-lightsail-distribution-inputorigin-protocolpolicy""", alias="ProtocolPolicy")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-inputorigin.html#cfn-lightsail-distribution-inputorigin-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.lightsail.InputOrigin:
        from troposphere.lightsail import InputOrigin as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class QueryStringObject(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-querystringobject.html
    Properties:
        - Name: Option
        - Name: QueryStringsAllowList
    
    """
    
    Option_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-querystringobject.html#cfn-lightsail-distribution-querystringobject-option""", alias="Option")
    QueryStringsAllowList_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-querystringobject.html#cfn-lightsail-distribution-querystringobject-querystringsallowlist""", alias="QueryStringsAllowList")
    


    @property
    def tropo_type(self) -> troposphere.lightsail.QueryStringObject:
        from troposphere.lightsail import QueryStringObject as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AddOn(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-addon.html
    Properties:
        - Name: Status
        - Name: AddOnType
        - Name: AutoSnapshotAddOnRequest
    
    """
    
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-addon.html#cfn-lightsail-instance-addon-status""", alias="Status")
    AddOnType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-addon.html#cfn-lightsail-instance-addon-addontype""", alias="AddOnType")
    AutoSnapshotAddOnRequest_: Optional['AutoSnapshotAddOn'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-addon.html#cfn-lightsail-instance-addon-autosnapshotaddonrequest""", alias="AutoSnapshotAddOnRequest")
    


    @property
    def tropo_type(self) -> troposphere.lightsail.AddOn:
        from troposphere.lightsail import AddOn as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AutoSnapshotAddOn(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-autosnapshotaddon.html
    Properties:
        - Name: SnapshotTimeOfDay
    
    """
    
    SnapshotTimeOfDay_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-autosnapshotaddon.html#cfn-lightsail-instance-autosnapshotaddon-snapshottimeofday""", alias="SnapshotTimeOfDay")
    


    @property
    def tropo_type(self) -> troposphere.lightsail.AutoSnapshotAddOn:
        from troposphere.lightsail import AutoSnapshotAddOn as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Disk(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html
    Properties:
        - Name: SizeInGb
        - Name: Path
        - Name: AttachmentState
        - Name: IsSystemDisk
        - Name: AttachedTo
        - Name: IOPS
        - Name: DiskName
    
    """
    
    SizeInGb_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-sizeingb""", alias="SizeInGb")
    Path_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-path""", alias="Path")
    AttachmentState_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-attachmentstate""", alias="AttachmentState")
    IsSystemDisk_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-issystemdisk""", alias="IsSystemDisk")
    AttachedTo_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-attachedto""", alias="AttachedTo")
    IOPS_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-iops""", alias="IOPS")
    DiskName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-diskname""", alias="DiskName")
    


    @property
    def tropo_type(self) -> troposphere.lightsail.Disk:
        from troposphere.lightsail import Disk as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Hardware(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-hardware.html
    Properties:
        - Name: CpuCount
        - Name: RamSizeInGb
        - Name: Disks
    
    """
    
    CpuCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-hardware.html#cfn-lightsail-instance-hardware-cpucount""", alias="CpuCount")
    RamSizeInGb_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-hardware.html#cfn-lightsail-instance-hardware-ramsizeingb""", alias="RamSizeInGb")
    Disks_: Optional[List['Disk']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-hardware.html#cfn-lightsail-instance-hardware-disks""", alias="Disks")
    


    @property
    def tropo_type(self) -> troposphere.lightsail.Hardware:
        from troposphere.lightsail import Hardware as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Location(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-location.html
    Properties:
        - Name: RegionName
        - Name: AvailabilityZone
    
    """
    
    RegionName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-location.html#cfn-lightsail-instance-location-regionname""", alias="RegionName")
    AvailabilityZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-location.html#cfn-lightsail-instance-location-availabilityzone""", alias="AvailabilityZone")
    


    @property
    def tropo_type(self) -> troposphere.lightsail.Location:
        from troposphere.lightsail import Location as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MonthlyTransfer(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-monthlytransfer.html
    Properties:
        - Name: GbPerMonthAllocated
    
    """
    
    GbPerMonthAllocated_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-monthlytransfer.html#cfn-lightsail-instance-monthlytransfer-gbpermonthallocated""", alias="GbPerMonthAllocated")
    


    @property
    def tropo_type(self) -> troposphere.lightsail.MonthlyTransfer:
        from troposphere.lightsail import MonthlyTransfer as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Networking(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-networking.html
    Properties:
        - Name: Ports
        - Name: MonthlyTransfer
    
    """
    
    Ports_: List['Port'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-networking.html#cfn-lightsail-instance-networking-ports""", alias="Ports")
    MonthlyTransfer_: Optional['MonthlyTransfer'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-networking.html#cfn-lightsail-instance-networking-monthlytransfer""", alias="MonthlyTransfer")
    


    @property
    def tropo_type(self) -> troposphere.lightsail.Networking:
        from troposphere.lightsail import Networking as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Port(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html
    Properties:
        - Name: FromPort
        - Name: AccessDirection
        - Name: CidrListAliases
        - Name: ToPort
        - Name: Ipv6Cidrs
        - Name: AccessFrom
        - Name: Protocol
        - Name: AccessType
        - Name: Cidrs
        - Name: CommonName
    
    """
    
    FromPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-fromport""", alias="FromPort")
    AccessDirection_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-accessdirection""", alias="AccessDirection")
    CidrListAliases_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-cidrlistaliases""", alias="CidrListAliases")
    ToPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-toport""", alias="ToPort")
    Ipv6Cidrs_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-ipv6cidrs""", alias="Ipv6Cidrs")
    AccessFrom_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-accessfrom""", alias="AccessFrom")
    Protocol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-protocol""", alias="Protocol")
    AccessType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-accesstype""", alias="AccessType")
    Cidrs_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-cidrs""", alias="Cidrs")
    CommonName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-commonname""", alias="CommonName")
    


    @property
    def tropo_type(self) -> troposphere.lightsail.Port:
        from troposphere.lightsail import Port as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class State(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-state.html
    Properties:
        - Name: Code
        - Name: Name
    
    """
    
    Code_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-state.html#cfn-lightsail-instance-state-code""", alias="Code")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-state.html#cfn-lightsail-instance-state-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.lightsail.State:
        from troposphere.lightsail import State as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Alarm(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-alarm.html
    Properties:
        - Name: MetricName
        - Name: ComparisonOperator
        - Name: TreatMissingData
        - Name: AlarmName
        - Name: ContactProtocols
        - Name: MonitoredResourceName
        - Name: EvaluationPeriods
        - Name: NotificationEnabled
        - Name: DatapointsToAlarm
        - Name: NotificationTriggers
        - Name: Threshold
    Attributes:
        - Name: AlarmArn
        - Name: State
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MetricName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-alarm.html#cfn-lightsail-alarm-metricname""", alias="MetricName")
    ComparisonOperator_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-alarm.html#cfn-lightsail-alarm-comparisonoperator""", alias="ComparisonOperator")
    TreatMissingData_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-alarm.html#cfn-lightsail-alarm-treatmissingdata""", alias="TreatMissingData")
    AlarmName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-alarm.html#cfn-lightsail-alarm-alarmname""", alias="AlarmName")
    ContactProtocols_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-alarm.html#cfn-lightsail-alarm-contactprotocols""", alias="ContactProtocols")
    MonitoredResourceName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-alarm.html#cfn-lightsail-alarm-monitoredresourcename""", alias="MonitoredResourceName")
    EvaluationPeriods_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-alarm.html#cfn-lightsail-alarm-evaluationperiods""", alias="EvaluationPeriods")
    NotificationEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-alarm.html#cfn-lightsail-alarm-notificationenabled""", alias="NotificationEnabled")
    DatapointsToAlarm_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-alarm.html#cfn-lightsail-alarm-datapointstoalarm""", alias="DatapointsToAlarm")
    NotificationTriggers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-alarm.html#cfn-lightsail-alarm-notificationtriggers""", alias="NotificationTriggers")
    Threshold_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-alarm.html#cfn-lightsail-alarm-threshold""", alias="Threshold")
    

    @property
    def tropo_type(self) -> troposphere.lightsail.Alarm:
        from troposphere.lightsail import Alarm as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.lightsail import Alarm as TropoT
        return resource_to_troposphere(self, TropoT)


class Bucket(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-bucket.html
    Properties:
        - Name: ObjectVersioning
        - Name: ReadOnlyAccessAccounts
        - Name: BundleId
        - Name: BucketName
        - Name: AccessRules
        - Name: ResourcesReceivingAccess
        - Name: Tags
    Attributes:
        - Name: BucketArn
        - Name: AbleToUpdateBundle
        - Name: Url
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ObjectVersioning_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-bucket.html#cfn-lightsail-bucket-objectversioning""", alias="ObjectVersioning")
    ReadOnlyAccessAccounts_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-bucket.html#cfn-lightsail-bucket-readonlyaccessaccounts""", alias="ReadOnlyAccessAccounts")
    BundleId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-bucket.html#cfn-lightsail-bucket-bundleid""", alias="BundleId")
    BucketName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-bucket.html#cfn-lightsail-bucket-bucketname""", alias="BucketName")
    AccessRules_: Optional['AccessRules'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-bucket.html#cfn-lightsail-bucket-accessrules""", alias="AccessRules")
    ResourcesReceivingAccess_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-bucket.html#cfn-lightsail-bucket-resourcesreceivingaccess""", alias="ResourcesReceivingAccess")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-bucket.html#cfn-lightsail-bucket-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.lightsail.Bucket:
        from troposphere.lightsail import Bucket as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.lightsail import Bucket as TropoT
        return resource_to_troposphere(self, TropoT)


class Certificate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-certificate.html
    Properties:
        - Name: DomainName
        - Name: SubjectAlternativeNames
        - Name: CertificateName
        - Name: Tags
    Attributes:
        - Name: Status
        - Name: CertificateArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DomainName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-certificate.html#cfn-lightsail-certificate-domainname""", alias="DomainName")
    SubjectAlternativeNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-certificate.html#cfn-lightsail-certificate-subjectalternativenames""", alias="SubjectAlternativeNames")
    CertificateName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-certificate.html#cfn-lightsail-certificate-certificatename""", alias="CertificateName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-certificate.html#cfn-lightsail-certificate-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.lightsail.Certificate:
        from troposphere.lightsail import Certificate as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.lightsail import Certificate as TropoT
        return resource_to_troposphere(self, TropoT)


class Container(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-container.html
    Properties:
        - Name: PublicDomainNames
        - Name: ServiceName
        - Name: PrivateRegistryAccess
        - Name: ContainerServiceDeployment
        - Name: IsDisabled
        - Name: Scale
        - Name: Power
        - Name: Tags
    Attributes:
        - Name: PrincipalArn
        - Name: PrivateRegistryAccess.EcrImagePullerRole.PrincipalArn
        - Name: ContainerArn
        - Name: Url
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PublicDomainNames_: Optional[List['PublicDomainName']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-container.html#cfn-lightsail-container-publicdomainnames""", alias="PublicDomainNames")
    ServiceName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-container.html#cfn-lightsail-container-servicename""", alias="ServiceName")
    PrivateRegistryAccess_: Optional['PrivateRegistryAccess'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-container.html#cfn-lightsail-container-privateregistryaccess""", alias="PrivateRegistryAccess")
    ContainerServiceDeployment_: Optional['ContainerServiceDeployment'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-container.html#cfn-lightsail-container-containerservicedeployment""", alias="ContainerServiceDeployment")
    IsDisabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-container.html#cfn-lightsail-container-isdisabled""", alias="IsDisabled")
    Scale_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-container.html#cfn-lightsail-container-scale""", alias="Scale")
    Power_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-container.html#cfn-lightsail-container-power""", alias="Power")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-container.html#cfn-lightsail-container-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.lightsail.Container:
        from troposphere.lightsail import Container as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.lightsail import Container as TropoT
        return resource_to_troposphere(self, TropoT)


class Database(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html
    Properties:
        - Name: RelationalDatabaseName
        - Name: CaCertificateIdentifier
        - Name: AvailabilityZone
        - Name: PreferredMaintenanceWindow
        - Name: RelationalDatabaseBlueprintId
        - Name: PreferredBackupWindow
        - Name: MasterDatabaseName
        - Name: MasterUserPassword
        - Name: RelationalDatabaseParameters
        - Name: RotateMasterUserPassword
        - Name: MasterUsername
        - Name: PubliclyAccessible
        - Name: RelationalDatabaseBundleId
        - Name: BackupRetention
        - Name: Tags
    Attributes:
        - Name: DatabaseArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    RelationalDatabaseName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-relationaldatabasename""", alias="RelationalDatabaseName")
    CaCertificateIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-cacertificateidentifier""", alias="CaCertificateIdentifier")
    AvailabilityZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-availabilityzone""", alias="AvailabilityZone")
    PreferredMaintenanceWindow_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-preferredmaintenancewindow""", alias="PreferredMaintenanceWindow")
    RelationalDatabaseBlueprintId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-relationaldatabaseblueprintid""", alias="RelationalDatabaseBlueprintId")
    PreferredBackupWindow_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-preferredbackupwindow""", alias="PreferredBackupWindow")
    MasterDatabaseName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-masterdatabasename""", alias="MasterDatabaseName")
    MasterUserPassword_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-masteruserpassword""", alias="MasterUserPassword")
    RelationalDatabaseParameters_: Optional[List['RelationalDatabaseParameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-relationaldatabaseparameters""", alias="RelationalDatabaseParameters")
    RotateMasterUserPassword_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-rotatemasteruserpassword""", alias="RotateMasterUserPassword")
    MasterUsername_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-masterusername""", alias="MasterUsername")
    PubliclyAccessible_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-publiclyaccessible""", alias="PubliclyAccessible")
    RelationalDatabaseBundleId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-relationaldatabasebundleid""", alias="RelationalDatabaseBundleId")
    BackupRetention_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-backupretention""", alias="BackupRetention")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.lightsail.Database:
        from troposphere.lightsail import Database as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.lightsail import Database as TropoT
        return resource_to_troposphere(self, TropoT)


class Disk(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html
    Properties:
        - Name: SizeInGb
        - Name: AvailabilityZone
        - Name: AddOns
        - Name: DiskName
        - Name: Tags
        - Name: Location
    Attributes:
        - Name: Path
        - Name: AttachmentState
        - Name: Location.AvailabilityZone
        - Name: SupportCode
        - Name: State
        - Name: IsAttached
        - Name: ResourceType
        - Name: DiskArn
        - Name: AttachedTo
        - Name: Iops
        - Name: Location.RegionName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SizeInGb_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-sizeingb""", alias="SizeInGb")
    AvailabilityZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-availabilityzone""", alias="AvailabilityZone")
    AddOns_: Optional[List['AddOn']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-addons""", alias="AddOns")
    DiskName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-diskname""", alias="DiskName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-tags""", alias="Tags")
    Location_: Optional['Location'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-location""", alias="Location")
    

    @property
    def tropo_type(self) -> troposphere.lightsail.Disk:
        from troposphere.lightsail import Disk as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.lightsail import Disk as TropoT
        return resource_to_troposphere(self, TropoT)


class Distribution(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-distribution.html
    Properties:
        - Name: IpAddressType
        - Name: Origin
        - Name: DistributionName
        - Name: BundleId
        - Name: DefaultCacheBehavior
        - Name: IsEnabled
        - Name: CacheBehaviorSettings
        - Name: CertificateName
        - Name: Tags
        - Name: CacheBehaviors
    Attributes:
        - Name: Status
        - Name: DistributionArn
        - Name: AbleToUpdateBundle
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    IpAddressType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-distribution.html#cfn-lightsail-distribution-ipaddresstype""", alias="IpAddressType")
    Origin_: 'InputOrigin' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-distribution.html#cfn-lightsail-distribution-origin""", alias="Origin")
    DistributionName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-distribution.html#cfn-lightsail-distribution-distributionname""", alias="DistributionName")
    BundleId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-distribution.html#cfn-lightsail-distribution-bundleid""", alias="BundleId")
    DefaultCacheBehavior_: 'CacheBehavior' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-distribution.html#cfn-lightsail-distribution-defaultcachebehavior""", alias="DefaultCacheBehavior")
    IsEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-distribution.html#cfn-lightsail-distribution-isenabled""", alias="IsEnabled")
    CacheBehaviorSettings_: Optional['CacheSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-distribution.html#cfn-lightsail-distribution-cachebehaviorsettings""", alias="CacheBehaviorSettings")
    CertificateName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-distribution.html#cfn-lightsail-distribution-certificatename""", alias="CertificateName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-distribution.html#cfn-lightsail-distribution-tags""", alias="Tags")
    CacheBehaviors_: Optional[List['CacheBehaviorPerPath']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-distribution.html#cfn-lightsail-distribution-cachebehaviors""", alias="CacheBehaviors")
    

    @property
    def tropo_type(self) -> troposphere.lightsail.Distribution:
        from troposphere.lightsail import Distribution as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.lightsail import Distribution as TropoT
        return resource_to_troposphere(self, TropoT)


class Instance(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html
    Properties:
        - Name: InstanceName
        - Name: KeyPairName
        - Name: BundleId
        - Name: BlueprintId
        - Name: Networking
        - Name: UserData
        - Name: State
        - Name: AvailabilityZone
        - Name: AddOns
        - Name: Hardware
        - Name: Tags
        - Name: Location
    Attributes:
        - Name: SshKeyName
        - Name: Networking.MonthlyTransfer.GbPerMonthAllocated
        - Name: Hardware.CpuCount
        - Name: IsStaticIp
        - Name: PrivateIpAddress
        - Name: UserName
        - Name: ResourceType
        - Name: Location.RegionName
        - Name: PublicIpAddress
        - Name: Location.AvailabilityZone
        - Name: State.Code
        - Name: SupportCode
        - Name: State.Name
        - Name: InstanceArn
        - Name: Hardware.RamSizeInGb
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    InstanceName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-instancename""", alias="InstanceName")
    KeyPairName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-keypairname""", alias="KeyPairName")
    BundleId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-bundleid""", alias="BundleId")
    BlueprintId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-blueprintid""", alias="BlueprintId")
    Networking_: Optional['Networking'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-networking""", alias="Networking")
    UserData_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-userdata""", alias="UserData")
    State_: Optional['State'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-state""", alias="State")
    AvailabilityZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-availabilityzone""", alias="AvailabilityZone")
    AddOns_: Optional[List['AddOn']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-addons""", alias="AddOns")
    Hardware_: Optional['Hardware'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-hardware""", alias="Hardware")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-tags""", alias="Tags")
    Location_: Optional['Location'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-location""", alias="Location")
    

    @property
    def tropo_type(self) -> troposphere.lightsail.Instance:
        from troposphere.lightsail import Instance as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.lightsail import Instance as TropoT
        return resource_to_troposphere(self, TropoT)


class LoadBalancer(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancer.html
    Properties:
        - Name: IpAddressType
        - Name: SessionStickinessLBCookieDurationSeconds
        - Name: LoadBalancerName
        - Name: AttachedInstances
        - Name: InstancePort
        - Name: HealthCheckPath
        - Name: SessionStickinessEnabled
        - Name: TlsPolicyName
        - Name: Tags
    Attributes:
        - Name: LoadBalancerArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    IpAddressType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancer.html#cfn-lightsail-loadbalancer-ipaddresstype""", alias="IpAddressType")
    SessionStickinessLBCookieDurationSeconds_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancer.html#cfn-lightsail-loadbalancer-sessionstickinesslbcookiedurationseconds""", alias="SessionStickinessLBCookieDurationSeconds")
    LoadBalancerName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancer.html#cfn-lightsail-loadbalancer-loadbalancername""", alias="LoadBalancerName")
    AttachedInstances_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancer.html#cfn-lightsail-loadbalancer-attachedinstances""", alias="AttachedInstances")
    InstancePort_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancer.html#cfn-lightsail-loadbalancer-instanceport""", alias="InstancePort")
    HealthCheckPath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancer.html#cfn-lightsail-loadbalancer-healthcheckpath""", alias="HealthCheckPath")
    SessionStickinessEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancer.html#cfn-lightsail-loadbalancer-sessionstickinessenabled""", alias="SessionStickinessEnabled")
    TlsPolicyName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancer.html#cfn-lightsail-loadbalancer-tlspolicyname""", alias="TlsPolicyName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancer.html#cfn-lightsail-loadbalancer-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.lightsail.LoadBalancer:
        from troposphere.lightsail import LoadBalancer as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.lightsail import LoadBalancer as TropoT
        return resource_to_troposphere(self, TropoT)


class LoadBalancerTlsCertificate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancertlscertificate.html
    Properties:
        - Name: LoadBalancerName
        - Name: CertificateDomainName
        - Name: IsAttached
        - Name: CertificateAlternativeNames
        - Name: HttpsRedirectionEnabled
        - Name: CertificateName
    Attributes:
        - Name: Status
        - Name: LoadBalancerTlsCertificateArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    LoadBalancerName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancertlscertificate.html#cfn-lightsail-loadbalancertlscertificate-loadbalancername""", alias="LoadBalancerName")
    CertificateDomainName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancertlscertificate.html#cfn-lightsail-loadbalancertlscertificate-certificatedomainname""", alias="CertificateDomainName")
    IsAttached_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancertlscertificate.html#cfn-lightsail-loadbalancertlscertificate-isattached""", alias="IsAttached")
    CertificateAlternativeNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancertlscertificate.html#cfn-lightsail-loadbalancertlscertificate-certificatealternativenames""", alias="CertificateAlternativeNames")
    HttpsRedirectionEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancertlscertificate.html#cfn-lightsail-loadbalancertlscertificate-httpsredirectionenabled""", alias="HttpsRedirectionEnabled")
    CertificateName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancertlscertificate.html#cfn-lightsail-loadbalancertlscertificate-certificatename""", alias="CertificateName")
    

    @property
    def tropo_type(self) -> troposphere.lightsail.LoadBalancerTlsCertificate:
        from troposphere.lightsail import LoadBalancerTlsCertificate as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.lightsail import LoadBalancerTlsCertificate as TropoT
        return resource_to_troposphere(self, TropoT)


class StaticIp(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-staticip.html
    Properties:
        - Name: StaticIpName
        - Name: AttachedTo
    Attributes:
        - Name: StaticIpArn
        - Name: IsAttached
        - Name: IpAddress
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    StaticIpName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-staticip.html#cfn-lightsail-staticip-staticipname""", alias="StaticIpName")
    AttachedTo_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-staticip.html#cfn-lightsail-staticip-attachedto""", alias="AttachedTo")
    

    @property
    def tropo_type(self) -> troposphere.lightsail.StaticIp:
        from troposphere.lightsail import StaticIp as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.lightsail import StaticIp as TropoT
        return resource_to_troposphere(self, TropoT)

