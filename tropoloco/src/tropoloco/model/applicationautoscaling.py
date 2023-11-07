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
        - Name: Dimensions
        - Name: MetricName
        - Name: Namespace
        - Name: Statistic
        - Name: Unit
    
    """
    
    Dimensions_: Optional[List['MetricDimension']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-dimensions""", alias="Dimensions")
    MetricName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-metricname""", alias="MetricName")
    Namespace_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-namespace""", alias="Namespace")
    Statistic_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-statistic""", alias="Statistic")
    Unit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-unit""", alias="Unit")
    


    @property
    def tropo_type(self) -> troposphere.applicationautoscaling.CustomizedMetricSpecification:
        from troposphere.applicationautoscaling import CustomizedMetricSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetricDimension(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-metricdimension.html
    Properties:
        - Name: Name
        - Name: Value
    
    """
    
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-metricdimension.html#cfn-applicationautoscaling-scalingpolicy-metricdimension-name""", alias="Name")
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-metricdimension.html#cfn-applicationautoscaling-scalingpolicy-metricdimension-value""", alias="Value")
    


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
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment.html
    Properties:
        - Name: MetricIntervalLowerBound
        - Name: MetricIntervalUpperBound
        - Name: ScalingAdjustment
    
    """
    
    MetricIntervalLowerBound_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment-metricintervallowerbound""", alias="MetricIntervalLowerBound")
    MetricIntervalUpperBound_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment-metricintervalupperbound""", alias="MetricIntervalUpperBound")
    ScalingAdjustment_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment-scalingadjustment""", alias="ScalingAdjustment")
    


    @property
    def tropo_type(self) -> troposphere.applicationautoscaling.StepAdjustment:
        from troposphere.applicationautoscaling import StepAdjustment as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StepScalingPolicyConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html
    Properties:
        - Name: AdjustmentType
        - Name: Cooldown
        - Name: MetricAggregationType
        - Name: MinAdjustmentMagnitude
        - Name: StepAdjustments
    
    """
    
    AdjustmentType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-adjustmenttype""", alias="AdjustmentType")
    Cooldown_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-cooldown""", alias="Cooldown")
    MetricAggregationType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-metricaggregationtype""", alias="MetricAggregationType")
    MinAdjustmentMagnitude_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-minadjustmentmagnitude""", alias="MinAdjustmentMagnitude")
    StepAdjustments_: Optional[List['StepAdjustment']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustments""", alias="StepAdjustments")
    


    @property
    def tropo_type(self) -> troposphere.applicationautoscaling.StepScalingPolicyConfiguration:
        from troposphere.applicationautoscaling import StepScalingPolicyConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TargetTrackingScalingPolicyConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html
    Properties:
        - Name: CustomizedMetricSpecification
        - Name: DisableScaleIn
        - Name: PredefinedMetricSpecification
        - Name: ScaleInCooldown
        - Name: ScaleOutCooldown
        - Name: TargetValue
    
    """
    
    CustomizedMetricSpecification_: Optional['CustomizedMetricSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-customizedmetricspecification""", alias="CustomizedMetricSpecification")
    DisableScaleIn_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-disablescalein""", alias="DisableScaleIn")
    PredefinedMetricSpecification_: Optional['PredefinedMetricSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-predefinedmetricspecification""", alias="PredefinedMetricSpecification")
    ScaleInCooldown_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-scaleincooldown""", alias="ScaleInCooldown")
    ScaleOutCooldown_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-scaleoutcooldown""", alias="ScaleOutCooldown")
    TargetValue_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-targetvalue""", alias="TargetValue")
    


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
        - Name: PolicyName
        - Name: PolicyType
        - Name: ResourceId
        - Name: ScalableDimension
        - Name: ScalingTargetId
        - Name: ServiceNamespace
        - Name: StepScalingPolicyConfiguration
        - Name: TargetTrackingScalingPolicyConfiguration
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PolicyName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-policyname""", alias="PolicyName")
    PolicyType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-policytype""", alias="PolicyType")
    ResourceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-resourceid""", alias="ResourceId")
    ScalableDimension_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-scalabledimension""", alias="ScalableDimension")
    ScalingTargetId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-scalingtargetid""", alias="ScalingTargetId")
    ServiceNamespace_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-servicenamespace""", alias="ServiceNamespace")
    StepScalingPolicyConfiguration_: Optional['StepScalingPolicyConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration""", alias="StepScalingPolicyConfiguration")
    TargetTrackingScalingPolicyConfiguration_: Optional['TargetTrackingScalingPolicyConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration""", alias="TargetTrackingScalingPolicyConfiguration")
    

    @property
    def tropo_type(self) -> troposphere.applicationautoscaling.ScalingPolicy:
        from troposphere.applicationautoscaling import ScalingPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.applicationautoscaling import ScalingPolicy as TropoT
        return resource_to_troposphere(self, TropoT)

