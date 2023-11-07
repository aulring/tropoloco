from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class RobotSoftwareSuite(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-robotapplication-robotsoftwaresuite.html
    Properties:
        - Name: Version
        - Name: Name
    
    """
    
    Version_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-robotapplication-robotsoftwaresuite.html#cfn-robomaker-robotapplication-robotsoftwaresuite-version""", alias="Version")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-robotapplication-robotsoftwaresuite.html#cfn-robomaker-robotapplication-robotsoftwaresuite-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.robomaker.RobotSoftwareSuite:
        from troposphere.robomaker import RobotSoftwareSuite as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SourceConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-robotapplication-sourceconfig.html
    Properties:
        - Name: S3Bucket
        - Name: Architecture
        - Name: S3Key
    
    """
    
    S3Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-robotapplication-sourceconfig.html#cfn-robomaker-robotapplication-sourceconfig-s3bucket""", alias="S3Bucket")
    Architecture_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-robotapplication-sourceconfig.html#cfn-robomaker-robotapplication-sourceconfig-architecture""", alias="Architecture")
    S3Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-robotapplication-sourceconfig.html#cfn-robomaker-robotapplication-sourceconfig-s3key""", alias="S3Key")
    


    @property
    def tropo_type(self) -> troposphere.robomaker.SourceConfig:
        from troposphere.robomaker import SourceConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RenderingEngine(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-renderingengine.html
    Properties:
        - Name: Version
        - Name: Name
    
    """
    
    Version_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-renderingengine.html#cfn-robomaker-simulationapplication-renderingengine-version""", alias="Version")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-renderingengine.html#cfn-robomaker-simulationapplication-renderingengine-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.robomaker.RenderingEngine:
        from troposphere.robomaker import RenderingEngine as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RobotSoftwareSuite(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-robotsoftwaresuite.html
    Properties:
        - Name: Version
        - Name: Name
    
    """
    
    Version_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-robotsoftwaresuite.html#cfn-robomaker-simulationapplication-robotsoftwaresuite-version""", alias="Version")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-robotsoftwaresuite.html#cfn-robomaker-simulationapplication-robotsoftwaresuite-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.robomaker.RobotSoftwareSuite:
        from troposphere.robomaker import RobotSoftwareSuite as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SimulationSoftwareSuite(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-simulationsoftwaresuite.html
    Properties:
        - Name: Version
        - Name: Name
    
    """
    
    Version_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-simulationsoftwaresuite.html#cfn-robomaker-simulationapplication-simulationsoftwaresuite-version""", alias="Version")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-simulationsoftwaresuite.html#cfn-robomaker-simulationapplication-simulationsoftwaresuite-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.robomaker.SimulationSoftwareSuite:
        from troposphere.robomaker import SimulationSoftwareSuite as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SourceConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-sourceconfig.html
    Properties:
        - Name: S3Bucket
        - Name: Architecture
        - Name: S3Key
    
    """
    
    S3Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-sourceconfig.html#cfn-robomaker-simulationapplication-sourceconfig-s3bucket""", alias="S3Bucket")
    Architecture_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-sourceconfig.html#cfn-robomaker-simulationapplication-sourceconfig-architecture""", alias="Architecture")
    S3Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-sourceconfig.html#cfn-robomaker-simulationapplication-sourceconfig-s3key""", alias="S3Key")
    


    @property
    def tropo_type(self) -> troposphere.robomaker.SourceConfig:
        from troposphere.robomaker import SourceConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Fleet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-fleet.html
    Properties:
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-fleet.html#cfn-robomaker-fleet-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-fleet.html#cfn-robomaker-fleet-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.robomaker.Fleet:
        from troposphere.robomaker import Fleet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.robomaker import Fleet as TropoT
        return resource_to_troposphere(self, TropoT)


