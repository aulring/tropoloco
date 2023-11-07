from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AuditCheckConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfiguration.html
    Properties:
        - Name: Enabled
    
    """
    
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfiguration.html#cfn-iot-accountauditconfiguration-auditcheckconfiguration-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.iot.AuditCheckConfiguration:
        from troposphere.iot import AuditCheckConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AuditCheckConfigurations(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html
    Properties:
        - Name: IotRoleAliasOverlyPermissiveCheck
        - Name: DeviceCertificateSharedCheck
        - Name: ConflictingClientIdsCheck
        - Name: IntermediateCaRevokedForActiveDeviceCertificatesCheck
        - Name: IotRoleAliasAllowsAccessToUnusedServicesCheck
        - Name: RevokedCaCertificateStillActiveCheck
        - Name: LoggingDisabledCheck
        - Name: UnauthenticatedCognitoRoleOverlyPermissiveCheck
        - Name: AuthenticatedCognitoRoleOverlyPermissiveCheck
        - Name: CaCertificateExpiringCheck
        - Name: DeviceCertificateExpiringCheck
        - Name: IoTPolicyPotentialMisConfigurationCheck
        - Name: IotPolicyOverlyPermissiveCheck
        - Name: RevokedDeviceCertificateStillActiveCheck
        - Name: DeviceCertificateKeyQualityCheck
        - Name: CaCertificateKeyQualityCheck
    
    """
    
    IotRoleAliasOverlyPermissiveCheck_: Optional['AuditCheckConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-iotrolealiasoverlypermissivecheck""", alias="IotRoleAliasOverlyPermissiveCheck")
    DeviceCertificateSharedCheck_: Optional['AuditCheckConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-devicecertificatesharedcheck""", alias="DeviceCertificateSharedCheck")
    ConflictingClientIdsCheck_: Optional['AuditCheckConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-conflictingclientidscheck""", alias="ConflictingClientIdsCheck")
    IntermediateCaRevokedForActiveDeviceCertificatesCheck_: Optional['AuditCheckConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-intermediatecarevokedforactivedevicecertificatescheck""", alias="IntermediateCaRevokedForActiveDeviceCertificatesCheck")
    IotRoleAliasAllowsAccessToUnusedServicesCheck_: Optional['AuditCheckConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-iotrolealiasallowsaccesstounusedservicescheck""", alias="IotRoleAliasAllowsAccessToUnusedServicesCheck")
    RevokedCaCertificateStillActiveCheck_: Optional['AuditCheckConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-revokedcacertificatestillactivecheck""", alias="RevokedCaCertificateStillActiveCheck")
    LoggingDisabledCheck_: Optional['AuditCheckConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-loggingdisabledcheck""", alias="LoggingDisabledCheck")
    UnauthenticatedCognitoRoleOverlyPermissiveCheck_: Optional['AuditCheckConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-unauthenticatedcognitoroleoverlypermissivecheck""", alias="UnauthenticatedCognitoRoleOverlyPermissiveCheck")
    AuthenticatedCognitoRoleOverlyPermissiveCheck_: Optional['AuditCheckConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-authenticatedcognitoroleoverlypermissivecheck""", alias="AuthenticatedCognitoRoleOverlyPermissiveCheck")
    CaCertificateExpiringCheck_: Optional['AuditCheckConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-cacertificateexpiringcheck""", alias="CaCertificateExpiringCheck")
    DeviceCertificateExpiringCheck_: Optional['AuditCheckConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-devicecertificateexpiringcheck""", alias="DeviceCertificateExpiringCheck")
    IoTPolicyPotentialMisConfigurationCheck_: Optional['AuditCheckConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-iotpolicypotentialmisconfigurationcheck""", alias="IoTPolicyPotentialMisConfigurationCheck")
    IotPolicyOverlyPermissiveCheck_: Optional['AuditCheckConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-iotpolicyoverlypermissivecheck""", alias="IotPolicyOverlyPermissiveCheck")
    RevokedDeviceCertificateStillActiveCheck_: Optional['AuditCheckConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-revokeddevicecertificatestillactivecheck""", alias="RevokedDeviceCertificateStillActiveCheck")
    DeviceCertificateKeyQualityCheck_: Optional['AuditCheckConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-devicecertificatekeyqualitycheck""", alias="DeviceCertificateKeyQualityCheck")
    CaCertificateKeyQualityCheck_: Optional['AuditCheckConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-cacertificatekeyqualitycheck""", alias="CaCertificateKeyQualityCheck")
    


    @property
    def tropo_type(self) -> troposphere.iot.AuditCheckConfigurations:
        from troposphere.iot import AuditCheckConfigurations as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AuditNotificationTarget(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditnotificationtarget.html
    Properties:
        - Name: TargetArn
        - Name: Enabled
        - Name: RoleArn
    
    """
    
    TargetArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditnotificationtarget.html#cfn-iot-accountauditconfiguration-auditnotificationtarget-targetarn""", alias="TargetArn")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditnotificationtarget.html#cfn-iot-accountauditconfiguration-auditnotificationtarget-enabled""", alias="Enabled")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditnotificationtarget.html#cfn-iot-accountauditconfiguration-auditnotificationtarget-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.iot.AuditNotificationTarget:
        from troposphere.iot import AuditNotificationTarget as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AuditNotificationTargetConfigurations(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditnotificationtargetconfigurations.html
    Properties:
        - Name: Sns
    
    """
    
    Sns_: Optional['AuditNotificationTarget'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditnotificationtargetconfigurations.html#cfn-iot-accountauditconfiguration-auditnotificationtargetconfigurations-sns""", alias="Sns")
    


    @property
    def tropo_type(self) -> troposphere.iot.AuditNotificationTargetConfigurations:
        from troposphere.iot import AuditNotificationTargetConfigurations as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BillingGroupProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-billinggroup-billinggroupproperties.html
    Properties:
        - Name: BillingGroupDescription
    
    """
    
    BillingGroupDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-billinggroup-billinggroupproperties.html#cfn-iot-billinggroup-billinggroupproperties-billinggroupdescription""", alias="BillingGroupDescription")
    


    @property
    def tropo_type(self) -> troposphere.iot.BillingGroupProperties:
        from troposphere.iot import BillingGroupProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RegistrationConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-cacertificate-registrationconfig.html
    Properties:
        - Name: TemplateName
        - Name: TemplateBody
        - Name: RoleArn
    
    """
    
    TemplateName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-cacertificate-registrationconfig.html#cfn-iot-cacertificate-registrationconfig-templatename""", alias="TemplateName")
    TemplateBody_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-cacertificate-registrationconfig.html#cfn-iot-cacertificate-registrationconfig-templatebody""", alias="TemplateBody")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-cacertificate-registrationconfig.html#cfn-iot-cacertificate-registrationconfig-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.iot.RegistrationConfig:
        from troposphere.iot import RegistrationConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AuthorizerConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-domainconfiguration-authorizerconfig.html
    Properties:
        - Name: DefaultAuthorizerName
        - Name: AllowAuthorizerOverride
    
    """
    
    DefaultAuthorizerName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-domainconfiguration-authorizerconfig.html#cfn-iot-domainconfiguration-authorizerconfig-defaultauthorizername""", alias="DefaultAuthorizerName")
    AllowAuthorizerOverride_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-domainconfiguration-authorizerconfig.html#cfn-iot-domainconfiguration-authorizerconfig-allowauthorizeroverride""", alias="AllowAuthorizerOverride")
    


    @property
    def tropo_type(self) -> troposphere.iot.AuthorizerConfig:
        from troposphere.iot import AuthorizerConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ServerCertificateSummary(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-domainconfiguration-servercertificatesummary.html
    Properties:
        - Name: ServerCertificateStatusDetail
        - Name: ServerCertificateArn
        - Name: ServerCertificateStatus
    
    """
    
    ServerCertificateStatusDetail_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-domainconfiguration-servercertificatesummary.html#cfn-iot-domainconfiguration-servercertificatesummary-servercertificatestatusdetail""", alias="ServerCertificateStatusDetail")
    ServerCertificateArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-domainconfiguration-servercertificatesummary.html#cfn-iot-domainconfiguration-servercertificatesummary-servercertificatearn""", alias="ServerCertificateArn")
    ServerCertificateStatus_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-domainconfiguration-servercertificatesummary.html#cfn-iot-domainconfiguration-servercertificatesummary-servercertificatestatus""", alias="ServerCertificateStatus")
    


    @property
    def tropo_type(self) -> troposphere.iot.ServerCertificateSummary:
        from troposphere.iot import ServerCertificateSummary as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TlsConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-domainconfiguration-tlsconfig.html
    Properties:
        - Name: SecurityPolicy
    
    """
    
    SecurityPolicy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-domainconfiguration-tlsconfig.html#cfn-iot-domainconfiguration-tlsconfig-securitypolicy""", alias="SecurityPolicy")
    


    @property
    def tropo_type(self) -> troposphere.iot.TlsConfig:
        from troposphere.iot import TlsConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AggregationType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-fleetmetric-aggregationtype.html
    Properties:
        - Name: Values
        - Name: Name
    
    """
    
    Values_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-fleetmetric-aggregationtype.html#cfn-iot-fleetmetric-aggregationtype-values""", alias="Values")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-fleetmetric-aggregationtype.html#cfn-iot-fleetmetric-aggregationtype-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.iot.AggregationType:
        from troposphere.iot import AggregationType as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AbortConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-abortconfig.html
    Properties:
        - Name: CriteriaList
    
    """
    
    CriteriaList_: List['AbortCriteria'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-abortconfig.html#cfn-iot-jobtemplate-abortconfig-criterialist""", alias="CriteriaList")
    


    @property
    def tropo_type(self) -> troposphere.iot.AbortConfig:
        from troposphere.iot import AbortConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AbortCriteria(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-abortcriteria.html
    Properties:
        - Name: Action
        - Name: FailureType
        - Name: ThresholdPercentage
        - Name: MinNumberOfExecutedThings
    
    """
    
    Action_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-abortcriteria.html#cfn-iot-jobtemplate-abortcriteria-action""", alias="Action")
    FailureType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-abortcriteria.html#cfn-iot-jobtemplate-abortcriteria-failuretype""", alias="FailureType")
    ThresholdPercentage_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-abortcriteria.html#cfn-iot-jobtemplate-abortcriteria-thresholdpercentage""", alias="ThresholdPercentage")
    MinNumberOfExecutedThings_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-abortcriteria.html#cfn-iot-jobtemplate-abortcriteria-minnumberofexecutedthings""", alias="MinNumberOfExecutedThings")
    


    @property
    def tropo_type(self) -> troposphere.iot.AbortCriteria:
        from troposphere.iot import AbortCriteria as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ExponentialRolloutRate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-exponentialrolloutrate.html
    Properties:
        - Name: RateIncreaseCriteria
        - Name: BaseRatePerMinute
        - Name: IncrementFactor
    
    """
    
    RateIncreaseCriteria_: 'RateIncreaseCriteria' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-exponentialrolloutrate.html#cfn-iot-jobtemplate-exponentialrolloutrate-rateincreasecriteria""", alias="RateIncreaseCriteria")
    BaseRatePerMinute_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-exponentialrolloutrate.html#cfn-iot-jobtemplate-exponentialrolloutrate-baserateperminute""", alias="BaseRatePerMinute")
    IncrementFactor_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-exponentialrolloutrate.html#cfn-iot-jobtemplate-exponentialrolloutrate-incrementfactor""", alias="IncrementFactor")
    


    @property
    def tropo_type(self) -> troposphere.iot.ExponentialRolloutRate:
        from troposphere.iot import ExponentialRolloutRate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class JobExecutionsRetryConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-jobexecutionsretryconfig.html
    Properties:
        - Name: RetryCriteriaList
    
    """
    
    RetryCriteriaList_: Optional[List['RetryCriteria']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-jobexecutionsretryconfig.html#cfn-iot-jobtemplate-jobexecutionsretryconfig-retrycriterialist""", alias="RetryCriteriaList")
    


    @property
    def tropo_type(self) -> troposphere.iot.JobExecutionsRetryConfig:
        from troposphere.iot import JobExecutionsRetryConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class JobExecutionsRolloutConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-jobexecutionsrolloutconfig.html
    Properties:
        - Name: MaximumPerMinute
        - Name: ExponentialRolloutRate
    
    """
    
    MaximumPerMinute_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-jobexecutionsrolloutconfig.html#cfn-iot-jobtemplate-jobexecutionsrolloutconfig-maximumperminute""", alias="MaximumPerMinute")
    ExponentialRolloutRate_: Optional['ExponentialRolloutRate'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-jobexecutionsrolloutconfig.html#cfn-iot-jobtemplate-jobexecutionsrolloutconfig-exponentialrolloutrate""", alias="ExponentialRolloutRate")
    


    @property
    def tropo_type(self) -> troposphere.iot.JobExecutionsRolloutConfig:
        from troposphere.iot import JobExecutionsRolloutConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MaintenanceWindow(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-maintenancewindow.html
    Properties:
        - Name: DurationInMinutes
        - Name: StartTime
    
    """
    
    DurationInMinutes_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-maintenancewindow.html#cfn-iot-jobtemplate-maintenancewindow-durationinminutes""", alias="DurationInMinutes")
    StartTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-maintenancewindow.html#cfn-iot-jobtemplate-maintenancewindow-starttime""", alias="StartTime")
    


    @property
    def tropo_type(self) -> troposphere.iot.MaintenanceWindow:
        from troposphere.iot import MaintenanceWindow as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PresignedUrlConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-presignedurlconfig.html
    Properties:
        - Name: ExpiresInSec
        - Name: RoleArn
    
    """
    
    ExpiresInSec_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-presignedurlconfig.html#cfn-iot-jobtemplate-presignedurlconfig-expiresinsec""", alias="ExpiresInSec")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-presignedurlconfig.html#cfn-iot-jobtemplate-presignedurlconfig-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.iot.PresignedUrlConfig:
        from troposphere.iot import PresignedUrlConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RateIncreaseCriteria(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-rateincreasecriteria.html
    Properties:
        - Name: NumberOfSucceededThings
        - Name: NumberOfNotifiedThings
    
    """
    
    NumberOfSucceededThings_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-rateincreasecriteria.html#cfn-iot-jobtemplate-rateincreasecriteria-numberofsucceededthings""", alias="NumberOfSucceededThings")
    NumberOfNotifiedThings_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-rateincreasecriteria.html#cfn-iot-jobtemplate-rateincreasecriteria-numberofnotifiedthings""", alias="NumberOfNotifiedThings")
    


    @property
    def tropo_type(self) -> troposphere.iot.RateIncreaseCriteria:
        from troposphere.iot import RateIncreaseCriteria as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RetryCriteria(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-retrycriteria.html
    Properties:
        - Name: FailureType
        - Name: NumberOfRetries
    
    """
    
    FailureType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-retrycriteria.html#cfn-iot-jobtemplate-retrycriteria-failuretype""", alias="FailureType")
    NumberOfRetries_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-retrycriteria.html#cfn-iot-jobtemplate-retrycriteria-numberofretries""", alias="NumberOfRetries")
    


    @property
    def tropo_type(self) -> troposphere.iot.RetryCriteria:
        from troposphere.iot import RetryCriteria as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TimeoutConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-timeoutconfig.html
    Properties:
        - Name: InProgressTimeoutInMinutes
    
    """
    
    InProgressTimeoutInMinutes_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-timeoutconfig.html#cfn-iot-jobtemplate-timeoutconfig-inprogresstimeoutinminutes""", alias="InProgressTimeoutInMinutes")
    


    @property
    def tropo_type(self) -> troposphere.iot.TimeoutConfig:
        from troposphere.iot import TimeoutConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ActionParams(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-actionparams.html
    Properties:
        - Name: UpdateDeviceCertificateParams
        - Name: AddThingsToThingGroupParams
        - Name: PublishFindingToSnsParams
        - Name: EnableIoTLoggingParams
        - Name: ReplaceDefaultPolicyVersionParams
        - Name: UpdateCACertificateParams
    
    """
    
    UpdateDeviceCertificateParams_: Optional['UpdateDeviceCertificateParams'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-actionparams.html#cfn-iot-mitigationaction-actionparams-updatedevicecertificateparams""", alias="UpdateDeviceCertificateParams")
    AddThingsToThingGroupParams_: Optional['AddThingsToThingGroupParams'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-actionparams.html#cfn-iot-mitigationaction-actionparams-addthingstothinggroupparams""", alias="AddThingsToThingGroupParams")
    PublishFindingToSnsParams_: Optional['PublishFindingToSnsParams'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-actionparams.html#cfn-iot-mitigationaction-actionparams-publishfindingtosnsparams""", alias="PublishFindingToSnsParams")
    EnableIoTLoggingParams_: Optional['EnableIoTLoggingParams'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-actionparams.html#cfn-iot-mitigationaction-actionparams-enableiotloggingparams""", alias="EnableIoTLoggingParams")
    ReplaceDefaultPolicyVersionParams_: Optional['ReplaceDefaultPolicyVersionParams'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-actionparams.html#cfn-iot-mitigationaction-actionparams-replacedefaultpolicyversionparams""", alias="ReplaceDefaultPolicyVersionParams")
    UpdateCACertificateParams_: Optional['UpdateCACertificateParams'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-actionparams.html#cfn-iot-mitigationaction-actionparams-updatecacertificateparams""", alias="UpdateCACertificateParams")
    


    @property
    def tropo_type(self) -> troposphere.iot.ActionParams:
        from troposphere.iot import ActionParams as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AddThingsToThingGroupParams(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-addthingstothinggroupparams.html
    Properties:
        - Name: OverrideDynamicGroups
        - Name: ThingGroupNames
    
    """
    
    OverrideDynamicGroups_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-addthingstothinggroupparams.html#cfn-iot-mitigationaction-addthingstothinggroupparams-overridedynamicgroups""", alias="OverrideDynamicGroups")
    ThingGroupNames_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-addthingstothinggroupparams.html#cfn-iot-mitigationaction-addthingstothinggroupparams-thinggroupnames""", alias="ThingGroupNames")
    


    @property
    def tropo_type(self) -> troposphere.iot.AddThingsToThingGroupParams:
        from troposphere.iot import AddThingsToThingGroupParams as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EnableIoTLoggingParams(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-enableiotloggingparams.html
    Properties:
        - Name: RoleArnForLogging
        - Name: LogLevel
    
    """
    
    RoleArnForLogging_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-enableiotloggingparams.html#cfn-iot-mitigationaction-enableiotloggingparams-rolearnforlogging""", alias="RoleArnForLogging")
    LogLevel_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-enableiotloggingparams.html#cfn-iot-mitigationaction-enableiotloggingparams-loglevel""", alias="LogLevel")
    


    @property
    def tropo_type(self) -> troposphere.iot.EnableIoTLoggingParams:
        from troposphere.iot import EnableIoTLoggingParams as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PublishFindingToSnsParams(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-publishfindingtosnsparams.html
    Properties:
        - Name: TopicArn
    
    """
    
    TopicArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-publishfindingtosnsparams.html#cfn-iot-mitigationaction-publishfindingtosnsparams-topicarn""", alias="TopicArn")
    


    @property
    def tropo_type(self) -> troposphere.iot.PublishFindingToSnsParams:
        from troposphere.iot import PublishFindingToSnsParams as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReplaceDefaultPolicyVersionParams(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-replacedefaultpolicyversionparams.html
    Properties:
        - Name: TemplateName
    
    """
    
    TemplateName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-replacedefaultpolicyversionparams.html#cfn-iot-mitigationaction-replacedefaultpolicyversionparams-templatename""", alias="TemplateName")
    


    @property
    def tropo_type(self) -> troposphere.iot.ReplaceDefaultPolicyVersionParams:
        from troposphere.iot import ReplaceDefaultPolicyVersionParams as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class UpdateCACertificateParams(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-updatecacertificateparams.html
    Properties:
        - Name: Action
    
    """
    
    Action_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-updatecacertificateparams.html#cfn-iot-mitigationaction-updatecacertificateparams-action""", alias="Action")
    


    @property
    def tropo_type(self) -> troposphere.iot.UpdateCACertificateParams:
        from troposphere.iot import UpdateCACertificateParams as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class UpdateDeviceCertificateParams(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-updatedevicecertificateparams.html
    Properties:
        - Name: Action
    
    """
    
    Action_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-updatedevicecertificateparams.html#cfn-iot-mitigationaction-updatedevicecertificateparams-action""", alias="Action")
    


    @property
    def tropo_type(self) -> troposphere.iot.UpdateDeviceCertificateParams:
        from troposphere.iot import UpdateDeviceCertificateParams as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProvisioningHook(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-provisioningtemplate-provisioninghook.html
    Properties:
        - Name: TargetArn
        - Name: PayloadVersion
    
    """
    
    TargetArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-provisioningtemplate-provisioninghook.html#cfn-iot-provisioningtemplate-provisioninghook-targetarn""", alias="TargetArn")
    PayloadVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-provisioningtemplate-provisioninghook.html#cfn-iot-provisioningtemplate-provisioninghook-payloadversion""", alias="PayloadVersion")
    


    @property
    def tropo_type(self) -> troposphere.iot.ProvisioningHook:
        from troposphere.iot import ProvisioningHook as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AlertTarget(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-alerttarget.html
    Properties:
        - Name: AlertTargetArn
        - Name: RoleArn
    
    """
    
    AlertTargetArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-alerttarget.html#cfn-iot-securityprofile-alerttarget-alerttargetarn""", alias="AlertTargetArn")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-alerttarget.html#cfn-iot-securityprofile-alerttarget-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.iot.AlertTarget:
        from troposphere.iot import AlertTarget as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Behavior(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behavior.html
    Properties:
        - Name: SuppressAlerts
        - Name: Metric
        - Name: Criteria
        - Name: MetricDimension
        - Name: Name
    
    """
    
    SuppressAlerts_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behavior.html#cfn-iot-securityprofile-behavior-suppressalerts""", alias="SuppressAlerts")
    Metric_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behavior.html#cfn-iot-securityprofile-behavior-metric""", alias="Metric")
    Criteria_: Optional['BehaviorCriteria'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behavior.html#cfn-iot-securityprofile-behavior-criteria""", alias="Criteria")
    MetricDimension_: Optional['MetricDimension'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behavior.html#cfn-iot-securityprofile-behavior-metricdimension""", alias="MetricDimension")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behavior.html#cfn-iot-securityprofile-behavior-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.iot.Behavior:
        from troposphere.iot import Behavior as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BehaviorCriteria(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behaviorcriteria.html
    Properties:
        - Name: ComparisonOperator
        - Name: MlDetectionConfig
        - Name: Value
        - Name: StatisticalThreshold
        - Name: DurationSeconds
        - Name: ConsecutiveDatapointsToAlarm
        - Name: ConsecutiveDatapointsToClear
    
    """
    
    ComparisonOperator_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behaviorcriteria.html#cfn-iot-securityprofile-behaviorcriteria-comparisonoperator""", alias="ComparisonOperator")
    MlDetectionConfig_: Optional['MachineLearningDetectionConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behaviorcriteria.html#cfn-iot-securityprofile-behaviorcriteria-mldetectionconfig""", alias="MlDetectionConfig")
    Value_: Optional['MetricValue'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behaviorcriteria.html#cfn-iot-securityprofile-behaviorcriteria-value""", alias="Value")
    StatisticalThreshold_: Optional['StatisticalThreshold'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behaviorcriteria.html#cfn-iot-securityprofile-behaviorcriteria-statisticalthreshold""", alias="StatisticalThreshold")
    DurationSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behaviorcriteria.html#cfn-iot-securityprofile-behaviorcriteria-durationseconds""", alias="DurationSeconds")
    ConsecutiveDatapointsToAlarm_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behaviorcriteria.html#cfn-iot-securityprofile-behaviorcriteria-consecutivedatapointstoalarm""", alias="ConsecutiveDatapointsToAlarm")
    ConsecutiveDatapointsToClear_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behaviorcriteria.html#cfn-iot-securityprofile-behaviorcriteria-consecutivedatapointstoclear""", alias="ConsecutiveDatapointsToClear")
    


    @property
    def tropo_type(self) -> troposphere.iot.BehaviorCriteria:
        from troposphere.iot import BehaviorCriteria as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MachineLearningDetectionConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-machinelearningdetectionconfig.html
    Properties:
        - Name: ConfidenceLevel
    
    """
    
    ConfidenceLevel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-machinelearningdetectionconfig.html#cfn-iot-securityprofile-machinelearningdetectionconfig-confidencelevel""", alias="ConfidenceLevel")
    


    @property
    def tropo_type(self) -> troposphere.iot.MachineLearningDetectionConfig:
        from troposphere.iot import MachineLearningDetectionConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetricDimension(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metricdimension.html
    Properties:
        - Name: Operator
        - Name: DimensionName
    
    """
    
    Operator_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metricdimension.html#cfn-iot-securityprofile-metricdimension-operator""", alias="Operator")
    DimensionName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metricdimension.html#cfn-iot-securityprofile-metricdimension-dimensionname""", alias="DimensionName")
    


    @property
    def tropo_type(self) -> troposphere.iot.MetricDimension:
        from troposphere.iot import MetricDimension as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetricToRetain(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metrictoretain.html
    Properties:
        - Name: Metric
        - Name: MetricDimension
    
    """
    
    Metric_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metrictoretain.html#cfn-iot-securityprofile-metrictoretain-metric""", alias="Metric")
    MetricDimension_: Optional['MetricDimension'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metrictoretain.html#cfn-iot-securityprofile-metrictoretain-metricdimension""", alias="MetricDimension")
    


    @property
    def tropo_type(self) -> troposphere.iot.MetricToRetain:
        from troposphere.iot import MetricToRetain as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetricValue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metricvalue.html
    Properties:
        - Name: Numbers
        - Name: Number
        - Name: Ports
        - Name: Count
        - Name: Strings
        - Name: Cidrs
    
    """
    
    Numbers_: Optional[List[float]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metricvalue.html#cfn-iot-securityprofile-metricvalue-numbers""", alias="Numbers")
    Number_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metricvalue.html#cfn-iot-securityprofile-metricvalue-number""", alias="Number")
    Ports_: Optional[List[int]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metricvalue.html#cfn-iot-securityprofile-metricvalue-ports""", alias="Ports")
    Count_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metricvalue.html#cfn-iot-securityprofile-metricvalue-count""", alias="Count")
    Strings_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metricvalue.html#cfn-iot-securityprofile-metricvalue-strings""", alias="Strings")
    Cidrs_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metricvalue.html#cfn-iot-securityprofile-metricvalue-cidrs""", alias="Cidrs")
    


    @property
    def tropo_type(self) -> troposphere.iot.MetricValue:
        from troposphere.iot import MetricValue as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StatisticalThreshold(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-statisticalthreshold.html
    Properties:
        - Name: Statistic
    
    """
    
    Statistic_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-statisticalthreshold.html#cfn-iot-securityprofile-statisticalthreshold-statistic""", alias="Statistic")
    


    @property
    def tropo_type(self) -> troposphere.iot.StatisticalThreshold:
        from troposphere.iot import StatisticalThreshold as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AttributePayload(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-thing-attributepayload.html
    Properties:
        - Name: Attributes
    
    """
    
    Attributes_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-thing-attributepayload.html#cfn-iot-thing-attributepayload-attributes""", alias="Attributes")
    


    @property
    def tropo_type(self) -> troposphere.iot.AttributePayload:
        from troposphere.iot import AttributePayload as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AttributePayload(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-thinggroup-attributepayload.html
    Properties:
        - Name: Attributes
    
    """
    
    Attributes_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-thinggroup-attributepayload.html#cfn-iot-thinggroup-attributepayload-attributes""", alias="Attributes")
    


    @property
    def tropo_type(self) -> troposphere.iot.AttributePayload:
        from troposphere.iot import AttributePayload as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ThingGroupProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-thinggroup-thinggroupproperties.html
    Properties:
        - Name: AttributePayload
        - Name: ThingGroupDescription
    
    """
    
    AttributePayload_: Optional['AttributePayload'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-thinggroup-thinggroupproperties.html#cfn-iot-thinggroup-thinggroupproperties-attributepayload""", alias="AttributePayload")
    ThingGroupDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-thinggroup-thinggroupproperties.html#cfn-iot-thinggroup-thinggroupproperties-thinggroupdescription""", alias="ThingGroupDescription")
    


    @property
    def tropo_type(self) -> troposphere.iot.ThingGroupProperties:
        from troposphere.iot import ThingGroupProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ThingTypeProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-thingtype-thingtypeproperties.html
    Properties:
        - Name: ThingTypeDescription
        - Name: SearchableAttributes
    
    """
    
    ThingTypeDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-thingtype-thingtypeproperties.html#cfn-iot-thingtype-thingtypeproperties-thingtypedescription""", alias="ThingTypeDescription")
    SearchableAttributes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-thingtype-thingtypeproperties.html#cfn-iot-thingtype-thingtypeproperties-searchableattributes""", alias="SearchableAttributes")
    


    @property
    def tropo_type(self) -> troposphere.iot.ThingTypeProperties:
        from troposphere.iot import ThingTypeProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Action(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html
    Properties:
        - Name: S3
        - Name: CloudwatchAlarm
        - Name: IotEvents
        - Name: Firehose
        - Name: Republish
        - Name: Kafka
        - Name: StepFunctions
        - Name: DynamoDB
        - Name: Http
        - Name: OpenSearch
        - Name: DynamoDBv2
        - Name: CloudwatchMetric
        - Name: IotSiteWise
        - Name: Elasticsearch
        - Name: Sqs
        - Name: Kinesis
        - Name: CloudwatchLogs
        - Name: Timestream
        - Name: IotAnalytics
        - Name: Sns
        - Name: Lambda
        - Name: Location
    
    """
    
    S3_: Optional['S3Action'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-s3""", alias="S3")
    CloudwatchAlarm_: Optional['CloudwatchAlarmAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-cloudwatchalarm""", alias="CloudwatchAlarm")
    IotEvents_: Optional['IotEventsAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-iotevents""", alias="IotEvents")
    Firehose_: Optional['FirehoseAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-firehose""", alias="Firehose")
    Republish_: Optional['RepublishAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-republish""", alias="Republish")
    Kafka_: Optional['KafkaAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-kafka""", alias="Kafka")
    StepFunctions_: Optional['StepFunctionsAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-stepfunctions""", alias="StepFunctions")
    DynamoDB_: Optional['DynamoDBAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-dynamodb""", alias="DynamoDB")
    Http_: Optional['HttpAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-http""", alias="Http")
    OpenSearch_: Optional['OpenSearchAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-opensearch""", alias="OpenSearch")
    DynamoDBv2_: Optional['DynamoDBv2Action'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-dynamodbv2""", alias="DynamoDBv2")
    CloudwatchMetric_: Optional['CloudwatchMetricAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-cloudwatchmetric""", alias="CloudwatchMetric")
    IotSiteWise_: Optional['IotSiteWiseAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-iotsitewise""", alias="IotSiteWise")
    Elasticsearch_: Optional['ElasticsearchAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-elasticsearch""", alias="Elasticsearch")
    Sqs_: Optional['SqsAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-sqs""", alias="Sqs")
    Kinesis_: Optional['KinesisAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-kinesis""", alias="Kinesis")
    CloudwatchLogs_: Optional['CloudwatchLogsAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-cloudwatchlogs""", alias="CloudwatchLogs")
    Timestream_: Optional['TimestreamAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-timestream""", alias="Timestream")
    IotAnalytics_: Optional['IotAnalyticsAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-iotanalytics""", alias="IotAnalytics")
    Sns_: Optional['SnsAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-sns""", alias="Sns")
    Lambda_: Optional['LambdaAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-lambda""", alias="Lambda")
    Location_: Optional['LocationAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-location""", alias="Location")
    


    @property
    def tropo_type(self) -> troposphere.iot.Action:
        from troposphere.iot import Action as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AssetPropertyTimestamp(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertytimestamp.html
    Properties:
        - Name: TimeInSeconds
        - Name: OffsetInNanos
    
    """
    
    TimeInSeconds_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertytimestamp.html#cfn-iot-topicrule-assetpropertytimestamp-timeinseconds""", alias="TimeInSeconds")
    OffsetInNanos_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertytimestamp.html#cfn-iot-topicrule-assetpropertytimestamp-offsetinnanos""", alias="OffsetInNanos")
    


    @property
    def tropo_type(self) -> troposphere.iot.AssetPropertyTimestamp:
        from troposphere.iot import AssetPropertyTimestamp as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AssetPropertyValue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertyvalue.html
    Properties:
        - Name: Quality
        - Name: Value
        - Name: Timestamp
    
    """
    
    Quality_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertyvalue.html#cfn-iot-topicrule-assetpropertyvalue-quality""", alias="Quality")
    Value_: 'AssetPropertyVariant' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertyvalue.html#cfn-iot-topicrule-assetpropertyvalue-value""", alias="Value")
    Timestamp_: 'AssetPropertyTimestamp' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertyvalue.html#cfn-iot-topicrule-assetpropertyvalue-timestamp""", alias="Timestamp")
    


    @property
    def tropo_type(self) -> troposphere.iot.AssetPropertyValue:
        from troposphere.iot import AssetPropertyValue as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AssetPropertyVariant(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertyvariant.html
    Properties:
        - Name: DoubleValue
        - Name: BooleanValue
        - Name: IntegerValue
        - Name: StringValue
    
    """
    
    DoubleValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertyvariant.html#cfn-iot-topicrule-assetpropertyvariant-doublevalue""", alias="DoubleValue")
    BooleanValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertyvariant.html#cfn-iot-topicrule-assetpropertyvariant-booleanvalue""", alias="BooleanValue")
    IntegerValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertyvariant.html#cfn-iot-topicrule-assetpropertyvariant-integervalue""", alias="IntegerValue")
    StringValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertyvariant.html#cfn-iot-topicrule-assetpropertyvariant-stringvalue""", alias="StringValue")
    


    @property
    def tropo_type(self) -> troposphere.iot.AssetPropertyVariant:
        from troposphere.iot import AssetPropertyVariant as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CloudwatchAlarmAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchalarmaction.html
    Properties:
        - Name: AlarmName
        - Name: StateReason
        - Name: StateValue
        - Name: RoleArn
    
    """
    
    AlarmName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchalarmaction.html#cfn-iot-topicrule-cloudwatchalarmaction-alarmname""", alias="AlarmName")
    StateReason_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchalarmaction.html#cfn-iot-topicrule-cloudwatchalarmaction-statereason""", alias="StateReason")
    StateValue_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchalarmaction.html#cfn-iot-topicrule-cloudwatchalarmaction-statevalue""", alias="StateValue")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchalarmaction.html#cfn-iot-topicrule-cloudwatchalarmaction-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.iot.CloudwatchAlarmAction:
        from troposphere.iot import CloudwatchAlarmAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CloudwatchLogsAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchlogsaction.html
    Properties:
        - Name: BatchMode
        - Name: LogGroupName
        - Name: RoleArn
    
    """
    
    BatchMode_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchlogsaction.html#cfn-iot-topicrule-cloudwatchlogsaction-batchmode""", alias="BatchMode")
    LogGroupName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchlogsaction.html#cfn-iot-topicrule-cloudwatchlogsaction-loggroupname""", alias="LogGroupName")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchlogsaction.html#cfn-iot-topicrule-cloudwatchlogsaction-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.iot.CloudwatchLogsAction:
        from troposphere.iot import CloudwatchLogsAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CloudwatchMetricAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchmetricaction.html
    Properties:
        - Name: MetricName
        - Name: MetricValue
        - Name: MetricNamespace
        - Name: MetricUnit
        - Name: RoleArn
        - Name: MetricTimestamp
    
    """
    
    MetricName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchmetricaction.html#cfn-iot-topicrule-cloudwatchmetricaction-metricname""", alias="MetricName")
    MetricValue_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchmetricaction.html#cfn-iot-topicrule-cloudwatchmetricaction-metricvalue""", alias="MetricValue")
    MetricNamespace_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchmetricaction.html#cfn-iot-topicrule-cloudwatchmetricaction-metricnamespace""", alias="MetricNamespace")
    MetricUnit_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchmetricaction.html#cfn-iot-topicrule-cloudwatchmetricaction-metricunit""", alias="MetricUnit")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchmetricaction.html#cfn-iot-topicrule-cloudwatchmetricaction-rolearn""", alias="RoleArn")
    MetricTimestamp_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchmetricaction.html#cfn-iot-topicrule-cloudwatchmetricaction-metrictimestamp""", alias="MetricTimestamp")
    


    @property
    def tropo_type(self) -> troposphere.iot.CloudwatchMetricAction:
        from troposphere.iot import CloudwatchMetricAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DynamoDBAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbaction.html
    Properties:
        - Name: TableName
        - Name: PayloadField
        - Name: RangeKeyField
        - Name: HashKeyField
        - Name: RangeKeyValue
        - Name: RangeKeyType
        - Name: HashKeyType
        - Name: HashKeyValue
        - Name: RoleArn
    
    """
    
    TableName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbaction.html#cfn-iot-topicrule-dynamodbaction-tablename""", alias="TableName")
    PayloadField_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbaction.html#cfn-iot-topicrule-dynamodbaction-payloadfield""", alias="PayloadField")
    RangeKeyField_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbaction.html#cfn-iot-topicrule-dynamodbaction-rangekeyfield""", alias="RangeKeyField")
    HashKeyField_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbaction.html#cfn-iot-topicrule-dynamodbaction-hashkeyfield""", alias="HashKeyField")
    RangeKeyValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbaction.html#cfn-iot-topicrule-dynamodbaction-rangekeyvalue""", alias="RangeKeyValue")
    RangeKeyType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbaction.html#cfn-iot-topicrule-dynamodbaction-rangekeytype""", alias="RangeKeyType")
    HashKeyType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbaction.html#cfn-iot-topicrule-dynamodbaction-hashkeytype""", alias="HashKeyType")
    HashKeyValue_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbaction.html#cfn-iot-topicrule-dynamodbaction-hashkeyvalue""", alias="HashKeyValue")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbaction.html#cfn-iot-topicrule-dynamodbaction-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.iot.DynamoDBAction:
        from troposphere.iot import DynamoDBAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DynamoDBv2Action(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbv2action.html
    Properties:
        - Name: PutItem
        - Name: RoleArn
    
    """
    
    PutItem_: Optional['PutItemInput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbv2action.html#cfn-iot-topicrule-dynamodbv2action-putitem""", alias="PutItem")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbv2action.html#cfn-iot-topicrule-dynamodbv2action-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.iot.DynamoDBv2Action:
        from troposphere.iot import DynamoDBv2Action as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ElasticsearchAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-elasticsearchaction.html
    Properties:
        - Name: Type
        - Name: Endpoint
        - Name: Index
        - Name: Id
        - Name: RoleArn
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-elasticsearchaction.html#cfn-iot-topicrule-elasticsearchaction-type""", alias="Type")
    Endpoint_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-elasticsearchaction.html#cfn-iot-topicrule-elasticsearchaction-endpoint""", alias="Endpoint")
    Index_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-elasticsearchaction.html#cfn-iot-topicrule-elasticsearchaction-index""", alias="Index")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-elasticsearchaction.html#cfn-iot-topicrule-elasticsearchaction-id""", alias="Id")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-elasticsearchaction.html#cfn-iot-topicrule-elasticsearchaction-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.iot.ElasticsearchAction:
        from troposphere.iot import ElasticsearchAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FirehoseAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-firehoseaction.html
    Properties:
        - Name: DeliveryStreamName
        - Name: BatchMode
        - Name: RoleArn
        - Name: Separator
    
    """
    
    DeliveryStreamName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-firehoseaction.html#cfn-iot-topicrule-firehoseaction-deliverystreamname""", alias="DeliveryStreamName")
    BatchMode_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-firehoseaction.html#cfn-iot-topicrule-firehoseaction-batchmode""", alias="BatchMode")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-firehoseaction.html#cfn-iot-topicrule-firehoseaction-rolearn""", alias="RoleArn")
    Separator_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-firehoseaction.html#cfn-iot-topicrule-firehoseaction-separator""", alias="Separator")
    


    @property
    def tropo_type(self) -> troposphere.iot.FirehoseAction:
        from troposphere.iot import FirehoseAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpaction.html
    Properties:
        - Name: Headers
        - Name: Auth
        - Name: ConfirmationUrl
        - Name: Url
    
    """
    
    Headers_: Optional[List['HttpActionHeader']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpaction.html#cfn-iot-topicrule-httpaction-headers""", alias="Headers")
    Auth_: Optional['HttpAuthorization'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpaction.html#cfn-iot-topicrule-httpaction-auth""", alias="Auth")
    ConfirmationUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpaction.html#cfn-iot-topicrule-httpaction-confirmationurl""", alias="ConfirmationUrl")
    Url_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpaction.html#cfn-iot-topicrule-httpaction-url""", alias="Url")
    


    @property
    def tropo_type(self) -> troposphere.iot.HttpAction:
        from troposphere.iot import HttpAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpActionHeader(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpactionheader.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpactionheader.html#cfn-iot-topicrule-httpactionheader-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpactionheader.html#cfn-iot-topicrule-httpactionheader-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.iot.HttpActionHeader:
        from troposphere.iot import HttpActionHeader as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpAuthorization(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpauthorization.html
    Properties:
        - Name: Sigv4
    
    """
    
    Sigv4_: Optional['SigV4Authorization'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpauthorization.html#cfn-iot-topicrule-httpauthorization-sigv4""", alias="Sigv4")
    


    @property
    def tropo_type(self) -> troposphere.iot.HttpAuthorization:
        from troposphere.iot import HttpAuthorization as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IotAnalyticsAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-iotanalyticsaction.html
    Properties:
        - Name: ChannelName
        - Name: BatchMode
        - Name: RoleArn
    
    """
    
    ChannelName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-iotanalyticsaction.html#cfn-iot-topicrule-iotanalyticsaction-channelname""", alias="ChannelName")
    BatchMode_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-iotanalyticsaction.html#cfn-iot-topicrule-iotanalyticsaction-batchmode""", alias="BatchMode")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-iotanalyticsaction.html#cfn-iot-topicrule-iotanalyticsaction-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.iot.IotAnalyticsAction:
        from troposphere.iot import IotAnalyticsAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IotEventsAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-ioteventsaction.html
    Properties:
        - Name: InputName
        - Name: BatchMode
        - Name: RoleArn
        - Name: MessageId
    
    """
    
    InputName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-ioteventsaction.html#cfn-iot-topicrule-ioteventsaction-inputname""", alias="InputName")
    BatchMode_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-ioteventsaction.html#cfn-iot-topicrule-ioteventsaction-batchmode""", alias="BatchMode")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-ioteventsaction.html#cfn-iot-topicrule-ioteventsaction-rolearn""", alias="RoleArn")
    MessageId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-ioteventsaction.html#cfn-iot-topicrule-ioteventsaction-messageid""", alias="MessageId")
    


    @property
    def tropo_type(self) -> troposphere.iot.IotEventsAction:
        from troposphere.iot import IotEventsAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IotSiteWiseAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-iotsitewiseaction.html
    Properties:
        - Name: PutAssetPropertyValueEntries
        - Name: RoleArn
    
    """
    
    PutAssetPropertyValueEntries_: List['PutAssetPropertyValueEntry'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-iotsitewiseaction.html#cfn-iot-topicrule-iotsitewiseaction-putassetpropertyvalueentries""", alias="PutAssetPropertyValueEntries")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-iotsitewiseaction.html#cfn-iot-topicrule-iotsitewiseaction-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.iot.IotSiteWiseAction:
        from troposphere.iot import IotSiteWiseAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KafkaAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kafkaaction.html
    Properties:
        - Name: Partition
        - Name: ClientProperties
        - Name: Headers
        - Name: Topic
        - Name: DestinationArn
        - Name: Key
    
    """
    
    Partition_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kafkaaction.html#cfn-iot-topicrule-kafkaaction-partition""", alias="Partition")
    ClientProperties_: Dict[str, str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kafkaaction.html#cfn-iot-topicrule-kafkaaction-clientproperties""", alias="ClientProperties")
    Headers_: Optional[List['KafkaActionHeader']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kafkaaction.html#cfn-iot-topicrule-kafkaaction-headers""", alias="Headers")
    Topic_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kafkaaction.html#cfn-iot-topicrule-kafkaaction-topic""", alias="Topic")
    DestinationArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kafkaaction.html#cfn-iot-topicrule-kafkaaction-destinationarn""", alias="DestinationArn")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kafkaaction.html#cfn-iot-topicrule-kafkaaction-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.iot.KafkaAction:
        from troposphere.iot import KafkaAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KafkaActionHeader(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kafkaactionheader.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kafkaactionheader.html#cfn-iot-topicrule-kafkaactionheader-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kafkaactionheader.html#cfn-iot-topicrule-kafkaactionheader-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.iot.KafkaActionHeader:
        from troposphere.iot import KafkaActionHeader as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KinesisAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kinesisaction.html
    Properties:
        - Name: StreamName
        - Name: PartitionKey
        - Name: RoleArn
    
    """
    
    StreamName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kinesisaction.html#cfn-iot-topicrule-kinesisaction-streamname""", alias="StreamName")
    PartitionKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kinesisaction.html#cfn-iot-topicrule-kinesisaction-partitionkey""", alias="PartitionKey")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kinesisaction.html#cfn-iot-topicrule-kinesisaction-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.iot.KinesisAction:
        from troposphere.iot import KinesisAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LambdaAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-lambdaaction.html
    Properties:
        - Name: FunctionArn
    
    """
    
    FunctionArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-lambdaaction.html#cfn-iot-topicrule-lambdaaction-functionarn""", alias="FunctionArn")
    


    @property
    def tropo_type(self) -> troposphere.iot.LambdaAction:
        from troposphere.iot import LambdaAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LocationAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-locationaction.html
    Properties:
        - Name: TrackerName
        - Name: DeviceId
        - Name: Latitude
        - Name: Longitude
        - Name: Timestamp
        - Name: RoleArn
    
    """
    
    TrackerName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-locationaction.html#cfn-iot-topicrule-locationaction-trackername""", alias="TrackerName")
    DeviceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-locationaction.html#cfn-iot-topicrule-locationaction-deviceid""", alias="DeviceId")
    Latitude_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-locationaction.html#cfn-iot-topicrule-locationaction-latitude""", alias="Latitude")
    Longitude_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-locationaction.html#cfn-iot-topicrule-locationaction-longitude""", alias="Longitude")
    Timestamp_: Optional[datetime.datetime] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-locationaction.html#cfn-iot-topicrule-locationaction-timestamp""", alias="Timestamp")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-locationaction.html#cfn-iot-topicrule-locationaction-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.iot.LocationAction:
        from troposphere.iot import LocationAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OpenSearchAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-opensearchaction.html
    Properties:
        - Name: Type
        - Name: Endpoint
        - Name: Index
        - Name: Id
        - Name: RoleArn
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-opensearchaction.html#cfn-iot-topicrule-opensearchaction-type""", alias="Type")
    Endpoint_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-opensearchaction.html#cfn-iot-topicrule-opensearchaction-endpoint""", alias="Endpoint")
    Index_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-opensearchaction.html#cfn-iot-topicrule-opensearchaction-index""", alias="Index")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-opensearchaction.html#cfn-iot-topicrule-opensearchaction-id""", alias="Id")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-opensearchaction.html#cfn-iot-topicrule-opensearchaction-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.iot.OpenSearchAction:
        from troposphere.iot import OpenSearchAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PutAssetPropertyValueEntry(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-putassetpropertyvalueentry.html
    Properties:
        - Name: PropertyValues
        - Name: EntryId
        - Name: PropertyAlias
        - Name: AssetId
        - Name: PropertyId
    
    """
    
    PropertyValues_: List['AssetPropertyValue'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-putassetpropertyvalueentry.html#cfn-iot-topicrule-putassetpropertyvalueentry-propertyvalues""", alias="PropertyValues")
    EntryId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-putassetpropertyvalueentry.html#cfn-iot-topicrule-putassetpropertyvalueentry-entryid""", alias="EntryId")
    PropertyAlias_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-putassetpropertyvalueentry.html#cfn-iot-topicrule-putassetpropertyvalueentry-propertyalias""", alias="PropertyAlias")
    AssetId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-putassetpropertyvalueentry.html#cfn-iot-topicrule-putassetpropertyvalueentry-assetid""", alias="AssetId")
    PropertyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-putassetpropertyvalueentry.html#cfn-iot-topicrule-putassetpropertyvalueentry-propertyid""", alias="PropertyId")
    


    @property
    def tropo_type(self) -> troposphere.iot.PutAssetPropertyValueEntry:
        from troposphere.iot import PutAssetPropertyValueEntry as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PutItemInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-putiteminput.html
    Properties:
        - Name: TableName
    
    """
    
    TableName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-putiteminput.html#cfn-iot-topicrule-putiteminput-tablename""", alias="TableName")
    


    @property
    def tropo_type(self) -> troposphere.iot.PutItemInput:
        from troposphere.iot import PutItemInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RepublishAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-republishaction.html
    Properties:
        - Name: Qos
        - Name: Headers
        - Name: Topic
        - Name: RoleArn
    
    """
    
    Qos_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-republishaction.html#cfn-iot-topicrule-republishaction-qos""", alias="Qos")
    Headers_: Optional['RepublishActionHeaders'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-republishaction.html#cfn-iot-topicrule-republishaction-headers""", alias="Headers")
    Topic_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-republishaction.html#cfn-iot-topicrule-republishaction-topic""", alias="Topic")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-republishaction.html#cfn-iot-topicrule-republishaction-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.iot.RepublishAction:
        from troposphere.iot import RepublishAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RepublishActionHeaders(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-republishactionheaders.html
    Properties:
        - Name: CorrelationData
        - Name: UserProperties
        - Name: PayloadFormatIndicator
        - Name: ContentType
        - Name: MessageExpiry
        - Name: ResponseTopic
    
    """
    
    CorrelationData_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-republishactionheaders.html#cfn-iot-topicrule-republishactionheaders-correlationdata""", alias="CorrelationData")
    UserProperties_: Optional[List['UserProperty']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-republishactionheaders.html#cfn-iot-topicrule-republishactionheaders-userproperties""", alias="UserProperties")
    PayloadFormatIndicator_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-republishactionheaders.html#cfn-iot-topicrule-republishactionheaders-payloadformatindicator""", alias="PayloadFormatIndicator")
    ContentType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-republishactionheaders.html#cfn-iot-topicrule-republishactionheaders-contenttype""", alias="ContentType")
    MessageExpiry_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-republishactionheaders.html#cfn-iot-topicrule-republishactionheaders-messageexpiry""", alias="MessageExpiry")
    ResponseTopic_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-republishactionheaders.html#cfn-iot-topicrule-republishactionheaders-responsetopic""", alias="ResponseTopic")
    


    @property
    def tropo_type(self) -> troposphere.iot.RepublishActionHeaders:
        from troposphere.iot import RepublishActionHeaders as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Action(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-s3action.html
    Properties:
        - Name: BucketName
        - Name: CannedAcl
        - Name: Key
        - Name: RoleArn
    
    """
    
    BucketName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-s3action.html#cfn-iot-topicrule-s3action-bucketname""", alias="BucketName")
    CannedAcl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-s3action.html#cfn-iot-topicrule-s3action-cannedacl""", alias="CannedAcl")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-s3action.html#cfn-iot-topicrule-s3action-key""", alias="Key")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-s3action.html#cfn-iot-topicrule-s3action-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.iot.S3Action:
        from troposphere.iot import S3Action as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SigV4Authorization(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-sigv4authorization.html
    Properties:
        - Name: ServiceName
        - Name: SigningRegion
        - Name: RoleArn
    
    """
    
    ServiceName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-sigv4authorization.html#cfn-iot-topicrule-sigv4authorization-servicename""", alias="ServiceName")
    SigningRegion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-sigv4authorization.html#cfn-iot-topicrule-sigv4authorization-signingregion""", alias="SigningRegion")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-sigv4authorization.html#cfn-iot-topicrule-sigv4authorization-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.iot.SigV4Authorization:
        from troposphere.iot import SigV4Authorization as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SnsAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-snsaction.html
    Properties:
        - Name: MessageFormat
        - Name: TargetArn
        - Name: RoleArn
    
    """
    
    MessageFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-snsaction.html#cfn-iot-topicrule-snsaction-messageformat""", alias="MessageFormat")
    TargetArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-snsaction.html#cfn-iot-topicrule-snsaction-targetarn""", alias="TargetArn")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-snsaction.html#cfn-iot-topicrule-snsaction-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.iot.SnsAction:
        from troposphere.iot import SnsAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SqsAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-sqsaction.html
    Properties:
        - Name: UseBase64
        - Name: RoleArn
        - Name: QueueUrl
    
    """
    
    UseBase64_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-sqsaction.html#cfn-iot-topicrule-sqsaction-usebase64""", alias="UseBase64")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-sqsaction.html#cfn-iot-topicrule-sqsaction-rolearn""", alias="RoleArn")
    QueueUrl_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-sqsaction.html#cfn-iot-topicrule-sqsaction-queueurl""", alias="QueueUrl")
    


    @property
    def tropo_type(self) -> troposphere.iot.SqsAction:
        from troposphere.iot import SqsAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StepFunctionsAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-stepfunctionsaction.html
    Properties:
        - Name: ExecutionNamePrefix
        - Name: StateMachineName
        - Name: RoleArn
    
    """
    
    ExecutionNamePrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-stepfunctionsaction.html#cfn-iot-topicrule-stepfunctionsaction-executionnameprefix""", alias="ExecutionNamePrefix")
    StateMachineName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-stepfunctionsaction.html#cfn-iot-topicrule-stepfunctionsaction-statemachinename""", alias="StateMachineName")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-stepfunctionsaction.html#cfn-iot-topicrule-stepfunctionsaction-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.iot.StepFunctionsAction:
        from troposphere.iot import StepFunctionsAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Timestamp(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestamp.html
    Properties:
        - Name: Value
        - Name: Unit
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestamp.html#cfn-iot-topicrule-timestamp-value""", alias="Value")
    Unit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestamp.html#cfn-iot-topicrule-timestamp-unit""", alias="Unit")
    


    @property
    def tropo_type(self) -> troposphere.iot.Timestamp:
        from troposphere.iot import Timestamp as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TimestreamAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamaction.html
    Properties:
        - Name: TableName
        - Name: DatabaseName
        - Name: Dimensions
        - Name: Timestamp
        - Name: RoleArn
    
    """
    
    TableName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamaction.html#cfn-iot-topicrule-timestreamaction-tablename""", alias="TableName")
    DatabaseName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamaction.html#cfn-iot-topicrule-timestreamaction-databasename""", alias="DatabaseName")
    Dimensions_: List['TimestreamDimension'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamaction.html#cfn-iot-topicrule-timestreamaction-dimensions""", alias="Dimensions")
    Timestamp_: Optional['TimestreamTimestamp'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamaction.html#cfn-iot-topicrule-timestreamaction-timestamp""", alias="Timestamp")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamaction.html#cfn-iot-topicrule-timestreamaction-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.iot.TimestreamAction:
        from troposphere.iot import TimestreamAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TimestreamDimension(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamdimension.html
    Properties:
        - Name: Value
        - Name: Name
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamdimension.html#cfn-iot-topicrule-timestreamdimension-value""", alias="Value")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamdimension.html#cfn-iot-topicrule-timestreamdimension-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.iot.TimestreamDimension:
        from troposphere.iot import TimestreamDimension as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TimestreamTimestamp(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamtimestamp.html
    Properties:
        - Name: Value
        - Name: Unit
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamtimestamp.html#cfn-iot-topicrule-timestreamtimestamp-value""", alias="Value")
    Unit_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamtimestamp.html#cfn-iot-topicrule-timestreamtimestamp-unit""", alias="Unit")
    


    @property
    def tropo_type(self) -> troposphere.iot.TimestreamTimestamp:
        from troposphere.iot import TimestreamTimestamp as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TopicRulePayload(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-topicrulepayload.html
    Properties:
        - Name: RuleDisabled
        - Name: ErrorAction
        - Name: Description
        - Name: AwsIotSqlVersion
        - Name: Actions
        - Name: Sql
    
    """
    
    RuleDisabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-topicrulepayload.html#cfn-iot-topicrule-topicrulepayload-ruledisabled""", alias="RuleDisabled")
    ErrorAction_: Optional['Action'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-topicrulepayload.html#cfn-iot-topicrule-topicrulepayload-erroraction""", alias="ErrorAction")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-topicrulepayload.html#cfn-iot-topicrule-topicrulepayload-description""", alias="Description")
    AwsIotSqlVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-topicrulepayload.html#cfn-iot-topicrule-topicrulepayload-awsiotsqlversion""", alias="AwsIotSqlVersion")
    Actions_: List['Action'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-topicrulepayload.html#cfn-iot-topicrule-topicrulepayload-actions""", alias="Actions")
    Sql_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-topicrulepayload.html#cfn-iot-topicrule-topicrulepayload-sql""", alias="Sql")
    


    @property
    def tropo_type(self) -> troposphere.iot.TopicRulePayload:
        from troposphere.iot import TopicRulePayload as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class UserProperty(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-userproperty.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-userproperty.html#cfn-iot-topicrule-userproperty-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-userproperty.html#cfn-iot-topicrule-userproperty-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.iot.UserProperty:
        from troposphere.iot import UserProperty as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpUrlDestinationSummary(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicruledestination-httpurldestinationsummary.html
    Properties:
        - Name: ConfirmationUrl
    
    """
    
    ConfirmationUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicruledestination-httpurldestinationsummary.html#cfn-iot-topicruledestination-httpurldestinationsummary-confirmationurl""", alias="ConfirmationUrl")
    


    @property
    def tropo_type(self) -> troposphere.iot.HttpUrlDestinationSummary:
        from troposphere.iot import HttpUrlDestinationSummary as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcDestinationProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicruledestination-vpcdestinationproperties.html
    Properties:
        - Name: SecurityGroups
        - Name: VpcId
        - Name: SubnetIds
        - Name: RoleArn
    
    """
    
    SecurityGroups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicruledestination-vpcdestinationproperties.html#cfn-iot-topicruledestination-vpcdestinationproperties-securitygroups""", alias="SecurityGroups")
    VpcId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicruledestination-vpcdestinationproperties.html#cfn-iot-topicruledestination-vpcdestinationproperties-vpcid""", alias="VpcId")
    SubnetIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicruledestination-vpcdestinationproperties.html#cfn-iot-topicruledestination-vpcdestinationproperties-subnetids""", alias="SubnetIds")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicruledestination-vpcdestinationproperties.html#cfn-iot-topicruledestination-vpcdestinationproperties-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.iot.VpcDestinationProperties:
        from troposphere.iot import VpcDestinationProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class AccountAuditConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html
    Properties:
        - Name: AccountId
        - Name: AuditCheckConfigurations
        - Name: AuditNotificationTargetConfigurations
        - Name: RoleArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AccountId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html#cfn-iot-accountauditconfiguration-accountid""", alias="AccountId")
    AuditCheckConfigurations_: 'AuditCheckConfigurations' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations""", alias="AuditCheckConfigurations")
    AuditNotificationTargetConfigurations_: Optional['AuditNotificationTargetConfigurations'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html#cfn-iot-accountauditconfiguration-auditnotificationtargetconfigurations""", alias="AuditNotificationTargetConfigurations")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html#cfn-iot-accountauditconfiguration-rolearn""", alias="RoleArn")
    

    @property
    def tropo_type(self) -> troposphere.iot.AccountAuditConfiguration:
        from troposphere.iot import AccountAuditConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iot import AccountAuditConfiguration as TropoT
        return resource_to_troposphere(self, TropoT)


class Authorizer(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html
    Properties:
        - Name: Status
        - Name: TokenKeyName
        - Name: EnableCachingForHttp
        - Name: AuthorizerName
        - Name: TokenSigningPublicKeys
        - Name: SigningDisabled
        - Name: Tags
        - Name: AuthorizerFunctionArn
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-status""", alias="Status")
    TokenKeyName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-tokenkeyname""", alias="TokenKeyName")
    EnableCachingForHttp_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-enablecachingforhttp""", alias="EnableCachingForHttp")
    AuthorizerName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-authorizername""", alias="AuthorizerName")
    TokenSigningPublicKeys_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-tokensigningpublickeys""", alias="TokenSigningPublicKeys")
    SigningDisabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-signingdisabled""", alias="SigningDisabled")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-tags""", alias="Tags")
    AuthorizerFunctionArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-authorizerfunctionarn""", alias="AuthorizerFunctionArn")
    

    @property
    def tropo_type(self) -> troposphere.iot.Authorizer:
        from troposphere.iot import Authorizer as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iot import Authorizer as TropoT
        return resource_to_troposphere(self, TropoT)


class BillingGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-billinggroup.html
    Properties:
        - Name: BillingGroupName
        - Name: BillingGroupProperties
        - Name: Tags
    Attributes:
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    BillingGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-billinggroup.html#cfn-iot-billinggroup-billinggroupname""", alias="BillingGroupName")
    BillingGroupProperties_: Optional['BillingGroupProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-billinggroup.html#cfn-iot-billinggroup-billinggroupproperties""", alias="BillingGroupProperties")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-billinggroup.html#cfn-iot-billinggroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iot.BillingGroup:
        from troposphere.iot import BillingGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iot import BillingGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class CACertificate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html
    Properties:
        - Name: Status
        - Name: CACertificatePem
        - Name: CertificateMode
        - Name: AutoRegistrationStatus
        - Name: RemoveAutoRegistration
        - Name: RegistrationConfig
        - Name: VerificationCertificatePem
        - Name: Tags
    Attributes:
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Status_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-status""", alias="Status")
    CACertificatePem_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-cacertificatepem""", alias="CACertificatePem")
    CertificateMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-certificatemode""", alias="CertificateMode")
    AutoRegistrationStatus_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-autoregistrationstatus""", alias="AutoRegistrationStatus")
    RemoveAutoRegistration_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-removeautoregistration""", alias="RemoveAutoRegistration")
    RegistrationConfig_: Optional['RegistrationConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-registrationconfig""", alias="RegistrationConfig")
    VerificationCertificatePem_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-verificationcertificatepem""", alias="VerificationCertificatePem")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iot.CACertificate:
        from troposphere.iot import CACertificate as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iot import CACertificate as TropoT
        return resource_to_troposphere(self, TropoT)


class Certificate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html
    Properties:
        - Name: Status
        - Name: CACertificatePem
        - Name: CertificateMode
        - Name: CertificateSigningRequest
        - Name: CertificatePem
    Attributes:
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Status_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html#cfn-iot-certificate-status""", alias="Status")
    CACertificatePem_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html#cfn-iot-certificate-cacertificatepem""", alias="CACertificatePem")
    CertificateMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html#cfn-iot-certificate-certificatemode""", alias="CertificateMode")
    CertificateSigningRequest_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html#cfn-iot-certificate-certificatesigningrequest""", alias="CertificateSigningRequest")
    CertificatePem_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html#cfn-iot-certificate-certificatepem""", alias="CertificatePem")
    

    @property
    def tropo_type(self) -> troposphere.iot.Certificate:
        from troposphere.iot import Certificate as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iot import Certificate as TropoT
        return resource_to_troposphere(self, TropoT)


class CustomMetric(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-custommetric.html
    Properties:
        - Name: MetricName
        - Name: MetricType
        - Name: DisplayName
        - Name: Tags
    Attributes:
        - Name: MetricArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MetricName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-custommetric.html#cfn-iot-custommetric-metricname""", alias="MetricName")
    MetricType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-custommetric.html#cfn-iot-custommetric-metrictype""", alias="MetricType")
    DisplayName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-custommetric.html#cfn-iot-custommetric-displayname""", alias="DisplayName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-custommetric.html#cfn-iot-custommetric-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iot.CustomMetric:
        from troposphere.iot import CustomMetric as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iot import CustomMetric as TropoT
        return resource_to_troposphere(self, TropoT)


class Dimension(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-dimension.html
    Properties:
        - Name: Type
        - Name: StringValues
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-dimension.html#cfn-iot-dimension-type""", alias="Type")
    StringValues_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-dimension.html#cfn-iot-dimension-stringvalues""", alias="StringValues")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-dimension.html#cfn-iot-dimension-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-dimension.html#cfn-iot-dimension-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.iot.Dimension:
        from troposphere.iot import Dimension as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iot import Dimension as TropoT
        return resource_to_troposphere(self, TropoT)


class DomainConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html
    Properties:
        - Name: DomainConfigurationName
        - Name: DomainName
        - Name: ServiceType
        - Name: DomainConfigurationStatus
        - Name: ValidationCertificateArn
        - Name: TlsConfig
        - Name: ServerCertificateArns
        - Name: AuthorizerConfig
        - Name: Tags
    Attributes:
        - Name: DomainType
        - Name: ServerCertificates
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DomainConfigurationName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-domainconfigurationname""", alias="DomainConfigurationName")
    DomainName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-domainname""", alias="DomainName")
    ServiceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-servicetype""", alias="ServiceType")
    DomainConfigurationStatus_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-domainconfigurationstatus""", alias="DomainConfigurationStatus")
    ValidationCertificateArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-validationcertificatearn""", alias="ValidationCertificateArn")
    TlsConfig_: Optional['TlsConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-tlsconfig""", alias="TlsConfig")
    ServerCertificateArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-servercertificatearns""", alias="ServerCertificateArns")
    AuthorizerConfig_: Optional['AuthorizerConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-authorizerconfig""", alias="AuthorizerConfig")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iot.DomainConfiguration:
        from troposphere.iot import DomainConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iot import DomainConfiguration as TropoT
        return resource_to_troposphere(self, TropoT)


class FleetMetric(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html
    Properties:
        - Name: IndexName
        - Name: MetricName
        - Name: Description
        - Name: QueryString
        - Name: Period
        - Name: QueryVersion
        - Name: Unit
        - Name: AggregationType
        - Name: AggregationField
        - Name: Tags
    Attributes:
        - Name: MetricArn
        - Name: CreationDate
        - Name: LastModifiedDate
        - Name: Version
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    IndexName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-indexname""", alias="IndexName")
    MetricName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-metricname""", alias="MetricName")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-description""", alias="Description")
    QueryString_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-querystring""", alias="QueryString")
    Period_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-period""", alias="Period")
    QueryVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-queryversion""", alias="QueryVersion")
    Unit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-unit""", alias="Unit")
    AggregationType_: Optional['AggregationType'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-aggregationtype""", alias="AggregationType")
    AggregationField_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-aggregationfield""", alias="AggregationField")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iot.FleetMetric:
        from troposphere.iot import FleetMetric as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iot import FleetMetric as TropoT
        return resource_to_troposphere(self, TropoT)


class JobTemplate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html
    Properties:
        - Name: TimeoutConfig
        - Name: Description
        - Name: JobExecutionsRetryConfig
        - Name: AbortConfig
        - Name: JobTemplateId
        - Name: Document
        - Name: DestinationPackageVersions
        - Name: JobArn
        - Name: JobExecutionsRolloutConfig
        - Name: DocumentSource
        - Name: MaintenanceWindows
        - Name: PresignedUrlConfig
        - Name: Tags
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TimeoutConfig_: Optional['TimeoutConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-timeoutconfig""", alias="TimeoutConfig")
    Description_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-description""", alias="Description")
    JobExecutionsRetryConfig_: Optional['JobExecutionsRetryConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-jobexecutionsretryconfig""", alias="JobExecutionsRetryConfig")
    AbortConfig_: Optional['AbortConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-abortconfig""", alias="AbortConfig")
    JobTemplateId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-jobtemplateid""", alias="JobTemplateId")
    Document_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-document""", alias="Document")
    DestinationPackageVersions_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-destinationpackageversions""", alias="DestinationPackageVersions")
    JobArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-jobarn""", alias="JobArn")
    JobExecutionsRolloutConfig_: Optional['JobExecutionsRolloutConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-jobexecutionsrolloutconfig""", alias="JobExecutionsRolloutConfig")
    DocumentSource_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-documentsource""", alias="DocumentSource")
    MaintenanceWindows_: Optional[List['MaintenanceWindow']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-maintenancewindows""", alias="MaintenanceWindows")
    PresignedUrlConfig_: Optional['PresignedUrlConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-presignedurlconfig""", alias="PresignedUrlConfig")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iot.JobTemplate:
        from troposphere.iot import JobTemplate as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iot import JobTemplate as TropoT
        return resource_to_troposphere(self, TropoT)


class Logging(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-logging.html
    Properties:
        - Name: AccountId
        - Name: RoleArn
        - Name: DefaultLogLevel
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AccountId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-logging.html#cfn-iot-logging-accountid""", alias="AccountId")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-logging.html#cfn-iot-logging-rolearn""", alias="RoleArn")
    DefaultLogLevel_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-logging.html#cfn-iot-logging-defaultloglevel""", alias="DefaultLogLevel")
    

    @property
    def tropo_type(self) -> troposphere.iot.Logging:
        from troposphere.iot import Logging as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iot import Logging as TropoT
        return resource_to_troposphere(self, TropoT)


class MitigationAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html
    Properties:
        - Name: ActionName
        - Name: ActionParams
        - Name: RoleArn
        - Name: Tags
    Attributes:
        - Name: MitigationActionArn
        - Name: MitigationActionId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ActionName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html#cfn-iot-mitigationaction-actionname""", alias="ActionName")
    ActionParams_: 'ActionParams' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html#cfn-iot-mitigationaction-actionparams""", alias="ActionParams")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html#cfn-iot-mitigationaction-rolearn""", alias="RoleArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html#cfn-iot-mitigationaction-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iot.MitigationAction:
        from troposphere.iot import MitigationAction as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iot import MitigationAction as TropoT
        return resource_to_troposphere(self, TropoT)


class Policy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policy.html
    Properties:
        - Name: PolicyName
        - Name: PolicyDocument
        - Name: Tags
    Attributes:
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PolicyName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policy.html#cfn-iot-policy-policyname""", alias="PolicyName")
    PolicyDocument_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policy.html#cfn-iot-policy-policydocument""", alias="PolicyDocument")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policy.html#cfn-iot-policy-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iot.Policy:
        from troposphere.iot import Policy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iot import Policy as TropoT
        return resource_to_troposphere(self, TropoT)


class PolicyPrincipalAttachment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policyprincipalattachment.html
    Properties:
        - Name: PolicyName
        - Name: Principal
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PolicyName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policyprincipalattachment.html#cfn-iot-policyprincipalattachment-policyname""", alias="PolicyName")
    Principal_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policyprincipalattachment.html#cfn-iot-policyprincipalattachment-principal""", alias="Principal")
    

    @property
    def tropo_type(self) -> troposphere.iot.PolicyPrincipalAttachment:
        from troposphere.iot import PolicyPrincipalAttachment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iot import PolicyPrincipalAttachment as TropoT
        return resource_to_troposphere(self, TropoT)


class ProvisioningTemplate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html
    Properties:
        - Name: ProvisioningRoleArn
        - Name: Description
        - Name: PreProvisioningHook
        - Name: TemplateName
        - Name: Enabled
        - Name: TemplateBody
        - Name: TemplateType
        - Name: Tags
    Attributes:
        - Name: TemplateArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ProvisioningRoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-provisioningrolearn""", alias="ProvisioningRoleArn")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-description""", alias="Description")
    PreProvisioningHook_: Optional['ProvisioningHook'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-preprovisioninghook""", alias="PreProvisioningHook")
    TemplateName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-templatename""", alias="TemplateName")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-enabled""", alias="Enabled")
    TemplateBody_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-templatebody""", alias="TemplateBody")
    TemplateType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-templatetype""", alias="TemplateType")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iot.ProvisioningTemplate:
        from troposphere.iot import ProvisioningTemplate as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iot import ProvisioningTemplate as TropoT
        return resource_to_troposphere(self, TropoT)


class ResourceSpecificLogging(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-resourcespecificlogging.html
    Properties:
        - Name: TargetType
        - Name: TargetName
        - Name: LogLevel
    Attributes:
        - Name: TargetId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TargetType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-resourcespecificlogging.html#cfn-iot-resourcespecificlogging-targettype""", alias="TargetType")
    TargetName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-resourcespecificlogging.html#cfn-iot-resourcespecificlogging-targetname""", alias="TargetName")
    LogLevel_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-resourcespecificlogging.html#cfn-iot-resourcespecificlogging-loglevel""", alias="LogLevel")
    

    @property
    def tropo_type(self) -> troposphere.iot.ResourceSpecificLogging:
        from troposphere.iot import ResourceSpecificLogging as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iot import ResourceSpecificLogging as TropoT
        return resource_to_troposphere(self, TropoT)


class RoleAlias(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-rolealias.html
    Properties:
        - Name: RoleAlias
        - Name: CredentialDurationSeconds
        - Name: RoleArn
        - Name: Tags
    Attributes:
        - Name: RoleAliasArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    RoleAlias_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-rolealias.html#cfn-iot-rolealias-rolealias""", alias="RoleAlias")
    CredentialDurationSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-rolealias.html#cfn-iot-rolealias-credentialdurationseconds""", alias="CredentialDurationSeconds")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-rolealias.html#cfn-iot-rolealias-rolearn""", alias="RoleArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-rolealias.html#cfn-iot-rolealias-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iot.RoleAlias:
        from troposphere.iot import RoleAlias as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iot import RoleAlias as TropoT
        return resource_to_troposphere(self, TropoT)


class ScheduledAudit(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html
    Properties:
        - Name: DayOfWeek
        - Name: TargetCheckNames
        - Name: ScheduledAuditName
        - Name: DayOfMonth
        - Name: Frequency
        - Name: Tags
    Attributes:
        - Name: ScheduledAuditArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DayOfWeek_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-dayofweek""", alias="DayOfWeek")
    TargetCheckNames_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-targetchecknames""", alias="TargetCheckNames")
    ScheduledAuditName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-scheduledauditname""", alias="ScheduledAuditName")
    DayOfMonth_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-dayofmonth""", alias="DayOfMonth")
    Frequency_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-frequency""", alias="Frequency")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iot.ScheduledAudit:
        from troposphere.iot import ScheduledAudit as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iot import ScheduledAudit as TropoT
        return resource_to_troposphere(self, TropoT)


class SecurityProfile(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html
    Properties:
        - Name: AdditionalMetricsToRetainV2
        - Name: SecurityProfileDescription
        - Name: Behaviors
        - Name: SecurityProfileName
        - Name: AlertTargets
        - Name: TargetArns
        - Name: Tags
    Attributes:
        - Name: SecurityProfileArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AdditionalMetricsToRetainV2_: Optional[List['MetricToRetain']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-additionalmetricstoretainv2""", alias="AdditionalMetricsToRetainV2")
    SecurityProfileDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-securityprofiledescription""", alias="SecurityProfileDescription")
    Behaviors_: Optional[List['Behavior']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-behaviors""", alias="Behaviors")
    SecurityProfileName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-securityprofilename""", alias="SecurityProfileName")
    AlertTargets_: Optional[Dict[str, 'AlertTarget']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-alerttargets""", alias="AlertTargets")
    TargetArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-targetarns""", alias="TargetArns")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iot.SecurityProfile:
        from troposphere.iot import SecurityProfile as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iot import SecurityProfile as TropoT
        return resource_to_troposphere(self, TropoT)


class SoftwarePackage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-softwarepackage.html
    Properties:
        - Name: Description
        - Name: PackageName
        - Name: Tags
    Attributes:
        - Name: PackageArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-softwarepackage.html#cfn-iot-softwarepackage-description""", alias="Description")
    PackageName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-softwarepackage.html#cfn-iot-softwarepackage-packagename""", alias="PackageName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-softwarepackage.html#cfn-iot-softwarepackage-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iot.SoftwarePackage:
        from troposphere.iot import SoftwarePackage as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iot import SoftwarePackage as TropoT
        return resource_to_troposphere(self, TropoT)


class SoftwarePackageVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-softwarepackageversion.html
    Properties:
        - Name: Description
        - Name: PackageName
        - Name: Attributes
        - Name: VersionName
        - Name: Tags
    Attributes:
        - Name: PackageVersionArn
        - Name: Status
        - Name: ErrorReason
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-softwarepackageversion.html#cfn-iot-softwarepackageversion-description""", alias="Description")
    PackageName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-softwarepackageversion.html#cfn-iot-softwarepackageversion-packagename""", alias="PackageName")
    Attributes_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-softwarepackageversion.html#cfn-iot-softwarepackageversion-attributes""", alias="Attributes")
    VersionName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-softwarepackageversion.html#cfn-iot-softwarepackageversion-versionname""", alias="VersionName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-softwarepackageversion.html#cfn-iot-softwarepackageversion-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iot.SoftwarePackageVersion:
        from troposphere.iot import SoftwarePackageVersion as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iot import SoftwarePackageVersion as TropoT
        return resource_to_troposphere(self, TropoT)


class Thing(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thing.html
    Properties:
        - Name: AttributePayload
        - Name: ThingName
    Attributes:
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AttributePayload_: Optional['AttributePayload'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thing.html#cfn-iot-thing-attributepayload""", alias="AttributePayload")
    ThingName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thing.html#cfn-iot-thing-thingname""", alias="ThingName")
    

    @property
    def tropo_type(self) -> troposphere.iot.Thing:
        from troposphere.iot import Thing as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iot import Thing as TropoT
        return resource_to_troposphere(self, TropoT)


class ThingGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thinggroup.html
    Properties:
        - Name: ParentGroupName
        - Name: ThingGroupName
        - Name: ThingGroupProperties
        - Name: QueryString
        - Name: Tags
    Attributes:
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ParentGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thinggroup.html#cfn-iot-thinggroup-parentgroupname""", alias="ParentGroupName")
    ThingGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thinggroup.html#cfn-iot-thinggroup-thinggroupname""", alias="ThingGroupName")
    ThingGroupProperties_: Optional['ThingGroupProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thinggroup.html#cfn-iot-thinggroup-thinggroupproperties""", alias="ThingGroupProperties")
    QueryString_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thinggroup.html#cfn-iot-thinggroup-querystring""", alias="QueryString")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thinggroup.html#cfn-iot-thinggroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iot.ThingGroup:
        from troposphere.iot import ThingGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iot import ThingGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class ThingPrincipalAttachment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thingprincipalattachment.html
    Properties:
        - Name: Principal
        - Name: ThingName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Principal_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thingprincipalattachment.html#cfn-iot-thingprincipalattachment-principal""", alias="Principal")
    ThingName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thingprincipalattachment.html#cfn-iot-thingprincipalattachment-thingname""", alias="ThingName")
    

    @property
    def tropo_type(self) -> troposphere.iot.ThingPrincipalAttachment:
        from troposphere.iot import ThingPrincipalAttachment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iot import ThingPrincipalAttachment as TropoT
        return resource_to_troposphere(self, TropoT)


class ThingType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thingtype.html
    Properties:
        - Name: DeprecateThingType
        - Name: ThingTypeName
        - Name: ThingTypeProperties
        - Name: Tags
    Attributes:
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DeprecateThingType_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thingtype.html#cfn-iot-thingtype-deprecatethingtype""", alias="DeprecateThingType")
    ThingTypeName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thingtype.html#cfn-iot-thingtype-thingtypename""", alias="ThingTypeName")
    ThingTypeProperties_: Optional['ThingTypeProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thingtype.html#cfn-iot-thingtype-thingtypeproperties""", alias="ThingTypeProperties")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thingtype.html#cfn-iot-thingtype-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iot.ThingType:
        from troposphere.iot import ThingType as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iot import ThingType as TropoT
        return resource_to_troposphere(self, TropoT)


class TopicRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicrule.html
    Properties:
        - Name: TopicRulePayload
        - Name: RuleName
        - Name: Tags
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TopicRulePayload_: 'TopicRulePayload' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicrule.html#cfn-iot-topicrule-topicrulepayload""", alias="TopicRulePayload")
    RuleName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicrule.html#cfn-iot-topicrule-rulename""", alias="RuleName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicrule.html#cfn-iot-topicrule-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iot.TopicRule:
        from troposphere.iot import TopicRule as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iot import TopicRule as TropoT
        return resource_to_troposphere(self, TropoT)


class TopicRuleDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicruledestination.html
    Properties:
        - Name: Status
        - Name: HttpUrlProperties
        - Name: VpcProperties
    Attributes:
        - Name: StatusReason
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicruledestination.html#cfn-iot-topicruledestination-status""", alias="Status")
    HttpUrlProperties_: Optional['HttpUrlDestinationSummary'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicruledestination.html#cfn-iot-topicruledestination-httpurlproperties""", alias="HttpUrlProperties")
    VpcProperties_: Optional['VpcDestinationProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicruledestination.html#cfn-iot-topicruledestination-vpcproperties""", alias="VpcProperties")
    

    @property
    def tropo_type(self) -> troposphere.iot.TopicRuleDestination:
        from troposphere.iot import TopicRuleDestination as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iot import TopicRuleDestination as TropoT
        return resource_to_troposphere(self, TropoT)

