from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class CognitoIdentityProvider(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-cognitoidentityprovider.html
    Properties:
        - Name: ServerSideTokenCheck
        - Name: ProviderName
        - Name: ClientId
    
    """
    
    ServerSideTokenCheck_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-cognitoidentityprovider.html#cfn-cognito-identitypool-cognitoidentityprovider-serversidetokencheck""", alias="ServerSideTokenCheck")
    ProviderName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-cognitoidentityprovider.html#cfn-cognito-identitypool-cognitoidentityprovider-providername""", alias="ProviderName")
    ClientId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-cognitoidentityprovider.html#cfn-cognito-identitypool-cognitoidentityprovider-clientid""", alias="ClientId")
    


    @property
    def tropo_type(self) -> troposphere.cognito.CognitoIdentityProvider:
        from troposphere.cognito import CognitoIdentityProvider as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CognitoStreams(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-cognitostreams.html
    Properties:
        - Name: StreamingStatus
        - Name: StreamName
        - Name: RoleArn
    
    """
    
    StreamingStatus_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-cognitostreams.html#cfn-cognito-identitypool-cognitostreams-streamingstatus""", alias="StreamingStatus")
    StreamName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-cognitostreams.html#cfn-cognito-identitypool-cognitostreams-streamname""", alias="StreamName")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-cognitostreams.html#cfn-cognito-identitypool-cognitostreams-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.cognito.CognitoStreams:
        from troposphere.cognito import CognitoStreams as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PushSync(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-pushsync.html
    Properties:
        - Name: ApplicationArns
        - Name: RoleArn
    
    """
    
    ApplicationArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-pushsync.html#cfn-cognito-identitypool-pushsync-applicationarns""", alias="ApplicationArns")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-pushsync.html#cfn-cognito-identitypool-pushsync-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.cognito.PushSync:
        from troposphere.cognito import PushSync as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MappingRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-mappingrule.html
    Properties:
        - Name: MatchType
        - Name: Value
        - Name: Claim
        - Name: RoleARN
    
    """
    
    MatchType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-mappingrule.html#cfn-cognito-identitypoolroleattachment-mappingrule-matchtype""", alias="MatchType")
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-mappingrule.html#cfn-cognito-identitypoolroleattachment-mappingrule-value""", alias="Value")
    Claim_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-mappingrule.html#cfn-cognito-identitypoolroleattachment-mappingrule-claim""", alias="Claim")
    RoleARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-mappingrule.html#cfn-cognito-identitypoolroleattachment-mappingrule-rolearn""", alias="RoleARN")
    


    @property
    def tropo_type(self) -> troposphere.cognito.MappingRule:
        from troposphere.cognito import MappingRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RoleMapping(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-rolemapping.html
    Properties:
        - Name: Type
        - Name: AmbiguousRoleResolution
        - Name: RulesConfiguration
        - Name: IdentityProvider
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-rolemapping.html#cfn-cognito-identitypoolroleattachment-rolemapping-type""", alias="Type")
    AmbiguousRoleResolution_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-rolemapping.html#cfn-cognito-identitypoolroleattachment-rolemapping-ambiguousroleresolution""", alias="AmbiguousRoleResolution")
    RulesConfiguration_: Optional['RulesConfigurationType'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-rolemapping.html#cfn-cognito-identitypoolroleattachment-rolemapping-rulesconfiguration""", alias="RulesConfiguration")
    IdentityProvider_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-rolemapping.html#cfn-cognito-identitypoolroleattachment-rolemapping-identityprovider""", alias="IdentityProvider")
    


    @property
    def tropo_type(self) -> troposphere.cognito.RoleMapping:
        from troposphere.cognito import RoleMapping as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RulesConfigurationType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-rulesconfigurationtype.html
    Properties:
        - Name: Rules
    
    """
    
    Rules_: List['MappingRule'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-rulesconfigurationtype.html#cfn-cognito-identitypoolroleattachment-rulesconfigurationtype-rules""", alias="Rules")
    


    @property
    def tropo_type(self) -> troposphere.cognito.RulesConfigurationType:
        from troposphere.cognito import RulesConfigurationType as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CloudWatchLogsConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-logdeliveryconfiguration-cloudwatchlogsconfiguration.html
    Properties:
        - Name: LogGroupArn
    
    """
    
    LogGroupArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-logdeliveryconfiguration-cloudwatchlogsconfiguration.html#cfn-cognito-logdeliveryconfiguration-cloudwatchlogsconfiguration-loggrouparn""", alias="LogGroupArn")
    


    @property
    def tropo_type(self) -> troposphere.cognito.CloudWatchLogsConfiguration:
        from troposphere.cognito import CloudWatchLogsConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LogConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-logdeliveryconfiguration-logconfiguration.html
    Properties:
        - Name: EventSource
        - Name: CloudWatchLogsConfiguration
        - Name: LogLevel
    
    """
    
    EventSource_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-logdeliveryconfiguration-logconfiguration.html#cfn-cognito-logdeliveryconfiguration-logconfiguration-eventsource""", alias="EventSource")
    CloudWatchLogsConfiguration_: Optional['CloudWatchLogsConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-logdeliveryconfiguration-logconfiguration.html#cfn-cognito-logdeliveryconfiguration-logconfiguration-cloudwatchlogsconfiguration""", alias="CloudWatchLogsConfiguration")
    LogLevel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-logdeliveryconfiguration-logconfiguration.html#cfn-cognito-logdeliveryconfiguration-logconfiguration-loglevel""", alias="LogLevel")
    


    @property
    def tropo_type(self) -> troposphere.cognito.LogConfiguration:
        from troposphere.cognito import LogConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AccountRecoverySetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-accountrecoverysetting.html
    Properties:
        - Name: RecoveryMechanisms
    
    """
    
    RecoveryMechanisms_: Optional[List['RecoveryOption']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-accountrecoverysetting.html#cfn-cognito-userpool-accountrecoverysetting-recoverymechanisms""", alias="RecoveryMechanisms")
    


    @property
    def tropo_type(self) -> troposphere.cognito.AccountRecoverySetting:
        from troposphere.cognito import AccountRecoverySetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AdminCreateUserConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-admincreateuserconfig.html
    Properties:
        - Name: InviteMessageTemplate
        - Name: UnusedAccountValidityDays
        - Name: AllowAdminCreateUserOnly
    
    """
    
    InviteMessageTemplate_: Optional['InviteMessageTemplate'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-admincreateuserconfig.html#cfn-cognito-userpool-admincreateuserconfig-invitemessagetemplate""", alias="InviteMessageTemplate")
    UnusedAccountValidityDays_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-admincreateuserconfig.html#cfn-cognito-userpool-admincreateuserconfig-unusedaccountvaliditydays""", alias="UnusedAccountValidityDays")
    AllowAdminCreateUserOnly_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-admincreateuserconfig.html#cfn-cognito-userpool-admincreateuserconfig-allowadmincreateuseronly""", alias="AllowAdminCreateUserOnly")
    


    @property
    def tropo_type(self) -> troposphere.cognito.AdminCreateUserConfig:
        from troposphere.cognito import AdminCreateUserConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomEmailSender(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-customemailsender.html
    Properties:
        - Name: LambdaArn
        - Name: LambdaVersion
    
    """
    
    LambdaArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-customemailsender.html#cfn-cognito-userpool-customemailsender-lambdaarn""", alias="LambdaArn")
    LambdaVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-customemailsender.html#cfn-cognito-userpool-customemailsender-lambdaversion""", alias="LambdaVersion")
    


    @property
    def tropo_type(self) -> troposphere.cognito.CustomEmailSender:
        from troposphere.cognito import CustomEmailSender as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomSMSSender(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-customsmssender.html
    Properties:
        - Name: LambdaArn
        - Name: LambdaVersion
    
    """
    
    LambdaArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-customsmssender.html#cfn-cognito-userpool-customsmssender-lambdaarn""", alias="LambdaArn")
    LambdaVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-customsmssender.html#cfn-cognito-userpool-customsmssender-lambdaversion""", alias="LambdaVersion")
    


    @property
    def tropo_type(self) -> troposphere.cognito.CustomSMSSender:
        from troposphere.cognito import CustomSMSSender as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeviceConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-deviceconfiguration.html
    Properties:
        - Name: DeviceOnlyRememberedOnUserPrompt
        - Name: ChallengeRequiredOnNewDevice
    
    """
    
    DeviceOnlyRememberedOnUserPrompt_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-deviceconfiguration.html#cfn-cognito-userpool-deviceconfiguration-deviceonlyrememberedonuserprompt""", alias="DeviceOnlyRememberedOnUserPrompt")
    ChallengeRequiredOnNewDevice_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-deviceconfiguration.html#cfn-cognito-userpool-deviceconfiguration-challengerequiredonnewdevice""", alias="ChallengeRequiredOnNewDevice")
    


    @property
    def tropo_type(self) -> troposphere.cognito.DeviceConfiguration:
        from troposphere.cognito import DeviceConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EmailConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-emailconfiguration.html
    Properties:
        - Name: ReplyToEmailAddress
        - Name: ConfigurationSet
        - Name: EmailSendingAccount
        - Name: SourceArn
        - Name: From
    
    """
    
    ReplyToEmailAddress_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-emailconfiguration.html#cfn-cognito-userpool-emailconfiguration-replytoemailaddress""", alias="ReplyToEmailAddress")
    ConfigurationSet_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-emailconfiguration.html#cfn-cognito-userpool-emailconfiguration-configurationset""", alias="ConfigurationSet")
    EmailSendingAccount_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-emailconfiguration.html#cfn-cognito-userpool-emailconfiguration-emailsendingaccount""", alias="EmailSendingAccount")
    SourceArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-emailconfiguration.html#cfn-cognito-userpool-emailconfiguration-sourcearn""", alias="SourceArn")
    From_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-emailconfiguration.html#cfn-cognito-userpool-emailconfiguration-from""", alias="From")
    


    @property
    def tropo_type(self) -> troposphere.cognito.EmailConfiguration:
        from troposphere.cognito import EmailConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InviteMessageTemplate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-invitemessagetemplate.html
    Properties:
        - Name: EmailMessage
        - Name: SMSMessage
        - Name: EmailSubject
    
    """
    
    EmailMessage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-invitemessagetemplate.html#cfn-cognito-userpool-invitemessagetemplate-emailmessage""", alias="EmailMessage")
    SMSMessage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-invitemessagetemplate.html#cfn-cognito-userpool-invitemessagetemplate-smsmessage""", alias="SMSMessage")
    EmailSubject_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-invitemessagetemplate.html#cfn-cognito-userpool-invitemessagetemplate-emailsubject""", alias="EmailSubject")
    


    @property
    def tropo_type(self) -> troposphere.cognito.InviteMessageTemplate:
        from troposphere.cognito import InviteMessageTemplate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LambdaConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-lambdaconfig.html
    Properties:
        - Name: CreateAuthChallenge
        - Name: PreSignUp
        - Name: KMSKeyID
        - Name: UserMigration
        - Name: PostAuthentication
        - Name: VerifyAuthChallengeResponse
        - Name: PreAuthentication
        - Name: DefineAuthChallenge
        - Name: PreTokenGeneration
        - Name: CustomSMSSender
        - Name: PostConfirmation
        - Name: CustomMessage
        - Name: CustomEmailSender
    
    """
    
    CreateAuthChallenge_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-lambdaconfig.html#cfn-cognito-userpool-lambdaconfig-createauthchallenge""", alias="CreateAuthChallenge")
    PreSignUp_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-lambdaconfig.html#cfn-cognito-userpool-lambdaconfig-presignup""", alias="PreSignUp")
    KMSKeyID_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-lambdaconfig.html#cfn-cognito-userpool-lambdaconfig-kmskeyid""", alias="KMSKeyID")
    UserMigration_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-lambdaconfig.html#cfn-cognito-userpool-lambdaconfig-usermigration""", alias="UserMigration")
    PostAuthentication_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-lambdaconfig.html#cfn-cognito-userpool-lambdaconfig-postauthentication""", alias="PostAuthentication")
    VerifyAuthChallengeResponse_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-lambdaconfig.html#cfn-cognito-userpool-lambdaconfig-verifyauthchallengeresponse""", alias="VerifyAuthChallengeResponse")
    PreAuthentication_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-lambdaconfig.html#cfn-cognito-userpool-lambdaconfig-preauthentication""", alias="PreAuthentication")
    DefineAuthChallenge_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-lambdaconfig.html#cfn-cognito-userpool-lambdaconfig-defineauthchallenge""", alias="DefineAuthChallenge")
    PreTokenGeneration_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-lambdaconfig.html#cfn-cognito-userpool-lambdaconfig-pretokengeneration""", alias="PreTokenGeneration")
    CustomSMSSender_: Optional['CustomSMSSender'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-lambdaconfig.html#cfn-cognito-userpool-lambdaconfig-customsmssender""", alias="CustomSMSSender")
    PostConfirmation_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-lambdaconfig.html#cfn-cognito-userpool-lambdaconfig-postconfirmation""", alias="PostConfirmation")
    CustomMessage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-lambdaconfig.html#cfn-cognito-userpool-lambdaconfig-custommessage""", alias="CustomMessage")
    CustomEmailSender_: Optional['CustomEmailSender'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-lambdaconfig.html#cfn-cognito-userpool-lambdaconfig-customemailsender""", alias="CustomEmailSender")
    


    @property
    def tropo_type(self) -> troposphere.cognito.LambdaConfig:
        from troposphere.cognito import LambdaConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NumberAttributeConstraints(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-numberattributeconstraints.html
    Properties:
        - Name: MinValue
        - Name: MaxValue
    
    """
    
    MinValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-numberattributeconstraints.html#cfn-cognito-userpool-numberattributeconstraints-minvalue""", alias="MinValue")
    MaxValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-numberattributeconstraints.html#cfn-cognito-userpool-numberattributeconstraints-maxvalue""", alias="MaxValue")
    


    @property
    def tropo_type(self) -> troposphere.cognito.NumberAttributeConstraints:
        from troposphere.cognito import NumberAttributeConstraints as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PasswordPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-passwordpolicy.html
    Properties:
        - Name: RequireNumbers
        - Name: MinimumLength
        - Name: TemporaryPasswordValidityDays
        - Name: RequireUppercase
        - Name: RequireLowercase
        - Name: RequireSymbols
    
    """
    
    RequireNumbers_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-passwordpolicy.html#cfn-cognito-userpool-passwordpolicy-requirenumbers""", alias="RequireNumbers")
    MinimumLength_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-passwordpolicy.html#cfn-cognito-userpool-passwordpolicy-minimumlength""", alias="MinimumLength")
    TemporaryPasswordValidityDays_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-passwordpolicy.html#cfn-cognito-userpool-passwordpolicy-temporarypasswordvaliditydays""", alias="TemporaryPasswordValidityDays")
    RequireUppercase_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-passwordpolicy.html#cfn-cognito-userpool-passwordpolicy-requireuppercase""", alias="RequireUppercase")
    RequireLowercase_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-passwordpolicy.html#cfn-cognito-userpool-passwordpolicy-requirelowercase""", alias="RequireLowercase")
    RequireSymbols_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-passwordpolicy.html#cfn-cognito-userpool-passwordpolicy-requiresymbols""", alias="RequireSymbols")
    


    @property
    def tropo_type(self) -> troposphere.cognito.PasswordPolicy:
        from troposphere.cognito import PasswordPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Policies(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-policies.html
    Properties:
        - Name: PasswordPolicy
    
    """
    
    PasswordPolicy_: Optional['PasswordPolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-policies.html#cfn-cognito-userpool-policies-passwordpolicy""", alias="PasswordPolicy")
    


    @property
    def tropo_type(self) -> troposphere.cognito.Policies:
        from troposphere.cognito import Policies as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RecoveryOption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-recoveryoption.html
    Properties:
        - Name: Priority
        - Name: Name
    
    """
    
    Priority_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-recoveryoption.html#cfn-cognito-userpool-recoveryoption-priority""", alias="Priority")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-recoveryoption.html#cfn-cognito-userpool-recoveryoption-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.cognito.RecoveryOption:
        from troposphere.cognito import RecoveryOption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SchemaAttribute(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-schemaattribute.html
    Properties:
        - Name: DeveloperOnlyAttribute
        - Name: Mutable
        - Name: AttributeDataType
        - Name: StringAttributeConstraints
        - Name: Required
        - Name: NumberAttributeConstraints
        - Name: Name
    
    """
    
    DeveloperOnlyAttribute_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-schemaattribute.html#cfn-cognito-userpool-schemaattribute-developeronlyattribute""", alias="DeveloperOnlyAttribute")
    Mutable_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-schemaattribute.html#cfn-cognito-userpool-schemaattribute-mutable""", alias="Mutable")
    AttributeDataType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-schemaattribute.html#cfn-cognito-userpool-schemaattribute-attributedatatype""", alias="AttributeDataType")
    StringAttributeConstraints_: Optional['StringAttributeConstraints'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-schemaattribute.html#cfn-cognito-userpool-schemaattribute-stringattributeconstraints""", alias="StringAttributeConstraints")
    Required_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-schemaattribute.html#cfn-cognito-userpool-schemaattribute-required""", alias="Required")
    NumberAttributeConstraints_: Optional['NumberAttributeConstraints'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-schemaattribute.html#cfn-cognito-userpool-schemaattribute-numberattributeconstraints""", alias="NumberAttributeConstraints")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-schemaattribute.html#cfn-cognito-userpool-schemaattribute-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.cognito.SchemaAttribute:
        from troposphere.cognito import SchemaAttribute as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SmsConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-smsconfiguration.html
    Properties:
        - Name: SnsRegion
        - Name: ExternalId
        - Name: SnsCallerArn
    
    """
    
    SnsRegion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-smsconfiguration.html#cfn-cognito-userpool-smsconfiguration-snsregion""", alias="SnsRegion")
    ExternalId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-smsconfiguration.html#cfn-cognito-userpool-smsconfiguration-externalid""", alias="ExternalId")
    SnsCallerArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-smsconfiguration.html#cfn-cognito-userpool-smsconfiguration-snscallerarn""", alias="SnsCallerArn")
    


    @property
    def tropo_type(self) -> troposphere.cognito.SmsConfiguration:
        from troposphere.cognito import SmsConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StringAttributeConstraints(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-stringattributeconstraints.html
    Properties:
        - Name: MinLength
        - Name: MaxLength
    
    """
    
    MinLength_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-stringattributeconstraints.html#cfn-cognito-userpool-stringattributeconstraints-minlength""", alias="MinLength")
    MaxLength_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-stringattributeconstraints.html#cfn-cognito-userpool-stringattributeconstraints-maxlength""", alias="MaxLength")
    


    @property
    def tropo_type(self) -> troposphere.cognito.StringAttributeConstraints:
        from troposphere.cognito import StringAttributeConstraints as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class UserAttributeUpdateSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-userattributeupdatesettings.html
    Properties:
        - Name: AttributesRequireVerificationBeforeUpdate
    
    """
    
    AttributesRequireVerificationBeforeUpdate_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-userattributeupdatesettings.html#cfn-cognito-userpool-userattributeupdatesettings-attributesrequireverificationbeforeupdate""", alias="AttributesRequireVerificationBeforeUpdate")
    


    @property
    def tropo_type(self) -> troposphere.cognito.UserAttributeUpdateSettings:
        from troposphere.cognito import UserAttributeUpdateSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class UserPoolAddOns(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-userpooladdons.html
    Properties:
        - Name: AdvancedSecurityMode
    
    """
    
    AdvancedSecurityMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-userpooladdons.html#cfn-cognito-userpool-userpooladdons-advancedsecuritymode""", alias="AdvancedSecurityMode")
    


    @property
    def tropo_type(self) -> troposphere.cognito.UserPoolAddOns:
        from troposphere.cognito import UserPoolAddOns as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class UsernameConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-usernameconfiguration.html
    Properties:
        - Name: CaseSensitive
    
    """
    
    CaseSensitive_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-usernameconfiguration.html#cfn-cognito-userpool-usernameconfiguration-casesensitive""", alias="CaseSensitive")
    


    @property
    def tropo_type(self) -> troposphere.cognito.UsernameConfiguration:
        from troposphere.cognito import UsernameConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VerificationMessageTemplate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-verificationmessagetemplate.html
    Properties:
        - Name: EmailMessageByLink
        - Name: EmailMessage
        - Name: SmsMessage
        - Name: EmailSubject
        - Name: DefaultEmailOption
        - Name: EmailSubjectByLink
    
    """
    
    EmailMessageByLink_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-verificationmessagetemplate.html#cfn-cognito-userpool-verificationmessagetemplate-emailmessagebylink""", alias="EmailMessageByLink")
    EmailMessage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-verificationmessagetemplate.html#cfn-cognito-userpool-verificationmessagetemplate-emailmessage""", alias="EmailMessage")
    SmsMessage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-verificationmessagetemplate.html#cfn-cognito-userpool-verificationmessagetemplate-smsmessage""", alias="SmsMessage")
    EmailSubject_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-verificationmessagetemplate.html#cfn-cognito-userpool-verificationmessagetemplate-emailsubject""", alias="EmailSubject")
    DefaultEmailOption_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-verificationmessagetemplate.html#cfn-cognito-userpool-verificationmessagetemplate-defaultemailoption""", alias="DefaultEmailOption")
    EmailSubjectByLink_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-verificationmessagetemplate.html#cfn-cognito-userpool-verificationmessagetemplate-emailsubjectbylink""", alias="EmailSubjectByLink")
    


    @property
    def tropo_type(self) -> troposphere.cognito.VerificationMessageTemplate:
        from troposphere.cognito import VerificationMessageTemplate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AnalyticsConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolclient-analyticsconfiguration.html
    Properties:
        - Name: ApplicationArn
        - Name: UserDataShared
        - Name: ExternalId
        - Name: ApplicationId
        - Name: RoleArn
    
    """
    
    ApplicationArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolclient-analyticsconfiguration.html#cfn-cognito-userpoolclient-analyticsconfiguration-applicationarn""", alias="ApplicationArn")
    UserDataShared_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolclient-analyticsconfiguration.html#cfn-cognito-userpoolclient-analyticsconfiguration-userdatashared""", alias="UserDataShared")
    ExternalId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolclient-analyticsconfiguration.html#cfn-cognito-userpoolclient-analyticsconfiguration-externalid""", alias="ExternalId")
    ApplicationId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolclient-analyticsconfiguration.html#cfn-cognito-userpoolclient-analyticsconfiguration-applicationid""", alias="ApplicationId")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolclient-analyticsconfiguration.html#cfn-cognito-userpoolclient-analyticsconfiguration-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.cognito.AnalyticsConfiguration:
        from troposphere.cognito import AnalyticsConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TokenValidityUnits(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolclient-tokenvalidityunits.html
    Properties:
        - Name: IdToken
        - Name: RefreshToken
        - Name: AccessToken
    
    """
    
    IdToken_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolclient-tokenvalidityunits.html#cfn-cognito-userpoolclient-tokenvalidityunits-idtoken""", alias="IdToken")
    RefreshToken_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolclient-tokenvalidityunits.html#cfn-cognito-userpoolclient-tokenvalidityunits-refreshtoken""", alias="RefreshToken")
    AccessToken_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolclient-tokenvalidityunits.html#cfn-cognito-userpoolclient-tokenvalidityunits-accesstoken""", alias="AccessToken")
    


    @property
    def tropo_type(self) -> troposphere.cognito.TokenValidityUnits:
        from troposphere.cognito import TokenValidityUnits as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomDomainConfigType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpooldomain-customdomainconfigtype.html
    Properties:
        - Name: CertificateArn
    
    """
    
    CertificateArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpooldomain-customdomainconfigtype.html#cfn-cognito-userpooldomain-customdomainconfigtype-certificatearn""", alias="CertificateArn")
    


    @property
    def tropo_type(self) -> troposphere.cognito.CustomDomainConfigType:
        from troposphere.cognito import CustomDomainConfigType as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResourceServerScopeType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolresourceserver-resourceserverscopetype.html
    Properties:
        - Name: ScopeName
        - Name: ScopeDescription
    
    """
    
    ScopeName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolresourceserver-resourceserverscopetype.html#cfn-cognito-userpoolresourceserver-resourceserverscopetype-scopename""", alias="ScopeName")
    ScopeDescription_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolresourceserver-resourceserverscopetype.html#cfn-cognito-userpoolresourceserver-resourceserverscopetype-scopedescription""", alias="ScopeDescription")
    


    @property
    def tropo_type(self) -> troposphere.cognito.ResourceServerScopeType:
        from troposphere.cognito import ResourceServerScopeType as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AccountTakeoverActionType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoveractiontype.html
    Properties:
        - Name: Notify
        - Name: EventAction
    
    """
    
    Notify_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoveractiontype.html#cfn-cognito-userpoolriskconfigurationattachment-accounttakeoveractiontype-notify""", alias="Notify")
    EventAction_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoveractiontype.html#cfn-cognito-userpoolriskconfigurationattachment-accounttakeoveractiontype-eventaction""", alias="EventAction")
    


    @property
    def tropo_type(self) -> troposphere.cognito.AccountTakeoverActionType:
        from troposphere.cognito import AccountTakeoverActionType as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AccountTakeoverActionsType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoveractionstype.html
    Properties:
        - Name: HighAction
        - Name: LowAction
        - Name: MediumAction
    
    """
    
    HighAction_: Optional['AccountTakeoverActionType'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoveractionstype.html#cfn-cognito-userpoolriskconfigurationattachment-accounttakeoveractionstype-highaction""", alias="HighAction")
    LowAction_: Optional['AccountTakeoverActionType'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoveractionstype.html#cfn-cognito-userpoolriskconfigurationattachment-accounttakeoveractionstype-lowaction""", alias="LowAction")
    MediumAction_: Optional['AccountTakeoverActionType'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoveractionstype.html#cfn-cognito-userpoolriskconfigurationattachment-accounttakeoveractionstype-mediumaction""", alias="MediumAction")
    


    @property
    def tropo_type(self) -> troposphere.cognito.AccountTakeoverActionsType:
        from troposphere.cognito import AccountTakeoverActionsType as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AccountTakeoverRiskConfigurationType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoverriskconfigurationtype.html
    Properties:
        - Name: Actions
        - Name: NotifyConfiguration
    
    """
    
    Actions_: 'AccountTakeoverActionsType' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoverriskconfigurationtype.html#cfn-cognito-userpoolriskconfigurationattachment-accounttakeoverriskconfigurationtype-actions""", alias="Actions")
    NotifyConfiguration_: Optional['NotifyConfigurationType'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoverriskconfigurationtype.html#cfn-cognito-userpoolriskconfigurationattachment-accounttakeoverriskconfigurationtype-notifyconfiguration""", alias="NotifyConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.cognito.AccountTakeoverRiskConfigurationType:
        from troposphere.cognito import AccountTakeoverRiskConfigurationType as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CompromisedCredentialsActionsType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-compromisedcredentialsactionstype.html
    Properties:
        - Name: EventAction
    
    """
    
    EventAction_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-compromisedcredentialsactionstype.html#cfn-cognito-userpoolriskconfigurationattachment-compromisedcredentialsactionstype-eventaction""", alias="EventAction")
    


    @property
    def tropo_type(self) -> troposphere.cognito.CompromisedCredentialsActionsType:
        from troposphere.cognito import CompromisedCredentialsActionsType as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CompromisedCredentialsRiskConfigurationType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-compromisedcredentialsriskconfigurationtype.html
    Properties:
        - Name: Actions
        - Name: EventFilter
    
    """
    
    Actions_: 'CompromisedCredentialsActionsType' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-compromisedcredentialsriskconfigurationtype.html#cfn-cognito-userpoolriskconfigurationattachment-compromisedcredentialsriskconfigurationtype-actions""", alias="Actions")
    EventFilter_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-compromisedcredentialsriskconfigurationtype.html#cfn-cognito-userpoolriskconfigurationattachment-compromisedcredentialsriskconfigurationtype-eventfilter""", alias="EventFilter")
    


    @property
    def tropo_type(self) -> troposphere.cognito.CompromisedCredentialsRiskConfigurationType:
        from troposphere.cognito import CompromisedCredentialsRiskConfigurationType as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NotifyConfigurationType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype.html
    Properties:
        - Name: BlockEmail
        - Name: ReplyTo
        - Name: SourceArn
        - Name: NoActionEmail
        - Name: From
        - Name: MfaEmail
    
    """
    
    BlockEmail_: Optional['NotifyEmailType'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype.html#cfn-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype-blockemail""", alias="BlockEmail")
    ReplyTo_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype.html#cfn-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype-replyto""", alias="ReplyTo")
    SourceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype.html#cfn-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype-sourcearn""", alias="SourceArn")
    NoActionEmail_: Optional['NotifyEmailType'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype.html#cfn-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype-noactionemail""", alias="NoActionEmail")
    From_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype.html#cfn-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype-from""", alias="From")
    MfaEmail_: Optional['NotifyEmailType'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype.html#cfn-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype-mfaemail""", alias="MfaEmail")
    


    @property
    def tropo_type(self) -> troposphere.cognito.NotifyConfigurationType:
        from troposphere.cognito import NotifyConfigurationType as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NotifyEmailType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-notifyemailtype.html
    Properties:
        - Name: TextBody
        - Name: HtmlBody
        - Name: Subject
    
    """
    
    TextBody_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-notifyemailtype.html#cfn-cognito-userpoolriskconfigurationattachment-notifyemailtype-textbody""", alias="TextBody")
    HtmlBody_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-notifyemailtype.html#cfn-cognito-userpoolriskconfigurationattachment-notifyemailtype-htmlbody""", alias="HtmlBody")
    Subject_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-notifyemailtype.html#cfn-cognito-userpoolriskconfigurationattachment-notifyemailtype-subject""", alias="Subject")
    


    @property
    def tropo_type(self) -> troposphere.cognito.NotifyEmailType:
        from troposphere.cognito import NotifyEmailType as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RiskExceptionConfigurationType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-riskexceptionconfigurationtype.html
    Properties:
        - Name: BlockedIPRangeList
        - Name: SkippedIPRangeList
    
    """
    
    BlockedIPRangeList_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-riskexceptionconfigurationtype.html#cfn-cognito-userpoolriskconfigurationattachment-riskexceptionconfigurationtype-blockediprangelist""", alias="BlockedIPRangeList")
    SkippedIPRangeList_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-riskexceptionconfigurationtype.html#cfn-cognito-userpoolriskconfigurationattachment-riskexceptionconfigurationtype-skippediprangelist""", alias="SkippedIPRangeList")
    


    @property
    def tropo_type(self) -> troposphere.cognito.RiskExceptionConfigurationType:
        from troposphere.cognito import RiskExceptionConfigurationType as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AttributeType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpooluser-attributetype.html
    Properties:
        - Name: Value
        - Name: Name
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpooluser-attributetype.html#cfn-cognito-userpooluser-attributetype-value""", alias="Value")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpooluser-attributetype.html#cfn-cognito-userpooluser-attributetype-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.cognito.AttributeType:
        from troposphere.cognito import AttributeType as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class IdentityPool(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html
    Properties:
        - Name: PushSync
        - Name: CognitoIdentityProviders
        - Name: CognitoEvents
        - Name: DeveloperProviderName
        - Name: CognitoStreams
        - Name: IdentityPoolName
        - Name: AllowUnauthenticatedIdentities
        - Name: SupportedLoginProviders
        - Name: SamlProviderARNs
        - Name: OpenIdConnectProviderARNs
        - Name: AllowClassicFlow
    Attributes:
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PushSync_: Optional['PushSync'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-pushsync""", alias="PushSync")
    CognitoIdentityProviders_: Optional[List['CognitoIdentityProvider']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-cognitoidentityproviders""", alias="CognitoIdentityProviders")
    CognitoEvents_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-cognitoevents""", alias="CognitoEvents")
    DeveloperProviderName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-developerprovidername""", alias="DeveloperProviderName")
    CognitoStreams_: Optional['CognitoStreams'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-cognitostreams""", alias="CognitoStreams")
    IdentityPoolName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-identitypoolname""", alias="IdentityPoolName")
    AllowUnauthenticatedIdentities_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-allowunauthenticatedidentities""", alias="AllowUnauthenticatedIdentities")
    SupportedLoginProviders_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-supportedloginproviders""", alias="SupportedLoginProviders")
    SamlProviderARNs_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-samlproviderarns""", alias="SamlProviderARNs")
    OpenIdConnectProviderARNs_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-openidconnectproviderarns""", alias="OpenIdConnectProviderARNs")
    AllowClassicFlow_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-allowclassicflow""", alias="AllowClassicFlow")
    

    @property
    def tropo_type(self) -> troposphere.cognito.IdentityPool:
        from troposphere.cognito import IdentityPool as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cognito import IdentityPool as TropoT
        return resource_to_troposphere(self, TropoT)


class IdentityPoolPrincipalTag(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypoolprincipaltag.html
    Properties:
        - Name: PrincipalTags
        - Name: UseDefaults
        - Name: IdentityProviderName
        - Name: IdentityPoolId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PrincipalTags_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypoolprincipaltag.html#cfn-cognito-identitypoolprincipaltag-principaltags""", alias="PrincipalTags")
    UseDefaults_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypoolprincipaltag.html#cfn-cognito-identitypoolprincipaltag-usedefaults""", alias="UseDefaults")
    IdentityProviderName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypoolprincipaltag.html#cfn-cognito-identitypoolprincipaltag-identityprovidername""", alias="IdentityProviderName")
    IdentityPoolId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypoolprincipaltag.html#cfn-cognito-identitypoolprincipaltag-identitypoolid""", alias="IdentityPoolId")
    

    @property
    def tropo_type(self) -> troposphere.cognito.IdentityPoolPrincipalTag:
        from troposphere.cognito import IdentityPoolPrincipalTag as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cognito import IdentityPoolPrincipalTag as TropoT
        return resource_to_troposphere(self, TropoT)


