from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class BoundingBox(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-boundingbox.html
    Properties:
        - Name: Left
        - Name: Top
        - Name: Height
        - Name: Width
    
    """
    
    Left_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-boundingbox.html#cfn-rekognition-streamprocessor-boundingbox-left""", alias="Left")
    Top_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-boundingbox.html#cfn-rekognition-streamprocessor-boundingbox-top""", alias="Top")
    Height_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-boundingbox.html#cfn-rekognition-streamprocessor-boundingbox-height""", alias="Height")
    Width_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-boundingbox.html#cfn-rekognition-streamprocessor-boundingbox-width""", alias="Width")
    


    @property
    def tropo_type(self) -> troposphere.rekognition.BoundingBox:
        from troposphere.rekognition import BoundingBox as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConnectedHomeSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-connectedhomesettings.html
    Properties:
        - Name: MinConfidence
        - Name: Labels
    
    """
    
    MinConfidence_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-connectedhomesettings.html#cfn-rekognition-streamprocessor-connectedhomesettings-minconfidence""", alias="MinConfidence")
    Labels_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-connectedhomesettings.html#cfn-rekognition-streamprocessor-connectedhomesettings-labels""", alias="Labels")
    


    @property
    def tropo_type(self) -> troposphere.rekognition.ConnectedHomeSettings:
        from troposphere.rekognition import ConnectedHomeSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataSharingPreference(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-datasharingpreference.html
    Properties:
        - Name: OptIn
    
    """
    
    OptIn_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-datasharingpreference.html#cfn-rekognition-streamprocessor-datasharingpreference-optin""", alias="OptIn")
    


    @property
    def tropo_type(self) -> troposphere.rekognition.DataSharingPreference:
        from troposphere.rekognition import DataSharingPreference as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FaceSearchSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-facesearchsettings.html
    Properties:
        - Name: CollectionId
        - Name: FaceMatchThreshold
    
    """
    
    CollectionId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-facesearchsettings.html#cfn-rekognition-streamprocessor-facesearchsettings-collectionid""", alias="CollectionId")
    FaceMatchThreshold_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-facesearchsettings.html#cfn-rekognition-streamprocessor-facesearchsettings-facematchthreshold""", alias="FaceMatchThreshold")
    


    @property
    def tropo_type(self) -> troposphere.rekognition.FaceSearchSettings:
        from troposphere.rekognition import FaceSearchSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KinesisDataStream(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-kinesisdatastream.html
    Properties:
        - Name: Arn
    
    """
    
    Arn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-kinesisdatastream.html#cfn-rekognition-streamprocessor-kinesisdatastream-arn""", alias="Arn")
    


    @property
    def tropo_type(self) -> troposphere.rekognition.KinesisDataStream:
        from troposphere.rekognition import KinesisDataStream as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KinesisVideoStream(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-kinesisvideostream.html
    Properties:
        - Name: Arn
    
    """
    
    Arn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-kinesisvideostream.html#cfn-rekognition-streamprocessor-kinesisvideostream-arn""", alias="Arn")
    


    @property
    def tropo_type(self) -> troposphere.rekognition.KinesisVideoStream:
        from troposphere.rekognition import KinesisVideoStream as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NotificationChannel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-notificationchannel.html
    Properties:
        - Name: Arn
    
    """
    
    Arn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-notificationchannel.html#cfn-rekognition-streamprocessor-notificationchannel-arn""", alias="Arn")
    


    @property
    def tropo_type(self) -> troposphere.rekognition.NotificationChannel:
        from troposphere.rekognition import NotificationChannel as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Destination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-s3destination.html
    Properties:
        - Name: BucketName
        - Name: ObjectKeyPrefix
    
    """
    
    BucketName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-s3destination.html#cfn-rekognition-streamprocessor-s3destination-bucketname""", alias="BucketName")
    ObjectKeyPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-s3destination.html#cfn-rekognition-streamprocessor-s3destination-objectkeyprefix""", alias="ObjectKeyPrefix")
    


    @property
    def tropo_type(self) -> troposphere.rekognition.S3Destination:
        from troposphere.rekognition import S3Destination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Collection(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-collection.html
    Properties:
        - Name: CollectionId
        - Name: Tags
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CollectionId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-collection.html#cfn-rekognition-collection-collectionid""", alias="CollectionId")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-collection.html#cfn-rekognition-collection-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.rekognition.Collection:
        from troposphere.rekognition import Collection as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.rekognition import Collection as TropoT
        return resource_to_troposphere(self, TropoT)


class Project(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-project.html
    Properties:
        - Name: ProjectName
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ProjectName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-project.html#cfn-rekognition-project-projectname""", alias="ProjectName")
    

    @property
    def tropo_type(self) -> troposphere.rekognition.Project:
        from troposphere.rekognition import Project as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.rekognition import Project as TropoT
        return resource_to_troposphere(self, TropoT)


class StreamProcessor(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html
    Properties:
        - Name: S3Destination
        - Name: DataSharingPreference
        - Name: KmsKeyId
        - Name: FaceSearchSettings
        - Name: PolygonRegionsOfInterest
        - Name: RoleArn
        - Name: Name
        - Name: ConnectedHomeSettings
        - Name: NotificationChannel
        - Name: KinesisVideoStream
        - Name: BoundingBoxRegionsOfInterest
        - Name: KinesisDataStream
        - Name: Tags
    Attributes:
        - Name: Status
        - Name: Arn
        - Name: StatusMessage
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    S3Destination_: Optional['S3Destination'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-s3destination""", alias="S3Destination")
    DataSharingPreference_: Optional['DataSharingPreference'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-datasharingpreference""", alias="DataSharingPreference")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-kmskeyid""", alias="KmsKeyId")
    FaceSearchSettings_: Optional['FaceSearchSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-facesearchsettings""", alias="FaceSearchSettings")
    PolygonRegionsOfInterest_: Optional[List[List[Dict[str, float]]]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-polygonregionsofinterest""", alias="PolygonRegionsOfInterest")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-rolearn""", alias="RoleArn")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-name""", alias="Name")
    ConnectedHomeSettings_: Optional['ConnectedHomeSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-connectedhomesettings""", alias="ConnectedHomeSettings")
    NotificationChannel_: Optional['NotificationChannel'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-notificationchannel""", alias="NotificationChannel")
    KinesisVideoStream_: 'KinesisVideoStream' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-kinesisvideostream""", alias="KinesisVideoStream")
    BoundingBoxRegionsOfInterest_: Optional[List['BoundingBox']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-boundingboxregionsofinterest""", alias="BoundingBoxRegionsOfInterest")
    KinesisDataStream_: Optional['KinesisDataStream'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-kinesisdatastream""", alias="KinesisDataStream")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.rekognition.StreamProcessor:
        from troposphere.rekognition import StreamProcessor as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.rekognition import StreamProcessor as TropoT
        return resource_to_troposphere(self, TropoT)

