from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class MapConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-location-map-mapconfiguration.html
    Properties:
        - Name: Style
    
    """
    
    Style_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-location-map-mapconfiguration.html#cfn-location-map-mapconfiguration-style""", alias="Style")
    


    @property
    def tropo_type(self) -> troposphere.location.MapConfiguration:
        from troposphere.location import MapConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataSourceConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-location-placeindex-datasourceconfiguration.html
    Properties:
        - Name: IntendedUse
    
    """
    
    IntendedUse_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-location-placeindex-datasourceconfiguration.html#cfn-location-placeindex-datasourceconfiguration-intendeduse""", alias="IntendedUse")
    


    @property
    def tropo_type(self) -> troposphere.location.DataSourceConfiguration:
        from troposphere.location import DataSourceConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class GeofenceCollection(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html
    Properties:
        - Name: Description
        - Name: KmsKeyId
        - Name: CollectionName
    Attributes:
        - Name: CollectionArn
        - Name: CreateTime
        - Name: UpdateTime
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html#cfn-location-geofencecollection-description""", alias="Description")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html#cfn-location-geofencecollection-kmskeyid""", alias="KmsKeyId")
    CollectionName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html#cfn-location-geofencecollection-collectionname""", alias="CollectionName")
    

    @property
    def tropo_type(self) -> troposphere.location.GeofenceCollection:
        from troposphere.location import GeofenceCollection as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.location import GeofenceCollection as TropoT
        return resource_to_troposphere(self, TropoT)


class Map(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html
    Properties:
        - Name: MapName
        - Name: Description
        - Name: Configuration
        - Name: PricingPlan
    Attributes:
        - Name: CreateTime
        - Name: UpdateTime
        - Name: Arn
        - Name: MapArn
        - Name: DataSource
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MapName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html#cfn-location-map-mapname""", alias="MapName")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html#cfn-location-map-description""", alias="Description")
    Configuration_: 'MapConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html#cfn-location-map-configuration""", alias="Configuration")
    PricingPlan_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html#cfn-location-map-pricingplan""", alias="PricingPlan")
    

    @property
    def tropo_type(self) -> troposphere.location.Map:
        from troposphere.location import Map as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.location import Map as TropoT
        return resource_to_troposphere(self, TropoT)


class PlaceIndex(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html
    Properties:
        - Name: IndexName
        - Name: Description
        - Name: PricingPlan
        - Name: DataSourceConfiguration
        - Name: DataSource
    Attributes:
        - Name: IndexArn
        - Name: CreateTime
        - Name: UpdateTime
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    IndexName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#cfn-location-placeindex-indexname""", alias="IndexName")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#cfn-location-placeindex-description""", alias="Description")
    PricingPlan_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#cfn-location-placeindex-pricingplan""", alias="PricingPlan")
    DataSourceConfiguration_: Optional['DataSourceConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#cfn-location-placeindex-datasourceconfiguration""", alias="DataSourceConfiguration")
    DataSource_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#cfn-location-placeindex-datasource""", alias="DataSource")
    

    @property
    def tropo_type(self) -> troposphere.location.PlaceIndex:
        from troposphere.location import PlaceIndex as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.location import PlaceIndex as TropoT
        return resource_to_troposphere(self, TropoT)


class RouteCalculator(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html
    Properties:
        - Name: CalculatorName
        - Name: Description
        - Name: PricingPlan
        - Name: DataSource
    Attributes:
        - Name: CreateTime
        - Name: UpdateTime
        - Name: CalculatorArn
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CalculatorName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#cfn-location-routecalculator-calculatorname""", alias="CalculatorName")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#cfn-location-routecalculator-description""", alias="Description")
    PricingPlan_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#cfn-location-routecalculator-pricingplan""", alias="PricingPlan")
    DataSource_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#cfn-location-routecalculator-datasource""", alias="DataSource")
    

    @property
    def tropo_type(self) -> troposphere.location.RouteCalculator:
        from troposphere.location import RouteCalculator as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.location import RouteCalculator as TropoT
        return resource_to_troposphere(self, TropoT)


class Tracker(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html
    Properties:
        - Name: TrackerName
        - Name: Description
        - Name: KmsKeyId
        - Name: PositionFiltering
    Attributes:
        - Name: CreateTime
        - Name: UpdateTime
        - Name: Arn
        - Name: TrackerArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TrackerName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#cfn-location-tracker-trackername""", alias="TrackerName")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#cfn-location-tracker-description""", alias="Description")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#cfn-location-tracker-kmskeyid""", alias="KmsKeyId")
    PositionFiltering_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#cfn-location-tracker-positionfiltering""", alias="PositionFiltering")
    

    @property
    def tropo_type(self) -> troposphere.location.Tracker:
        from troposphere.location import Tracker as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.location import Tracker as TropoT
        return resource_to_troposphere(self, TropoT)


class TrackerConsumer(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-trackerconsumer.html
    Properties:
        - Name: TrackerName
        - Name: ConsumerArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TrackerName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-trackerconsumer.html#cfn-location-trackerconsumer-trackername""", alias="TrackerName")
    ConsumerArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-trackerconsumer.html#cfn-location-trackerconsumer-consumerarn""", alias="ConsumerArn")
    

    @property
    def tropo_type(self) -> troposphere.location.TrackerConsumer:
        from troposphere.location import TrackerConsumer as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.location import TrackerConsumer as TropoT
        return resource_to_troposphere(self, TropoT)