class IdentityPoolRoleAttachment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypoolroleattachment.html
    Properties:
        - Name: RoleMappings
        - Name: IdentityPoolId
        - Name: Roles
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    RoleMappings_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypoolroleattachment.html#cfn-cognito-identitypoolroleattachment-rolemappings""", alias="RoleMappings")
    IdentityPoolId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypoolroleattachment.html#cfn-cognito-identitypoolroleattachment-identitypoolid""", alias="IdentityPoolId")
    Roles_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypoolroleattachment.html#cfn-cognito-identitypoolroleattachment-roles""", alias="Roles")
    

    @property
    def tropo_type(self) -> troposphere.cognito.IdentityPoolRoleAttachment:
        from troposphere.cognito import IdentityPoolRoleAttachment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cognito import IdentityPoolRoleAttachment as TropoT
        return resource_to_troposphere(self, TropoT)


class LogDeliveryConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-logdeliveryconfiguration.html
    Properties:
        - Name: UserPoolId
        - Name: LogConfigurations
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    UserPoolId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-logdeliveryconfiguration.html#cfn-cognito-logdeliveryconfiguration-userpoolid""", alias="UserPoolId")
    LogConfigurations_: Optional[List['LogConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-logdeliveryconfiguration.html#cfn-cognito-logdeliveryconfiguration-logconfigurations""", alias="LogConfigurations")
    

    @property
    def tropo_type(self) -> troposphere.cognito.LogDeliveryConfiguration:
        from troposphere.cognito import LogDeliveryConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cognito import LogDeliveryConfiguration as TropoT
        return resource_to_troposphere(self, TropoT)


class UserPool(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html
    Properties:
        - Name: UserPoolTags
        - Name: Policies
        - Name: VerificationMessageTemplate
        - Name: MfaConfiguration
        - Name: Schema
        - Name: AdminCreateUserConfig
        - Name: DeletionProtection
        - Name: SmsAuthenticationMessage
        - Name: UsernameConfiguration
        - Name: UserPoolName
        - Name: SmsVerificationMessage
        - Name: UserPoolAddOns
        - Name: UserAttributeUpdateSettings
        - Name: EmailConfiguration
        - Name: SmsConfiguration
        - Name: AliasAttributes
        - Name: EnabledMfas
        - Name: EmailVerificationSubject
        - Name: LambdaConfig
        - Name: UsernameAttributes
        - Name: AutoVerifiedAttributes
        - Name: DeviceConfiguration
        - Name: EmailVerificationMessage
        - Name: AccountRecoverySetting
    Attributes:
        - Name: ProviderName
        - Name: UserPoolId
        - Name: ProviderURL
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    UserPoolTags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-userpooltags""", alias="UserPoolTags")
    Policies_: Optional['Policies'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-policies""", alias="Policies")
    VerificationMessageTemplate_: Optional['VerificationMessageTemplate'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-verificationmessagetemplate""", alias="VerificationMessageTemplate")
    MfaConfiguration_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-mfaconfiguration""", alias="MfaConfiguration")
    Schema_: Optional[List['SchemaAttribute']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-schema""", alias="Schema")
    AdminCreateUserConfig_: Optional['AdminCreateUserConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-admincreateuserconfig""", alias="AdminCreateUserConfig")
    DeletionProtection_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-deletionprotection""", alias="DeletionProtection")
    SmsAuthenticationMessage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-smsauthenticationmessage""", alias="SmsAuthenticationMessage")
    UsernameConfiguration_: Optional['UsernameConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-usernameconfiguration""", alias="UsernameConfiguration")
    UserPoolName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-userpoolname""", alias="UserPoolName")
    SmsVerificationMessage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-smsverificationmessage""", alias="SmsVerificationMessage")
    UserPoolAddOns_: Optional['UserPoolAddOns'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-userpooladdons""", alias="UserPoolAddOns")
    UserAttributeUpdateSettings_: Optional['UserAttributeUpdateSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-userattributeupdatesettings""", alias="UserAttributeUpdateSettings")
    EmailConfiguration_: Optional['EmailConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-emailconfiguration""", alias="EmailConfiguration")
    SmsConfiguration_: Optional['SmsConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-smsconfiguration""", alias="SmsConfiguration")
    AliasAttributes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-aliasattributes""", alias="AliasAttributes")
    EnabledMfas_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-enabledmfas""", alias="EnabledMfas")
    EmailVerificationSubject_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-emailverificationsubject""", alias="EmailVerificationSubject")
    LambdaConfig_: Optional['LambdaConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-lambdaconfig""", alias="LambdaConfig")
    UsernameAttributes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-usernameattributes""", alias="UsernameAttributes")
    AutoVerifiedAttributes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-autoverifiedattributes""", alias="AutoVerifiedAttributes")
    DeviceConfiguration_: Optional['DeviceConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-deviceconfiguration""", alias="DeviceConfiguration")
    EmailVerificationMessage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-emailverificationmessage""", alias="EmailVerificationMessage")
    AccountRecoverySetting_: Optional['AccountRecoverySetting'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-accountrecoverysetting""", alias="AccountRecoverySetting")
    

    @property
    def tropo_type(self) -> troposphere.cognito.UserPool:
        from troposphere.cognito import UserPool as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cognito import UserPool as TropoT
        return resource_to_troposphere(self, TropoT)


