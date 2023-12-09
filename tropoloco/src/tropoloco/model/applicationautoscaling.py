from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class ScalableTargetAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scalabletargetaction.html
    Properties:
        - Name: MinCapacity
        - Name: MaxCapacity
    
    """
    
    MinCapacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scalabletargetaction.html#cfn-applicationautoscaling-scalabletarget-scalabletargetaction-mincapacity""", alias="MinCapacity")
    MaxCapacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scalabletargetaction.html#cfn-applicationautoscaling-scalabletarget-scalabletargetaction-maxcapacity""", alias="MaxCapacity")
    


    @property
    def tropo_type(self) -> troposphere.applicationautoscaling.ScalableTargetAction:
        from troposphere.applicationautoscaling import ScalableTargetAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ScheduledAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html
    Properties:
        - Name: Timezone
        - Name: ScheduledActionName
        - Name: EndTime
        - Name: Schedule
        - Name: StartTime
        - Name: ScalableTargetAction
    
    """
    
    Timezone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-timezone""", alias="Timezone")
    ScheduledActionName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-scheduledactionname""", alias="ScheduledActionName")
    EndTime_: Optional[datetime.datetime] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-endtime""", alias="EndTime")
    Schedule_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-schedule""", alias="Schedule")
    StartTime_: Optional[datetime.datetime] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-starttime""", alias="StartTime")
    ScalableTargetAction_: Optional['ScalableTargetAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-scalabletargetaction""", alias="ScalableTargetAction")
    


    @property
    def tropo_type(self) -> troposphere.applicationautoscaling.ScheduledAction:
        from troposphere.applicationautoscaling import ScheduledAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SuspendedState(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-suspendedstate.html
    Properties:
        - Name: DynamicScalingOutSuspended
        - Name: ScheduledScalingSuspended
        - Name: DynamicScalingInSuspended
    
    """
    
    DynamicScalingOutSuspended_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-suspendedstate.html#cfn-applicationautoscaling-scalabletarget-suspendedstate-dynamicscalingoutsuspended""", alias="DynamicScalingOutSuspended")
    ScheduledScalingSuspended_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-suspendedstate.html#cfn-applicationautoscaling-scalabletarget-suspendedstate-scheduledscalingsuspended""", alias="ScheduledScalingSuspended")
    DynamicScalingInSuspended_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-suspendedstate.html#cfn-applicationautoscaling-scalabletarget-suspendedstate-dynamicscalinginsuspended""", alias="DynamicScalingInSuspended")
    


    @property
    def tropo_type(self) -> troposphere.applicationautoscaling.SuspendedState:
        from troposphere.applicationautoscaling import SuspendedState as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomizedMetricSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html
    Properties:
        - Name: MetricName
        - Name: Metrics
        - Name: Statistic
        - Name: Dimensions
        - Name: Unit
        - Name: Namespace
    
    """
    
    MetricName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-metricname""", alias="MetricName")
    Metrics_: Optional[List['TargetTrackingMetricDataQuery']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-metrics""", alias="Metrics")
    Statistic_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-statistic""", alias="Statistic")
    Dimensions_: Optional[List['MetricDimension']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-dimensions""", alias="Dimensions")
    Unit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-unit""", alias="Unit")
    Namespace_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-namespace""", alias="Namespace")
    


    @property
    def tropo_type(self) -> troposphere.applicationautoscaling.CustomizedMetricSpecification:
        from troposphere.applicationautoscaling import CustomizedMetricSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetricDimension(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-metricdimension.html
    Properties:
        - Name: Value
        - Name: Name
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-metricdimension.html#cfn-applicationautoscaling-scalingpolicy-metricdimension-value""", alias="Value")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-metricdimension.html#cfn-applicationautoscaling-scalingpolicy-metricdimension-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.applicationautoscaling.MetricDimension:
        from troposphere.applicationautoscaling import MetricDimension as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PredefinedMetricSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-predefinedmetricspecification.html
    Properties:
        - Name: PredefinedMetricType
        - Name: ResourceLabel
    
    """
    
    PredefinedMetricType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-predefinedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-predefinedmetricspecification-predefinedmetrictype""", alias="PredefinedMetricType")
    ResourceLabel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-predefinedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-predefinedmetricspecification-resourcelabel""", alias="ResourceLabel")
    


    @property
    def tropo_type(self) -> troposphere.applicationautoscaling.PredefinedMetricSpecification:
        from troposphere.applicationautoscaling import PredefinedMetricSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StepAdjustment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepadjustment.html
    Properties:
        - Name: MetricIntervalUpperBound
        - Name: MetricIntervalLowerBound
        - Name: ScalingAdjustment
    
    """
    
    MetricIntervalUpperBound_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepadjustment.html#cfn-applicationautoscaling-scalingpolicy-stepadjustment-metricintervalupperbound""", alias="MetricIntervalUpperBound")
    MetricIntervalLowerBound_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepadjustment.html#cfn-applicationautoscaling-scalingpolicy-stepadjustment-metricintervallowerbound""", alias="MetricIntervalLowerBound")
    ScalingAdjustment_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepadjustment.html#cfn-applicationautoscaling-scalingpolicy-stepadjustment-scalingadjustment""", alias="ScalingAdjustment")
    


    @property
    def tropo_type(self) -> troposphere.applicationautoscaling.StepAdjustment:
        from troposphere.applicationautoscaling import StepAdjustment as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StepScalingPolicyConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html
    Properties:
        - Name: MetricAggregationType
        - Name: Cooldown
        - Name: StepAdjustments
        - Name: MinAdjustmentMagnitude
        - Name: AdjustmentType
    
    """
    
    MetricAggregationType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-metricaggregationtype""", alias="MetricAggregationType")
    Cooldown_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-cooldown""", alias="Cooldown")
    StepAdjustments_: Optional[List['StepAdjustment']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustments""", alias="StepAdjustments")
    MinAdjustmentMagnitude_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-minadjustmentmagnitude""", alias="MinAdjustmentMagnitude")
    AdjustmentType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-adjustmenttype""", alias="AdjustmentType")
    


    @property
    def tropo_type(self) -> troposphere.applicationautoscaling.StepScalingPolicyConfiguration:
        from troposphere.applicationautoscaling import StepScalingPolicyConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TargetTrackingMetric(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetric.html
    Properties:
        - Name: MetricName
        - Name: Dimensions
        - Name: Namespace
    
    """
    
    MetricName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetric.html#cfn-applicationautoscaling-scalingpolicy-targettrackingmetric-metricname""", alias="MetricName")
    Dimensions_: Optional[List['TargetTrackingMetricDimension']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetric.html#cfn-applicationautoscaling-scalingpolicy-targettrackingmetric-dimensions""", alias="Dimensions")
    Namespace_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetric.html#cfn-applicationautoscaling-scalingpolicy-targettrackingmetric-namespace""", alias="Namespace")
    


    @property
    def tropo_type(self) -> troposphere.applicationautoscaling.TargetTrackingMetric:
        from troposphere.applicationautoscaling import TargetTrackingMetric as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TargetTrackingMetricDataQuery(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery.html
    Properties:
        - Name: ReturnData
        - Name: Expression
        - Name: Label
        - Name: MetricStat
        - Name: Id
    
    """
    
    ReturnData_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery.html#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery-returndata""", alias="ReturnData")
    Expression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery.html#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery-expression""", alias="Expression")
    Label_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery.html#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery-label""", alias="Label")
    MetricStat_: Optional['TargetTrackingMetricStat'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery.html#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery-metricstat""", alias="MetricStat")
    Id_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery.html#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery-id""", alias="Id")
    


    @property
    def tropo_type(self) -> troposphere.applicationautoscaling.TargetTrackingMetricDataQuery:
        from troposphere.applicationautoscaling import TargetTrackingMetricDataQuery as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TargetTrackingMetricDimension(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdimension.html
    Properties:
        - Name: Value
        - Name: Name
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdimension.html#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdimension-value""", alias="Value")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdimension.html#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdimension-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.applicationautoscaling.TargetTrackingMetricDimension:
        from troposphere.applicationautoscaling import TargetTrackingMetricDimension as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TargetTrackingMetricStat(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricstat.html
    Properties:
        - Name: Stat
        - Name: Metric
        - Name: Unit
    
    """
    
    Stat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricstat.html#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricstat-stat""", alias="Stat")
    Metric_: Optional['TargetTrackingMetric'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricstat.html#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricstat-metric""", alias="Metric")
    Unit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricstat.html#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricstat-unit""", alias="Unit")
    


    @property
    def tropo_type(self) -> troposphere.applicationautoscaling.TargetTrackingMetricStat:
        from troposphere.applicationautoscaling import TargetTrackingMetricStat as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TargetTrackingScalingPolicyConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html
    Properties:
        - Name: ScaleOutCooldown
        - Name: TargetValue
        - Name: CustomizedMetricSpecification
        - Name: DisableScaleIn
        - Name: ScaleInCooldown
        - Name: PredefinedMetricSpecification
    
    """
    
    ScaleOutCooldown_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-scaleoutcooldown""", alias="ScaleOutCooldown")
    TargetValue_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-targetvalue""", alias="TargetValue")
    CustomizedMetricSpecification_: Optional['CustomizedMetricSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-customizedmetricspecification""", alias="CustomizedMetricSpecification")
    DisableScaleIn_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-disablescalein""", alias="DisableScaleIn")
    ScaleInCooldown_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-scaleincooldown""", alias="ScaleInCooldown")
    PredefinedMetricSpecification_: Optional['PredefinedMetricSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-predefinedmetricspecification""", alias="PredefinedMetricSpecification")
    


    @property
    def tropo_type(self) -> troposphere.applicationautoscaling.TargetTrackingScalingPolicyConfiguration:
        from troposphere.applicationautoscaling import TargetTrackingScalingPolicyConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class ScalableTarget(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html
    Properties:
        - Name: ScheduledActions
        - Name: ResourceId
        - Name: ServiceNamespace
        - Name: ScalableDimension
        - Name: SuspendedState
        - Name: MinCapacity
        - Name: RoleARN
        - Name: MaxCapacity
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ScheduledActions_: Optional[List['ScheduledAction']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-scheduledactions""", alias="ScheduledActions")
    ResourceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-resourceid""", alias="ResourceId")
    ServiceNamespace_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-servicenamespace""", alias="ServiceNamespace")
    ScalableDimension_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-scalabledimension""", alias="ScalableDimension")
    SuspendedState_: Optional['SuspendedState'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-suspendedstate""", alias="SuspendedState")
    MinCapacity_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-mincapacity""", alias="MinCapacity")
    RoleARN_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-rolearn""", alias="RoleARN")
    MaxCapacity_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-maxcapacity""", alias="MaxCapacity")
    

    @property
    def tropo_type(self) -> troposphere.applicationautoscaling.ScalableTarget:
        from troposphere.applicationautoscaling import ScalableTarget as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.applicationautoscaling import ScalableTarget as TropoT
        return resource_to_troposphere(self, TropoT)


class ScalingPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html
    Properties:
        - Name: PolicyType
        - Name: ResourceId
        - Name: ScalingTargetId
        - Name: PolicyName
        - Name: ServiceNamespace
        - Name: ScalableDimension
        - Name: TargetTrackingScalingPolicyConfiguration
        - Name: StepScalingPolicyConfiguration
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PolicyType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-policytype""", alias="PolicyType")
    ResourceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-resourceid""", alias="ResourceId")
    ScalingTargetId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-scalingtargetid""", alias="ScalingTargetId")
    PolicyName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-policyname""", alias="PolicyName")
    ServiceNamespace_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-servicenamespace""", alias="ServiceNamespace")
    ScalableDimension_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-scalabledimension""", alias="ScalableDimension")
    TargetTrackingScalingPolicyConfiguration_: Optional['TargetTrackingScalingPolicyConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration""", alias="TargetTrackingScalingPolicyConfiguration")
    StepScalingPolicyConfiguration_: Optional['StepScalingPolicyConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration""", alias="StepScalingPolicyConfiguration")
    

    @property
    def tropo_type(self) -> troposphere.applicationautoscaling.ScalingPolicy:
        from troposphere.applicationautoscaling import ScalingPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.applicationautoscaling import ScalingPolicy as TropoT
        return resource_to_troposphere(self, TropoT)

