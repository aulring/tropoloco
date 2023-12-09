from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class RoutingStrategy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-alias-routingstrategy.html
    Properties:
        - Name: Type
        - Name: Message
        - Name: FleetId
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-alias-routingstrategy.html#cfn-gamelift-alias-routingstrategy-type""", alias="Type")
    Message_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-alias-routingstrategy.html#cfn-gamelift-alias-routingstrategy-message""", alias="Message")
    FleetId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-alias-routingstrategy.html#cfn-gamelift-alias-routingstrategy-fleetid""", alias="FleetId")
    


    @property
    def tropo_type(self) -> troposphere.gamelift.RoutingStrategy:
        from troposphere.gamelift import RoutingStrategy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StorageLocation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-build-storagelocation.html
    Properties:
        - Name: ObjectVersion
        - Name: Bucket
        - Name: Key
        - Name: RoleArn
    
    """
    
    ObjectVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-build-storagelocation.html#cfn-gamelift-build-storagelocation-objectversion""", alias="ObjectVersion")
    Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-build-storagelocation.html#cfn-gamelift-build-storagelocation-bucket""", alias="Bucket")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-build-storagelocation.html#cfn-gamelift-build-storagelocation-key""", alias="Key")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-build-storagelocation.html#cfn-gamelift-build-storagelocation-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.gamelift.StorageLocation:
        from troposphere.gamelift import StorageLocation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AnywhereConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-anywhereconfiguration.html
    Properties:
        - Name: Cost
    
    """
    
    Cost_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-anywhereconfiguration.html#cfn-gamelift-fleet-anywhereconfiguration-cost""", alias="Cost")
    


    @property
    def tropo_type(self) -> troposphere.gamelift.AnywhereConfiguration:
        from troposphere.gamelift import AnywhereConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CertificateConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-certificateconfiguration.html
    Properties:
        - Name: CertificateType
    
    """
    
    CertificateType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-certificateconfiguration.html#cfn-gamelift-fleet-certificateconfiguration-certificatetype""", alias="CertificateType")
    


    @property
    def tropo_type(self) -> troposphere.gamelift.CertificateConfiguration:
        from troposphere.gamelift import CertificateConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IpPermission(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-ippermission.html
    Properties:
        - Name: IpRange
        - Name: FromPort
        - Name: ToPort
        - Name: Protocol
    
    """
    
    IpRange_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-ippermission.html#cfn-gamelift-fleet-ippermission-iprange""", alias="IpRange")
    FromPort_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-ippermission.html#cfn-gamelift-fleet-ippermission-fromport""", alias="FromPort")
    ToPort_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-ippermission.html#cfn-gamelift-fleet-ippermission-toport""", alias="ToPort")
    Protocol_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-ippermission.html#cfn-gamelift-fleet-ippermission-protocol""", alias="Protocol")
    


    @property
    def tropo_type(self) -> troposphere.gamelift.IpPermission:
        from troposphere.gamelift import IpPermission as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LocationCapacity(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-locationcapacity.html
    Properties:
        - Name: MinSize
        - Name: DesiredEC2Instances
        - Name: MaxSize
    
    """
    
    MinSize_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-locationcapacity.html#cfn-gamelift-fleet-locationcapacity-minsize""", alias="MinSize")
    DesiredEC2Instances_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-locationcapacity.html#cfn-gamelift-fleet-locationcapacity-desiredec2instances""", alias="DesiredEC2Instances")
    MaxSize_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-locationcapacity.html#cfn-gamelift-fleet-locationcapacity-maxsize""", alias="MaxSize")
    


    @property
    def tropo_type(self) -> troposphere.gamelift.LocationCapacity:
        from troposphere.gamelift import LocationCapacity as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LocationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-locationconfiguration.html
    Properties:
        - Name: LocationCapacity
        - Name: Location
    
    """
    
    LocationCapacity_: Optional['LocationCapacity'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-locationconfiguration.html#cfn-gamelift-fleet-locationconfiguration-locationcapacity""", alias="LocationCapacity")
    Location_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-locationconfiguration.html#cfn-gamelift-fleet-locationconfiguration-location""", alias="Location")
    


    @property
    def tropo_type(self) -> troposphere.gamelift.LocationConfiguration:
        from troposphere.gamelift import LocationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResourceCreationLimitPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-resourcecreationlimitpolicy.html
    Properties:
        - Name: PolicyPeriodInMinutes
        - Name: NewGameSessionsPerCreator
    
    """
    
    PolicyPeriodInMinutes_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-resourcecreationlimitpolicy.html#cfn-gamelift-fleet-resourcecreationlimitpolicy-policyperiodinminutes""", alias="PolicyPeriodInMinutes")
    NewGameSessionsPerCreator_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-resourcecreationlimitpolicy.html#cfn-gamelift-fleet-resourcecreationlimitpolicy-newgamesessionspercreator""", alias="NewGameSessionsPerCreator")
    


    @property
    def tropo_type(self) -> troposphere.gamelift.ResourceCreationLimitPolicy:
        from troposphere.gamelift import ResourceCreationLimitPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RuntimeConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-runtimeconfiguration.html
    Properties:
        - Name: ServerProcesses
        - Name: MaxConcurrentGameSessionActivations
        - Name: GameSessionActivationTimeoutSeconds
    
    """
    
    ServerProcesses_: Optional[List['ServerProcess']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-runtimeconfiguration.html#cfn-gamelift-fleet-runtimeconfiguration-serverprocesses""", alias="ServerProcesses")
    MaxConcurrentGameSessionActivations_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-runtimeconfiguration.html#cfn-gamelift-fleet-runtimeconfiguration-maxconcurrentgamesessionactivations""", alias="MaxConcurrentGameSessionActivations")
    GameSessionActivationTimeoutSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-runtimeconfiguration.html#cfn-gamelift-fleet-runtimeconfiguration-gamesessionactivationtimeoutseconds""", alias="GameSessionActivationTimeoutSeconds")
    


    @property
    def tropo_type(self) -> troposphere.gamelift.RuntimeConfiguration:
        from troposphere.gamelift import RuntimeConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ScalingPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html
    Properties:
        - Name: Status
        - Name: MetricName
        - Name: PolicyType
        - Name: ComparisonOperator
        - Name: TargetConfiguration
        - Name: UpdateStatus
        - Name: ScalingAdjustment
        - Name: EvaluationPeriods
        - Name: Location
        - Name: Name
        - Name: ScalingAdjustmentType
        - Name: Threshold
    
    """
    
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-status""", alias="Status")
    MetricName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-metricname""", alias="MetricName")
    PolicyType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-policytype""", alias="PolicyType")
    ComparisonOperator_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-comparisonoperator""", alias="ComparisonOperator")
    TargetConfiguration_: Optional['TargetConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-targetconfiguration""", alias="TargetConfiguration")
    UpdateStatus_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-updatestatus""", alias="UpdateStatus")
    ScalingAdjustment_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-scalingadjustment""", alias="ScalingAdjustment")
    EvaluationPeriods_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-evaluationperiods""", alias="EvaluationPeriods")
    Location_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-location""", alias="Location")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-name""", alias="Name")
    ScalingAdjustmentType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-scalingadjustmenttype""", alias="ScalingAdjustmentType")
    Threshold_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-threshold""", alias="Threshold")
    


    @property
    def tropo_type(self) -> troposphere.gamelift.ScalingPolicy:
        from troposphere.gamelift import ScalingPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ServerProcess(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-serverprocess.html
    Properties:
        - Name: ConcurrentExecutions
        - Name: Parameters
        - Name: LaunchPath
    
    """
    
    ConcurrentExecutions_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-serverprocess.html#cfn-gamelift-fleet-serverprocess-concurrentexecutions""", alias="ConcurrentExecutions")
    Parameters_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-serverprocess.html#cfn-gamelift-fleet-serverprocess-parameters""", alias="Parameters")
    LaunchPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-serverprocess.html#cfn-gamelift-fleet-serverprocess-launchpath""", alias="LaunchPath")
    


    @property
    def tropo_type(self) -> troposphere.gamelift.ServerProcess:
        from troposphere.gamelift import ServerProcess as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TargetConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-targetconfiguration.html
    Properties:
        - Name: TargetValue
    
    """
    
    TargetValue_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-targetconfiguration.html#cfn-gamelift-fleet-targetconfiguration-targetvalue""", alias="TargetValue")
    


    @property
    def tropo_type(self) -> troposphere.gamelift.TargetConfiguration:
        from troposphere.gamelift import TargetConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AutoScalingPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-autoscalingpolicy.html
    Properties:
        - Name: TargetTrackingConfiguration
        - Name: EstimatedInstanceWarmup
    
    """
    
    TargetTrackingConfiguration_: 'TargetTrackingConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-autoscalingpolicy.html#cfn-gamelift-gameservergroup-autoscalingpolicy-targettrackingconfiguration""", alias="TargetTrackingConfiguration")
    EstimatedInstanceWarmup_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-autoscalingpolicy.html#cfn-gamelift-gameservergroup-autoscalingpolicy-estimatedinstancewarmup""", alias="EstimatedInstanceWarmup")
    


    @property
    def tropo_type(self) -> troposphere.gamelift.AutoScalingPolicy:
        from troposphere.gamelift import AutoScalingPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InstanceDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-instancedefinition.html
    Properties:
        - Name: WeightedCapacity
        - Name: InstanceType
    
    """
    
    WeightedCapacity_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-instancedefinition.html#cfn-gamelift-gameservergroup-instancedefinition-weightedcapacity""", alias="WeightedCapacity")
    InstanceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-instancedefinition.html#cfn-gamelift-gameservergroup-instancedefinition-instancetype""", alias="InstanceType")
    


    @property
    def tropo_type(self) -> troposphere.gamelift.InstanceDefinition:
        from troposphere.gamelift import InstanceDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LaunchTemplate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-launchtemplate.html
    Properties:
        - Name: LaunchTemplateName
        - Name: Version
        - Name: LaunchTemplateId
    
    """
    
    LaunchTemplateName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-launchtemplate.html#cfn-gamelift-gameservergroup-launchtemplate-launchtemplatename""", alias="LaunchTemplateName")
    Version_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-launchtemplate.html#cfn-gamelift-gameservergroup-launchtemplate-version""", alias="Version")
    LaunchTemplateId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-launchtemplate.html#cfn-gamelift-gameservergroup-launchtemplate-launchtemplateid""", alias="LaunchTemplateId")
    


    @property
    def tropo_type(self) -> troposphere.gamelift.LaunchTemplate:
        from troposphere.gamelift import LaunchTemplate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TargetTrackingConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-targettrackingconfiguration.html
    Properties:
        - Name: TargetValue
    
    """
    
    TargetValue_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-targettrackingconfiguration.html#cfn-gamelift-gameservergroup-targettrackingconfiguration-targetvalue""", alias="TargetValue")
    


    @property
    def tropo_type(self) -> troposphere.gamelift.TargetTrackingConfiguration:
        from troposphere.gamelift import TargetTrackingConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FilterConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-filterconfiguration.html
    Properties:
        - Name: AllowedLocations
    
    """
    
    AllowedLocations_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-filterconfiguration.html#cfn-gamelift-gamesessionqueue-filterconfiguration-allowedlocations""", alias="AllowedLocations")
    


    @property
    def tropo_type(self) -> troposphere.gamelift.FilterConfiguration:
        from troposphere.gamelift import FilterConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GameSessionQueueDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-gamesessionqueuedestination.html
    Properties:
        - Name: DestinationArn
    
    """
    
    DestinationArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-gamesessionqueuedestination.html#cfn-gamelift-gamesessionqueue-gamesessionqueuedestination-destinationarn""", alias="DestinationArn")
    


    @property
    def tropo_type(self) -> troposphere.gamelift.GameSessionQueueDestination:
        from troposphere.gamelift import GameSessionQueueDestination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PlayerLatencyPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-playerlatencypolicy.html
    Properties:
        - Name: PolicyDurationSeconds
        - Name: MaximumIndividualPlayerLatencyMilliseconds
    
    """
    
    PolicyDurationSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-playerlatencypolicy.html#cfn-gamelift-gamesessionqueue-playerlatencypolicy-policydurationseconds""", alias="PolicyDurationSeconds")
    MaximumIndividualPlayerLatencyMilliseconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-playerlatencypolicy.html#cfn-gamelift-gamesessionqueue-playerlatencypolicy-maximumindividualplayerlatencymilliseconds""", alias="MaximumIndividualPlayerLatencyMilliseconds")
    


    @property
    def tropo_type(self) -> troposphere.gamelift.PlayerLatencyPolicy:
        from troposphere.gamelift import PlayerLatencyPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PriorityConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-priorityconfiguration.html
    Properties:
        - Name: PriorityOrder
        - Name: LocationOrder
    
    """
    
    PriorityOrder_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-priorityconfiguration.html#cfn-gamelift-gamesessionqueue-priorityconfiguration-priorityorder""", alias="PriorityOrder")
    LocationOrder_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-priorityconfiguration.html#cfn-gamelift-gamesessionqueue-priorityconfiguration-locationorder""", alias="LocationOrder")
    


    @property
    def tropo_type(self) -> troposphere.gamelift.PriorityConfiguration:
        from troposphere.gamelift import PriorityConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GameProperty(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-matchmakingconfiguration-gameproperty.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-matchmakingconfiguration-gameproperty.html#cfn-gamelift-matchmakingconfiguration-gameproperty-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-matchmakingconfiguration-gameproperty.html#cfn-gamelift-matchmakingconfiguration-gameproperty-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.gamelift.GameProperty:
        from troposphere.gamelift import GameProperty as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Location(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-script-s3location.html
    Properties:
        - Name: ObjectVersion
        - Name: Bucket
        - Name: Key
        - Name: RoleArn
    
    """
    
    ObjectVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-script-s3location.html#cfn-gamelift-script-s3location-objectversion""", alias="ObjectVersion")
    Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-script-s3location.html#cfn-gamelift-script-s3location-bucket""", alias="Bucket")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-script-s3location.html#cfn-gamelift-script-s3location-key""", alias="Key")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-script-s3location.html#cfn-gamelift-script-s3location-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.gamelift.S3Location:
        from troposphere.gamelift import S3Location as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Alias(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-alias.html
    Properties:
        - Name: Description
        - Name: RoutingStrategy
        - Name: Name
    Attributes:
        - Name: AliasId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-alias.html#cfn-gamelift-alias-description""", alias="Description")
    RoutingStrategy_: 'RoutingStrategy' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-alias.html#cfn-gamelift-alias-routingstrategy""", alias="RoutingStrategy")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-alias.html#cfn-gamelift-alias-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.gamelift.Alias:
        from troposphere.gamelift import Alias as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.gamelift import Alias as TropoT
        return resource_to_troposphere(self, TropoT)


class Build(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html
    Properties:
        - Name: OperatingSystem
        - Name: Version
        - Name: ServerSdkVersion
        - Name: StorageLocation
        - Name: Name
    Attributes:
        - Name: BuildId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    OperatingSystem_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html#cfn-gamelift-build-operatingsystem""", alias="OperatingSystem")
    Version_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html#cfn-gamelift-build-version""", alias="Version")
    ServerSdkVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html#cfn-gamelift-build-serversdkversion""", alias="ServerSdkVersion")
    StorageLocation_: Optional['StorageLocation'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html#cfn-gamelift-build-storagelocation""", alias="StorageLocation")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html#cfn-gamelift-build-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.gamelift.Build:
        from troposphere.gamelift import Build as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.gamelift import Build as TropoT
        return resource_to_troposphere(self, TropoT)


class Fleet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html
    Properties:
        - Name: ScalingPolicies
        - Name: Description
        - Name: PeerVpcId
        - Name: FleetType
        - Name: EC2InboundPermissions
        - Name: Locations
        - Name: NewGameSessionProtectionPolicy
        - Name: ScriptId
        - Name: ComputeType
        - Name: MaxSize
        - Name: RuntimeConfiguration
        - Name: Name
        - Name: MinSize
        - Name: PeerVpcAwsAccountId
        - Name: AnywhereConfiguration
        - Name: InstanceRoleARN
        - Name: MetricGroups
        - Name: BuildId
        - Name: ResourceCreationLimitPolicy
        - Name: EC2InstanceType
        - Name: CertificateConfiguration
        - Name: InstanceRoleCredentialsProvider
        - Name: DesiredEC2Instances
    Attributes:
        - Name: FleetId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ScalingPolicies_: Optional[List['ScalingPolicy']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-scalingpolicies""", alias="ScalingPolicies")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-description""", alias="Description")
    PeerVpcId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-peervpcid""", alias="PeerVpcId")
    FleetType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-fleettype""", alias="FleetType")
    EC2InboundPermissions_: Optional[List['IpPermission']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-ec2inboundpermissions""", alias="EC2InboundPermissions")
    Locations_: Optional[List['LocationConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-locations""", alias="Locations")
    NewGameSessionProtectionPolicy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-newgamesessionprotectionpolicy""", alias="NewGameSessionProtectionPolicy")
    ScriptId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-scriptid""", alias="ScriptId")
    ComputeType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-computetype""", alias="ComputeType")
    MaxSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-maxsize""", alias="MaxSize")
    RuntimeConfiguration_: Optional['RuntimeConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-runtimeconfiguration""", alias="RuntimeConfiguration")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-name""", alias="Name")
    MinSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-minsize""", alias="MinSize")
    PeerVpcAwsAccountId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-peervpcawsaccountid""", alias="PeerVpcAwsAccountId")
    AnywhereConfiguration_: Optional['AnywhereConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-anywhereconfiguration""", alias="AnywhereConfiguration")
    InstanceRoleARN_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-instancerolearn""", alias="InstanceRoleARN")
    MetricGroups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-metricgroups""", alias="MetricGroups")
    BuildId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-buildid""", alias="BuildId")
    ResourceCreationLimitPolicy_: Optional['ResourceCreationLimitPolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-resourcecreationlimitpolicy""", alias="ResourceCreationLimitPolicy")
    EC2InstanceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-ec2instancetype""", alias="EC2InstanceType")
    CertificateConfiguration_: Optional['CertificateConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-certificateconfiguration""", alias="CertificateConfiguration")
    InstanceRoleCredentialsProvider_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-instancerolecredentialsprovider""", alias="InstanceRoleCredentialsProvider")
    DesiredEC2Instances_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-desiredec2instances""", alias="DesiredEC2Instances")
    

    @property
    def tropo_type(self) -> troposphere.gamelift.Fleet:
        from troposphere.gamelift import Fleet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.gamelift import Fleet as TropoT
        return resource_to_troposphere(self, TropoT)


class GameServerGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html
    Properties:
        - Name: AutoScalingPolicy
        - Name: MinSize
        - Name: DeleteOption
        - Name: BalancingStrategy
        - Name: GameServerGroupName
        - Name: LaunchTemplate
        - Name: GameServerProtectionPolicy
        - Name: VpcSubnets
        - Name: MaxSize
        - Name: InstanceDefinitions
        - Name: RoleArn
        - Name: Tags
    Attributes:
        - Name: AutoScalingGroupArn
        - Name: GameServerGroupArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AutoScalingPolicy_: Optional['AutoScalingPolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-autoscalingpolicy""", alias="AutoScalingPolicy")
    MinSize_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-minsize""", alias="MinSize")
    DeleteOption_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-deleteoption""", alias="DeleteOption")
    BalancingStrategy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-balancingstrategy""", alias="BalancingStrategy")
    GameServerGroupName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-gameservergroupname""", alias="GameServerGroupName")
    LaunchTemplate_: Optional['LaunchTemplate'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-launchtemplate""", alias="LaunchTemplate")
    GameServerProtectionPolicy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-gameserverprotectionpolicy""", alias="GameServerProtectionPolicy")
    VpcSubnets_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-vpcsubnets""", alias="VpcSubnets")
    MaxSize_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-maxsize""", alias="MaxSize")
    InstanceDefinitions_: List['InstanceDefinition'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-instancedefinitions""", alias="InstanceDefinitions")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-rolearn""", alias="RoleArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.gamelift.GameServerGroup:
        from troposphere.gamelift import GameServerGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.gamelift import GameServerGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class GameSessionQueue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html
    Properties:
        - Name: TimeoutInSeconds
        - Name: PlayerLatencyPolicies
        - Name: Destinations
        - Name: NotificationTarget
        - Name: FilterConfiguration
        - Name: CustomEventData
        - Name: Tags
        - Name: Name
        - Name: PriorityConfiguration
    Attributes:
        - Name: Arn
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TimeoutInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-timeoutinseconds""", alias="TimeoutInSeconds")
    PlayerLatencyPolicies_: Optional[List['PlayerLatencyPolicy']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-playerlatencypolicies""", alias="PlayerLatencyPolicies")
    Destinations_: Optional[List['GameSessionQueueDestination']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-destinations""", alias="Destinations")
    NotificationTarget_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-notificationtarget""", alias="NotificationTarget")
    FilterConfiguration_: Optional['FilterConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-filterconfiguration""", alias="FilterConfiguration")
    CustomEventData_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-customeventdata""", alias="CustomEventData")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-name""", alias="Name")
    PriorityConfiguration_: Optional['PriorityConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-priorityconfiguration""", alias="PriorityConfiguration")
    

    @property
    def tropo_type(self) -> troposphere.gamelift.GameSessionQueue:
        from troposphere.gamelift import GameSessionQueue as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.gamelift import GameSessionQueue as TropoT
        return resource_to_troposphere(self, TropoT)


class Location(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-location.html
    Properties:
        - Name: Tags
        - Name: LocationName
    Attributes:
        - Name: LocationArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-location.html#cfn-gamelift-location-tags""", alias="Tags")
    LocationName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-location.html#cfn-gamelift-location-locationname""", alias="LocationName")
    

    @property
    def tropo_type(self) -> troposphere.gamelift.Location:
        from troposphere.gamelift import Location as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.gamelift import Location as TropoT
        return resource_to_troposphere(self, TropoT)


class MatchmakingConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html
    Properties:
        - Name: GameProperties
        - Name: GameSessionData
        - Name: Description
        - Name: AcceptanceTimeoutSeconds
        - Name: NotificationTarget
        - Name: CustomEventData
        - Name: Name
        - Name: AdditionalPlayerCount
        - Name: BackfillMode
        - Name: RequestTimeoutSeconds
        - Name: AcceptanceRequired
        - Name: CreationTime
        - Name: FlexMatchMode
        - Name: RuleSetName
        - Name: GameSessionQueueArns
        - Name: Tags
        - Name: RuleSetArn
    Attributes:
        - Name: Arn
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    GameProperties_: Optional[List['GameProperty']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-gameproperties""", alias="GameProperties")
    GameSessionData_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-gamesessiondata""", alias="GameSessionData")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-description""", alias="Description")
    AcceptanceTimeoutSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-acceptancetimeoutseconds""", alias="AcceptanceTimeoutSeconds")
    NotificationTarget_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-notificationtarget""", alias="NotificationTarget")
    CustomEventData_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-customeventdata""", alias="CustomEventData")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-name""", alias="Name")
    AdditionalPlayerCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-additionalplayercount""", alias="AdditionalPlayerCount")
    BackfillMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-backfillmode""", alias="BackfillMode")
    RequestTimeoutSeconds_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-requesttimeoutseconds""", alias="RequestTimeoutSeconds")
    AcceptanceRequired_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-acceptancerequired""", alias="AcceptanceRequired")
    CreationTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-creationtime""", alias="CreationTime")
    FlexMatchMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-flexmatchmode""", alias="FlexMatchMode")
    RuleSetName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-rulesetname""", alias="RuleSetName")
    GameSessionQueueArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-gamesessionqueuearns""", alias="GameSessionQueueArns")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-tags""", alias="Tags")
    RuleSetArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-rulesetarn""", alias="RuleSetArn")
    

    @property
    def tropo_type(self) -> troposphere.gamelift.MatchmakingConfiguration:
        from troposphere.gamelift import MatchmakingConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.gamelift import MatchmakingConfiguration as TropoT
        return resource_to_troposphere(self, TropoT)


class MatchmakingRuleSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingruleset.html
    Properties:
        - Name: RuleSetBody
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: CreationTime
        - Name: Arn
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    RuleSetBody_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingruleset.html#cfn-gamelift-matchmakingruleset-rulesetbody""", alias="RuleSetBody")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingruleset.html#cfn-gamelift-matchmakingruleset-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingruleset.html#cfn-gamelift-matchmakingruleset-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.gamelift.MatchmakingRuleSet:
        from troposphere.gamelift import MatchmakingRuleSet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.gamelift import MatchmakingRuleSet as TropoT
        return resource_to_troposphere(self, TropoT)


class Script(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-script.html
    Properties:
        - Name: Version
        - Name: StorageLocation
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: CreationTime
        - Name: Id
        - Name: Arn
        - Name: SizeOnDisk
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Version_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-script.html#cfn-gamelift-script-version""", alias="Version")
    StorageLocation_: 'S3Location' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-script.html#cfn-gamelift-script-storagelocation""", alias="StorageLocation")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-script.html#cfn-gamelift-script-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-script.html#cfn-gamelift-script-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.gamelift.Script:
        from troposphere.gamelift import Script as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.gamelift import Script as TropoT
        return resource_to_troposphere(self, TropoT)