class UserPoolClient(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html
    Properties:
        - Name: AnalyticsConfiguration
        - Name: GenerateSecret
        - Name: CallbackURLs
        - Name: EnablePropagateAdditionalUserContextData
        - Name: IdTokenValidity
        - Name: AuthSessionValidity
        - Name: AllowedOAuthScopes
        - Name: TokenValidityUnits
        - Name: ReadAttributes
        - Name: AllowedOAuthFlowsUserPoolClient
        - Name: DefaultRedirectURI
        - Name: SupportedIdentityProviders
        - Name: ClientName
        - Name: UserPoolId
        - Name: AllowedOAuthFlows
        - Name: ExplicitAuthFlows
        - Name: LogoutURLs
        - Name: AccessTokenValidity
        - Name: RefreshTokenValidity
        - Name: WriteAttributes
        - Name: PreventUserExistenceErrors
        - Name: EnableTokenRevocation
    Attributes:
        - Name: ClientSecret
        - Name: ClientId
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AnalyticsConfiguration_: Optional['AnalyticsConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-analyticsconfiguration""", alias="AnalyticsConfiguration")
    GenerateSecret_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-generatesecret""", alias="GenerateSecret")
    CallbackURLs_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-callbackurls""", alias="CallbackURLs")
    EnablePropagateAdditionalUserContextData_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-enablepropagateadditionalusercontextdata""", alias="EnablePropagateAdditionalUserContextData")
    IdTokenValidity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-idtokenvalidity""", alias="IdTokenValidity")
    AuthSessionValidity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-authsessionvalidity""", alias="AuthSessionValidity")
    AllowedOAuthScopes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-allowedoauthscopes""", alias="AllowedOAuthScopes")
    TokenValidityUnits_: Optional['TokenValidityUnits'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-tokenvalidityunits""", alias="TokenValidityUnits")
    ReadAttributes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-readattributes""", alias="ReadAttributes")
    AllowedOAuthFlowsUserPoolClient_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-allowedoauthflowsuserpoolclient""", alias="AllowedOAuthFlowsUserPoolClient")
    DefaultRedirectURI_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-defaultredirecturi""", alias="DefaultRedirectURI")
    SupportedIdentityProviders_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-supportedidentityproviders""", alias="SupportedIdentityProviders")
    ClientName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-clientname""", alias="ClientName")
    UserPoolId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-userpoolid""", alias="UserPoolId")
    AllowedOAuthFlows_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-allowedoauthflows""", alias="AllowedOAuthFlows")
    ExplicitAuthFlows_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-explicitauthflows""", alias="ExplicitAuthFlows")
    LogoutURLs_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-logouturls""", alias="LogoutURLs")
    AccessTokenValidity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-accesstokenvalidity""", alias="AccessTokenValidity")
    RefreshTokenValidity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-refreshtokenvalidity""", alias="RefreshTokenValidity")
    WriteAttributes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-writeattributes""", alias="WriteAttributes")
    PreventUserExistenceErrors_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-preventuserexistenceerrors""", alias="PreventUserExistenceErrors")
    EnableTokenRevocation_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-enabletokenrevocation""", alias="EnableTokenRevocation")
    

    @property
    def tropo_type(self) -> troposphere.cognito.UserPoolClient:
        from troposphere.cognito import UserPoolClient as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cognito import UserPoolClient as TropoT
        return resource_to_troposphere(self, TropoT)


class UserPoolDomain(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooldomain.html
    Properties:
        - Name: UserPoolId
        - Name: CustomDomainConfig
        - Name: Domain
    Attributes:
        - Name: CloudFrontDistribution
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    UserPoolId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooldomain.html#cfn-cognito-userpooldomain-userpoolid""", alias="UserPoolId")
    CustomDomainConfig_: Optional['CustomDomainConfigType'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooldomain.html#cfn-cognito-userpooldomain-customdomainconfig""", alias="CustomDomainConfig")
    Domain_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooldomain.html#cfn-cognito-userpooldomain-domain""", alias="Domain")
    

    @property
    def tropo_type(self) -> troposphere.cognito.UserPoolDomain:
        from troposphere.cognito import UserPoolDomain as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cognito import UserPoolDomain as TropoT
        return resource_to_troposphere(self, TropoT)


class UserPoolGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolgroup.html
    Properties:
        - Name: GroupName
        - Name: Description
        - Name: UserPoolId
        - Name: Precedence
        - Name: RoleArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    GroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolgroup.html#cfn-cognito-userpoolgroup-groupname""", alias="GroupName")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolgroup.html#cfn-cognito-userpoolgroup-description""", alias="Description")
    UserPoolId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolgroup.html#cfn-cognito-userpoolgroup-userpoolid""", alias="UserPoolId")
    Precedence_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolgroup.html#cfn-cognito-userpoolgroup-precedence""", alias="Precedence")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolgroup.html#cfn-cognito-userpoolgroup-rolearn""", alias="RoleArn")
    

    @property
    def tropo_type(self) -> troposphere.cognito.UserPoolGroup:
        from troposphere.cognito import UserPoolGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cognito import UserPoolGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class UserPoolIdentityProvider(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolidentityprovider.html
    Properties:
        - Name: ProviderName
        - Name: UserPoolId
        - Name: AttributeMapping
        - Name: ProviderDetails
        - Name: ProviderType
        - Name: IdpIdentifiers
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ProviderName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolidentityprovider.html#cfn-cognito-userpoolidentityprovider-providername""", alias="ProviderName")
    UserPoolId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolidentityprovider.html#cfn-cognito-userpoolidentityprovider-userpoolid""", alias="UserPoolId")
    AttributeMapping_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolidentityprovider.html#cfn-cognito-userpoolidentityprovider-attributemapping""", alias="AttributeMapping")
    ProviderDetails_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolidentityprovider.html#cfn-cognito-userpoolidentityprovider-providerdetails""", alias="ProviderDetails")
    ProviderType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolidentityprovider.html#cfn-cognito-userpoolidentityprovider-providertype""", alias="ProviderType")
    IdpIdentifiers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolidentityprovider.html#cfn-cognito-userpoolidentityprovider-idpidentifiers""", alias="IdpIdentifiers")
    

    @property
    def tropo_type(self) -> troposphere.cognito.UserPoolIdentityProvider:
        from troposphere.cognito import UserPoolIdentityProvider as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cognito import UserPoolIdentityProvider as TropoT
        return resource_to_troposphere(self, TropoT)


class UserPoolResourceServer(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolresourceserver.html
    Properties:
        - Name: UserPoolId
        - Name: Identifier
        - Name: Scopes
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    UserPoolId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolresourceserver.html#cfn-cognito-userpoolresourceserver-userpoolid""", alias="UserPoolId")
    Identifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolresourceserver.html#cfn-cognito-userpoolresourceserver-identifier""", alias="Identifier")
    Scopes_: Optional[List['ResourceServerScopeType']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolresourceserver.html#cfn-cognito-userpoolresourceserver-scopes""", alias="Scopes")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolresourceserver.html#cfn-cognito-userpoolresourceserver-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.cognito.UserPoolResourceServer:
        from troposphere.cognito import UserPoolResourceServer as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cognito import UserPoolResourceServer as TropoT
        return resource_to_troposphere(self, TropoT)


class UserPoolRiskConfigurationAttachment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolriskconfigurationattachment.html
    Properties:
        - Name: CompromisedCredentialsRiskConfiguration
        - Name: UserPoolId
        - Name: ClientId
        - Name: AccountTakeoverRiskConfiguration
        - Name: RiskExceptionConfiguration
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CompromisedCredentialsRiskConfiguration_: Optional['CompromisedCredentialsRiskConfigurationType'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolriskconfigurationattachment.html#cfn-cognito-userpoolriskconfigurationattachment-compromisedcredentialsriskconfiguration""", alias="CompromisedCredentialsRiskConfiguration")
    UserPoolId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolriskconfigurationattachment.html#cfn-cognito-userpoolriskconfigurationattachment-userpoolid""", alias="UserPoolId")
    ClientId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolriskconfigurationattachment.html#cfn-cognito-userpoolriskconfigurationattachment-clientid""", alias="ClientId")
    AccountTakeoverRiskConfiguration_: Optional['AccountTakeoverRiskConfigurationType'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolriskconfigurationattachment.html#cfn-cognito-userpoolriskconfigurationattachment-accounttakeoverriskconfiguration""", alias="AccountTakeoverRiskConfiguration")
    RiskExceptionConfiguration_: Optional['RiskExceptionConfigurationType'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolriskconfigurationattachment.html#cfn-cognito-userpoolriskconfigurationattachment-riskexceptionconfiguration""", alias="RiskExceptionConfiguration")
    

    @property
    def tropo_type(self) -> troposphere.cognito.UserPoolRiskConfigurationAttachment:
        from troposphere.cognito import UserPoolRiskConfigurationAttachment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cognito import UserPoolRiskConfigurationAttachment as TropoT
        return resource_to_troposphere(self, TropoT)


class UserPoolUICustomizationAttachment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluicustomizationattachment.html
    Properties:
        - Name: CSS
        - Name: UserPoolId
        - Name: ClientId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CSS_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluicustomizationattachment.html#cfn-cognito-userpooluicustomizationattachment-css""", alias="CSS")
    UserPoolId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluicustomizationattachment.html#cfn-cognito-userpooluicustomizationattachment-userpoolid""", alias="UserPoolId")
    ClientId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluicustomizationattachment.html#cfn-cognito-userpooluicustomizationattachment-clientid""", alias="ClientId")
    

    @property
    def tropo_type(self) -> troposphere.cognito.UserPoolUICustomizationAttachment:
        from troposphere.cognito import UserPoolUICustomizationAttachment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cognito import UserPoolUICustomizationAttachment as TropoT
        return resource_to_troposphere(self, TropoT)


class UserPoolUser(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluser.html
    Properties:
        - Name: ValidationData
        - Name: UserPoolId
        - Name: Username
        - Name: MessageAction
        - Name: ClientMetadata
        - Name: DesiredDeliveryMediums
        - Name: ForceAliasCreation
        - Name: UserAttributes
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ValidationData_: Optional[List['AttributeType']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluser.html#cfn-cognito-userpooluser-validationdata""", alias="ValidationData")
    UserPoolId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluser.html#cfn-cognito-userpooluser-userpoolid""", alias="UserPoolId")
    Username_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluser.html#cfn-cognito-userpooluser-username""", alias="Username")
    MessageAction_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluser.html#cfn-cognito-userpooluser-messageaction""", alias="MessageAction")
    ClientMetadata_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluser.html#cfn-cognito-userpooluser-clientmetadata""", alias="ClientMetadata")
    DesiredDeliveryMediums_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluser.html#cfn-cognito-userpooluser-desireddeliverymediums""", alias="DesiredDeliveryMediums")
    ForceAliasCreation_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluser.html#cfn-cognito-userpooluser-forcealiascreation""", alias="ForceAliasCreation")
    UserAttributes_: Optional[List['AttributeType']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluser.html#cfn-cognito-userpooluser-userattributes""", alias="UserAttributes")
    

    @property
    def tropo_type(self) -> troposphere.cognito.UserPoolUser:
        from troposphere.cognito import UserPoolUser as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cognito import UserPoolUser as TropoT
        return resource_to_troposphere(self, TropoT)


class UserPoolUserToGroupAttachment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolusertogroupattachment.html
    Properties:
        - Name: GroupName
        - Name: UserPoolId
        - Name: Username
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    GroupName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolusertogroupattachment.html#cfn-cognito-userpoolusertogroupattachment-groupname""", alias="GroupName")
    UserPoolId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolusertogroupattachment.html#cfn-cognito-userpoolusertogroupattachment-userpoolid""", alias="UserPoolId")
    Username_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolusertogroupattachment.html#cfn-cognito-userpoolusertogroupattachment-username""", alias="Username")
    

    @property
    def tropo_type(self) -> troposphere.cognito.UserPoolUserToGroupAttachment:
        from troposphere.cognito import UserPoolUserToGroupAttachment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cognito import UserPoolUserToGroupAttachment as TropoT
        return resource_to_troposphere(self, TropoT)