class Robot(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robot.html
    Properties:
        - Name: Fleet
        - Name: Architecture
        - Name: GreengrassGroupId
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Fleet_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robot.html#cfn-robomaker-robot-fleet""", alias="Fleet")
    Architecture_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robot.html#cfn-robomaker-robot-architecture""", alias="Architecture")
    GreengrassGroupId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robot.html#cfn-robomaker-robot-greengrassgroupid""", alias="GreengrassGroupId")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robot.html#cfn-robomaker-robot-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robot.html#cfn-robomaker-robot-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.robomaker.Robot:
        from troposphere.robomaker import Robot as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.robomaker import Robot as TropoT
        return resource_to_troposphere(self, TropoT)


class RobotApplication(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplication.html
    Properties:
        - Name: CurrentRevisionId
        - Name: Environment
        - Name: RobotSoftwareSuite
        - Name: Sources
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: CurrentRevisionId
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CurrentRevisionId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplication.html#cfn-robomaker-robotapplication-currentrevisionid""", alias="CurrentRevisionId")
    Environment_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplication.html#cfn-robomaker-robotapplication-environment""", alias="Environment")
    RobotSoftwareSuite_: 'RobotSoftwareSuite' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplication.html#cfn-robomaker-robotapplication-robotsoftwaresuite""", alias="RobotSoftwareSuite")
    Sources_: Optional[List['SourceConfig']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplication.html#cfn-robomaker-robotapplication-sources""", alias="Sources")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplication.html#cfn-robomaker-robotapplication-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplication.html#cfn-robomaker-robotapplication-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.robomaker.RobotApplication:
        from troposphere.robomaker import RobotApplication as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.robomaker import RobotApplication as TropoT
        return resource_to_troposphere(self, TropoT)


class RobotApplicationVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplicationversion.html
    Properties:
        - Name: CurrentRevisionId
        - Name: Application
    Attributes:
        - Name: ApplicationVersion
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CurrentRevisionId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplicationversion.html#cfn-robomaker-robotapplicationversion-currentrevisionid""", alias="CurrentRevisionId")
    Application_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplicationversion.html#cfn-robomaker-robotapplicationversion-application""", alias="Application")
    

    @property
    def tropo_type(self) -> troposphere.robomaker.RobotApplicationVersion:
        from troposphere.robomaker import RobotApplicationVersion as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.robomaker import RobotApplicationVersion as TropoT
        return resource_to_troposphere(self, TropoT)


class SimulationApplication(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplication.html
    Properties:
        - Name: RenderingEngine
        - Name: SimulationSoftwareSuite
        - Name: CurrentRevisionId
        - Name: Environment
        - Name: RobotSoftwareSuite
        - Name: Sources
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: CurrentRevisionId
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    RenderingEngine_: Optional['RenderingEngine'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplication.html#cfn-robomaker-simulationapplication-renderingengine""", alias="RenderingEngine")
    SimulationSoftwareSuite_: 'SimulationSoftwareSuite' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplication.html#cfn-robomaker-simulationapplication-simulationsoftwaresuite""", alias="SimulationSoftwareSuite")
    CurrentRevisionId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplication.html#cfn-robomaker-simulationapplication-currentrevisionid""", alias="CurrentRevisionId")
    Environment_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplication.html#cfn-robomaker-simulationapplication-environment""", alias="Environment")
    RobotSoftwareSuite_: 'RobotSoftwareSuite' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplication.html#cfn-robomaker-simulationapplication-robotsoftwaresuite""", alias="RobotSoftwareSuite")
    Sources_: Optional[List['SourceConfig']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplication.html#cfn-robomaker-simulationapplication-sources""", alias="Sources")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplication.html#cfn-robomaker-simulationapplication-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplication.html#cfn-robomaker-simulationapplication-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.robomaker.SimulationApplication:
        from troposphere.robomaker import SimulationApplication as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.robomaker import SimulationApplication as TropoT
        return resource_to_troposphere(self, TropoT)


class SimulationApplicationVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplicationversion.html
    Properties:
        - Name: CurrentRevisionId
        - Name: Application
    Attributes:
        - Name: ApplicationVersion
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CurrentRevisionId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplicationversion.html#cfn-robomaker-simulationapplicationversion-currentrevisionid""", alias="CurrentRevisionId")
    Application_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplicationversion.html#cfn-robomaker-simulationapplicationversion-application""", alias="Application")
    

    @property
    def tropo_type(self) -> troposphere.robomaker.SimulationApplicationVersion:
        from troposphere.robomaker import SimulationApplicationVersion as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.robomaker import SimulationApplicationVersion as TropoT
        return resource_to_troposphere(self, TropoT)

