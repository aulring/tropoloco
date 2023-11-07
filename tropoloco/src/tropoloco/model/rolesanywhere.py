from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class NotificationSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rolesanywhere-trustanchor-notificationsetting.html
    Properties:
        - Name: Channel
        - Name: Enabled
        - Name: Event
        - Name: Threshold
    
    """
    
    Channel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rolesanywhere-trustanchor-notificationsetting.html#cfn-rolesanywhere-trustanchor-notificationsetting-channel""", alias="Channel")
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rolesanywhere-trustanchor-notificationsetting.html#cfn-rolesanywhere-trustanchor-notificationsetting-enabled""", alias="Enabled")
    Event_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rolesanywhere-trustanchor-notificationsetting.html#cfn-rolesanywhere-trustanchor-notificationsetting-event""", alias="Event")
    Threshold_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rolesanywhere-trustanchor-notificationsetting.html#cfn-rolesanywhere-trustanchor-notificationsetting-threshold""", alias="Threshold")
    


    @property
    def tropo_type(self) -> troposphere.rolesanywhere.NotificationSetting:
        from troposphere.rolesanywhere import NotificationSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Source(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rolesanywhere-trustanchor-source.html
    Properties:
        - Name: SourceType
        - Name: SourceData
    
    """
    
    SourceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rolesanywhere-trustanchor-source.html#cfn-rolesanywhere-trustanchor-source-sourcetype""", alias="SourceType")
    SourceData_: Optional['SourceData'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rolesanywhere-trustanchor-source.html#cfn-rolesanywhere-trustanchor-source-sourcedata""", alias="SourceData")
    


    @property
    def tropo_type(self) -> troposphere.rolesanywhere.Source:
        from troposphere.rolesanywhere import Source as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SourceData(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rolesanywhere-trustanchor-sourcedata.html
    Properties:
        - Name: AcmPcaArn
        - Name: X509CertificateData
    
    """
    
    AcmPcaArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rolesanywhere-trustanchor-sourcedata.html#cfn-rolesanywhere-trustanchor-sourcedata-acmpcaarn""", alias="AcmPcaArn")
    X509CertificateData_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rolesanywhere-trustanchor-sourcedata.html#cfn-rolesanywhere-trustanchor-sourcedata-x509certificatedata""", alias="X509CertificateData")
    


    @property
    def tropo_type(self) -> troposphere.rolesanywhere.SourceData:
        from troposphere.rolesanywhere import SourceData as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class CRL(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-crl.html
    Properties:
        - Name: TrustAnchorArn
        - Name: Enabled
        - Name: CrlData
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: CrlId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TrustAnchorArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-crl.html#cfn-rolesanywhere-crl-trustanchorarn""", alias="TrustAnchorArn")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-crl.html#cfn-rolesanywhere-crl-enabled""", alias="Enabled")
    CrlData_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-crl.html#cfn-rolesanywhere-crl-crldata""", alias="CrlData")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-crl.html#cfn-rolesanywhere-crl-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-crl.html#cfn-rolesanywhere-crl-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.rolesanywhere.CRL:
        from troposphere.rolesanywhere import CRL as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.rolesanywhere import CRL as TropoT
        return resource_to_troposphere(self, TropoT)


class Profile(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-profile.html
    Properties:
        - Name: ManagedPolicyArns
        - Name: RequireInstanceProperties
        - Name: RoleArns
        - Name: SessionPolicy
        - Name: Enabled
        - Name: DurationSeconds
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: ProfileId
        - Name: ProfileArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ManagedPolicyArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-profile.html#cfn-rolesanywhere-profile-managedpolicyarns""", alias="ManagedPolicyArns")
    RequireInstanceProperties_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-profile.html#cfn-rolesanywhere-profile-requireinstanceproperties""", alias="RequireInstanceProperties")
    RoleArns_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-profile.html#cfn-rolesanywhere-profile-rolearns""", alias="RoleArns")
    SessionPolicy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-profile.html#cfn-rolesanywhere-profile-sessionpolicy""", alias="SessionPolicy")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-profile.html#cfn-rolesanywhere-profile-enabled""", alias="Enabled")
    DurationSeconds_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-profile.html#cfn-rolesanywhere-profile-durationseconds""", alias="DurationSeconds")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-profile.html#cfn-rolesanywhere-profile-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-profile.html#cfn-rolesanywhere-profile-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.rolesanywhere.Profile:
        from troposphere.rolesanywhere import Profile as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.rolesanywhere import Profile as TropoT
        return resource_to_troposphere(self, TropoT)


class TrustAnchor(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-trustanchor.html
    Properties:
        - Name: NotificationSettings
        - Name: Enabled
        - Name: Source
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: TrustAnchorArn
        - Name: TrustAnchorId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    NotificationSettings_: Optional[List['NotificationSetting']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-trustanchor.html#cfn-rolesanywhere-trustanchor-notificationsettings""", alias="NotificationSettings")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-trustanchor.html#cfn-rolesanywhere-trustanchor-enabled""", alias="Enabled")
    Source_: 'Source' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-trustanchor.html#cfn-rolesanywhere-trustanchor-source""", alias="Source")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-trustanchor.html#cfn-rolesanywhere-trustanchor-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-trustanchor.html#cfn-rolesanywhere-trustanchor-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.rolesanywhere.TrustAnchor:
        from troposphere.rolesanywhere import TrustAnchor as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.rolesanywhere import TrustAnchor as TropoT
        return resource_to_troposphere(self, TropoT)

