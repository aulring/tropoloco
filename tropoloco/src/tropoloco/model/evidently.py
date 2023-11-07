from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class MetricGoalObject(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-metricgoalobject.html
    Properties:
        - Name: EntityIdKey
        - Name: DesiredChange
        - Name: MetricName
        - Name: EventPattern
        - Name: ValueKey
        - Name: UnitLabel
    
    """
    
    EntityIdKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-metricgoalobject.html#cfn-evidently-experiment-metricgoalobject-entityidkey""", alias="EntityIdKey")
    DesiredChange_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-metricgoalobject.html#cfn-evidently-experiment-metricgoalobject-desiredchange""", alias="DesiredChange")
    MetricName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-metricgoalobject.html#cfn-evidently-experiment-metricgoalobject-metricname""", alias="MetricName")
    EventPattern_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-metricgoalobject.html#cfn-evidently-experiment-metricgoalobject-eventpattern""", alias="EventPattern")
    ValueKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-metricgoalobject.html#cfn-evidently-experiment-metricgoalobject-valuekey""", alias="ValueKey")
    UnitLabel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-metricgoalobject.html#cfn-evidently-experiment-metricgoalobject-unitlabel""", alias="UnitLabel")
    


    @property
    def tropo_type(self) -> troposphere.evidently.MetricGoalObject:
        from troposphere.evidently import MetricGoalObject as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OnlineAbConfigObject(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-onlineabconfigobject.html
    Properties:
        - Name: TreatmentWeights
        - Name: ControlTreatmentName
    
    """
    
    TreatmentWeights_: Optional[List['TreatmentToWeight']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-onlineabconfigobject.html#cfn-evidently-experiment-onlineabconfigobject-treatmentweights""", alias="TreatmentWeights")
    ControlTreatmentName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-onlineabconfigobject.html#cfn-evidently-experiment-onlineabconfigobject-controltreatmentname""", alias="ControlTreatmentName")
    


    @property
    def tropo_type(self) -> troposphere.evidently.OnlineAbConfigObject:
        from troposphere.evidently import OnlineAbConfigObject as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RunningStatusObject(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-runningstatusobject.html
    Properties:
        - Name: Status
        - Name: DesiredState
        - Name: AnalysisCompleteTime
        - Name: Reason
    
    """
    
    Status_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-runningstatusobject.html#cfn-evidently-experiment-runningstatusobject-status""", alias="Status")
    DesiredState_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-runningstatusobject.html#cfn-evidently-experiment-runningstatusobject-desiredstate""", alias="DesiredState")
    AnalysisCompleteTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-runningstatusobject.html#cfn-evidently-experiment-runningstatusobject-analysiscompletetime""", alias="AnalysisCompleteTime")
    Reason_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-runningstatusobject.html#cfn-evidently-experiment-runningstatusobject-reason""", alias="Reason")
    


    @property
    def tropo_type(self) -> troposphere.evidently.RunningStatusObject:
        from troposphere.evidently import RunningStatusObject as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TreatmentObject(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-treatmentobject.html
    Properties:
        - Name: Description
        - Name: Variation
        - Name: Feature
        - Name: TreatmentName
    
    """
    
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-treatmentobject.html#cfn-evidently-experiment-treatmentobject-description""", alias="Description")
    Variation_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-treatmentobject.html#cfn-evidently-experiment-treatmentobject-variation""", alias="Variation")
    Feature_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-treatmentobject.html#cfn-evidently-experiment-treatmentobject-feature""", alias="Feature")
    TreatmentName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-treatmentobject.html#cfn-evidently-experiment-treatmentobject-treatmentname""", alias="TreatmentName")
    


    @property
    def tropo_type(self) -> troposphere.evidently.TreatmentObject:
        from troposphere.evidently import TreatmentObject as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TreatmentToWeight(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-treatmenttoweight.html
    Properties:
        - Name: Treatment
        - Name: SplitWeight
    
    """
    
    Treatment_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-treatmenttoweight.html#cfn-evidently-experiment-treatmenttoweight-treatment""", alias="Treatment")
    SplitWeight_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-treatmenttoweight.html#cfn-evidently-experiment-treatmenttoweight-splitweight""", alias="SplitWeight")
    


    @property
    def tropo_type(self) -> troposphere.evidently.TreatmentToWeight:
        from troposphere.evidently import TreatmentToWeight as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EntityOverride(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-feature-entityoverride.html
    Properties:
        - Name: EntityId
        - Name: Variation
    
    """
    
    EntityId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-feature-entityoverride.html#cfn-evidently-feature-entityoverride-entityid""", alias="EntityId")
    Variation_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-feature-entityoverride.html#cfn-evidently-feature-entityoverride-variation""", alias="Variation")
    


    @property
    def tropo_type(self) -> troposphere.evidently.EntityOverride:
        from troposphere.evidently import EntityOverride as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VariationObject(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-feature-variationobject.html
    Properties:
        - Name: VariationName
        - Name: DoubleValue
        - Name: BooleanValue
        - Name: LongValue
        - Name: StringValue
    
    """
    
    VariationName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-feature-variationobject.html#cfn-evidently-feature-variationobject-variationname""", alias="VariationName")
    DoubleValue_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-feature-variationobject.html#cfn-evidently-feature-variationobject-doublevalue""", alias="DoubleValue")
    BooleanValue_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-feature-variationobject.html#cfn-evidently-feature-variationobject-booleanvalue""", alias="BooleanValue")
    LongValue_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-feature-variationobject.html#cfn-evidently-feature-variationobject-longvalue""", alias="LongValue")
    StringValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-feature-variationobject.html#cfn-evidently-feature-variationobject-stringvalue""", alias="StringValue")
    


    @property
    def tropo_type(self) -> troposphere.evidently.VariationObject:
        from troposphere.evidently import VariationObject as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ExecutionStatusObject(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-executionstatusobject.html
    Properties:
        - Name: Status
        - Name: DesiredState
        - Name: Reason
    
    """
    
    Status_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-executionstatusobject.html#cfn-evidently-launch-executionstatusobject-status""", alias="Status")
    DesiredState_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-executionstatusobject.html#cfn-evidently-launch-executionstatusobject-desiredstate""", alias="DesiredState")
    Reason_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-executionstatusobject.html#cfn-evidently-launch-executionstatusobject-reason""", alias="Reason")
    


    @property
    def tropo_type(self) -> troposphere.evidently.ExecutionStatusObject:
        from troposphere.evidently import ExecutionStatusObject as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GroupToWeight(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-grouptoweight.html
    Properties:
        - Name: GroupName
        - Name: SplitWeight
    
    """
    
    GroupName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-grouptoweight.html#cfn-evidently-launch-grouptoweight-groupname""", alias="GroupName")
    SplitWeight_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-grouptoweight.html#cfn-evidently-launch-grouptoweight-splitweight""", alias="SplitWeight")
    


    @property
    def tropo_type(self) -> troposphere.evidently.GroupToWeight:
        from troposphere.evidently import GroupToWeight as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LaunchGroupObject(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-launchgroupobject.html
    Properties:
        - Name: GroupName
        - Name: Description
        - Name: Variation
        - Name: Feature
    
    """
    
    GroupName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-launchgroupobject.html#cfn-evidently-launch-launchgroupobject-groupname""", alias="GroupName")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-launchgroupobject.html#cfn-evidently-launch-launchgroupobject-description""", alias="Description")
    Variation_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-launchgroupobject.html#cfn-evidently-launch-launchgroupobject-variation""", alias="Variation")
    Feature_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-launchgroupobject.html#cfn-evidently-launch-launchgroupobject-feature""", alias="Feature")
    


    @property
    def tropo_type(self) -> troposphere.evidently.LaunchGroupObject:
        from troposphere.evidently import LaunchGroupObject as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetricDefinitionObject(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-metricdefinitionobject.html
    Properties:
        - Name: EntityIdKey
        - Name: MetricName
        - Name: EventPattern
        - Name: ValueKey
        - Name: UnitLabel
    
    """
    
    EntityIdKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-metricdefinitionobject.html#cfn-evidently-launch-metricdefinitionobject-entityidkey""", alias="EntityIdKey")
    MetricName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-metricdefinitionobject.html#cfn-evidently-launch-metricdefinitionobject-metricname""", alias="MetricName")
    EventPattern_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-metricdefinitionobject.html#cfn-evidently-launch-metricdefinitionobject-eventpattern""", alias="EventPattern")
    ValueKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-metricdefinitionobject.html#cfn-evidently-launch-metricdefinitionobject-valuekey""", alias="ValueKey")
    UnitLabel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-metricdefinitionobject.html#cfn-evidently-launch-metricdefinitionobject-unitlabel""", alias="UnitLabel")
    


    @property
    def tropo_type(self) -> troposphere.evidently.MetricDefinitionObject:
        from troposphere.evidently import MetricDefinitionObject as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SegmentOverride(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-segmentoverride.html
    Properties:
        - Name: Weights
        - Name: EvaluationOrder
        - Name: Segment
    
    """
    
    Weights_: List['GroupToWeight'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-segmentoverride.html#cfn-evidently-launch-segmentoverride-weights""", alias="Weights")
    EvaluationOrder_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-segmentoverride.html#cfn-evidently-launch-segmentoverride-evaluationorder""", alias="EvaluationOrder")
    Segment_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-segmentoverride.html#cfn-evidently-launch-segmentoverride-segment""", alias="Segment")
    


    @property
    def tropo_type(self) -> troposphere.evidently.SegmentOverride:
        from troposphere.evidently import SegmentOverride as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StepConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-stepconfig.html
    Properties:
        - Name: GroupWeights
        - Name: SegmentOverrides
        - Name: StartTime
    
    """
    
    GroupWeights_: List['GroupToWeight'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-stepconfig.html#cfn-evidently-launch-stepconfig-groupweights""", alias="GroupWeights")
    SegmentOverrides_: Optional[List['SegmentOverride']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-stepconfig.html#cfn-evidently-launch-stepconfig-segmentoverrides""", alias="SegmentOverrides")
    StartTime_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-stepconfig.html#cfn-evidently-launch-stepconfig-starttime""", alias="StartTime")
    


    @property
    def tropo_type(self) -> troposphere.evidently.StepConfig:
        from troposphere.evidently import StepConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AppConfigResourceObject(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-project-appconfigresourceobject.html
    Properties:
        - Name: EnvironmentId
        - Name: ApplicationId
    
    """
    
    EnvironmentId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-project-appconfigresourceobject.html#cfn-evidently-project-appconfigresourceobject-environmentid""", alias="EnvironmentId")
    ApplicationId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-project-appconfigresourceobject.html#cfn-evidently-project-appconfigresourceobject-applicationid""", alias="ApplicationId")
    


    @property
    def tropo_type(self) -> troposphere.evidently.AppConfigResourceObject:
        from troposphere.evidently import AppConfigResourceObject as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataDeliveryObject(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-project-datadeliveryobject.html
    Properties:
        - Name: S3
        - Name: LogGroup
    
    """
    
    S3_: Optional['S3Destination'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-project-datadeliveryobject.html#cfn-evidently-project-datadeliveryobject-s3""", alias="S3")
    LogGroup_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-project-datadeliveryobject.html#cfn-evidently-project-datadeliveryobject-loggroup""", alias="LogGroup")
    


    @property
    def tropo_type(self) -> troposphere.evidently.DataDeliveryObject:
        from troposphere.evidently import DataDeliveryObject as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Destination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-project-s3destination.html
    Properties:
        - Name: BucketName
        - Name: Prefix
    
    """
    
    BucketName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-project-s3destination.html#cfn-evidently-project-s3destination-bucketname""", alias="BucketName")
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-project-s3destination.html#cfn-evidently-project-s3destination-prefix""", alias="Prefix")
    


    @property
    def tropo_type(self) -> troposphere.evidently.S3Destination:
        from troposphere.evidently import S3Destination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Experiment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html
    Properties:
        - Name: Project
        - Name: RunningStatus
        - Name: Description
        - Name: MetricGoals
        - Name: OnlineAbConfig
        - Name: RemoveSegment
        - Name: RandomizationSalt
        - Name: Treatments
        - Name: SamplingRate
        - Name: Segment
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Project_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-project""", alias="Project")
    RunningStatus_: Optional['RunningStatusObject'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-runningstatus""", alias="RunningStatus")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-description""", alias="Description")
    MetricGoals_: List['MetricGoalObject'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-metricgoals""", alias="MetricGoals")
    OnlineAbConfig_: 'OnlineAbConfigObject' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-onlineabconfig""", alias="OnlineAbConfig")
    RemoveSegment_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-removesegment""", alias="RemoveSegment")
    RandomizationSalt_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-randomizationsalt""", alias="RandomizationSalt")
    Treatments_: List['TreatmentObject'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-treatments""", alias="Treatments")
    SamplingRate_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-samplingrate""", alias="SamplingRate")
    Segment_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-segment""", alias="Segment")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.evidently.Experiment:
        from troposphere.evidently import Experiment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.evidently import Experiment as TropoT
        return resource_to_troposphere(self, TropoT)


class Feature(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html
    Properties:
        - Name: Project
        - Name: Description
        - Name: EvaluationStrategy
        - Name: DefaultVariation
        - Name: EntityOverrides
        - Name: Variations
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Project_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html#cfn-evidently-feature-project""", alias="Project")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html#cfn-evidently-feature-description""", alias="Description")
    EvaluationStrategy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html#cfn-evidently-feature-evaluationstrategy""", alias="EvaluationStrategy")
    DefaultVariation_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html#cfn-evidently-feature-defaultvariation""", alias="DefaultVariation")
    EntityOverrides_: Optional[List['EntityOverride']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html#cfn-evidently-feature-entityoverrides""", alias="EntityOverrides")
    Variations_: List['VariationObject'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html#cfn-evidently-feature-variations""", alias="Variations")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html#cfn-evidently-feature-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html#cfn-evidently-feature-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.evidently.Feature:
        from troposphere.evidently import Feature as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.evidently import Feature as TropoT
        return resource_to_troposphere(self, TropoT)


class Launch(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html
    Properties:
        - Name: Project
        - Name: Description
        - Name: ExecutionStatus
        - Name: Groups
        - Name: RandomizationSalt
        - Name: MetricMonitors
        - Name: ScheduledSplitsConfig
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Project_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-project""", alias="Project")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-description""", alias="Description")
    ExecutionStatus_: Optional['ExecutionStatusObject'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-executionstatus""", alias="ExecutionStatus")
    Groups_: List['LaunchGroupObject'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-groups""", alias="Groups")
    RandomizationSalt_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-randomizationsalt""", alias="RandomizationSalt")
    MetricMonitors_: Optional[List['MetricDefinitionObject']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-metricmonitors""", alias="MetricMonitors")
    ScheduledSplitsConfig_: List['StepConfig'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-scheduledsplitsconfig""", alias="ScheduledSplitsConfig")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.evidently.Launch:
        from troposphere.evidently import Launch as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.evidently import Launch as TropoT
        return resource_to_troposphere(self, TropoT)


class Project(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-project.html
    Properties:
        - Name: DataDelivery
        - Name: Description
        - Name: AppConfigResource
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DataDelivery_: Optional['DataDeliveryObject'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-project.html#cfn-evidently-project-datadelivery""", alias="DataDelivery")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-project.html#cfn-evidently-project-description""", alias="Description")
    AppConfigResource_: Optional['AppConfigResourceObject'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-project.html#cfn-evidently-project-appconfigresource""", alias="AppConfigResource")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-project.html#cfn-evidently-project-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-project.html#cfn-evidently-project-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.evidently.Project:
        from troposphere.evidently import Project as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.evidently import Project as TropoT
        return resource_to_troposphere(self, TropoT)


class Segment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-segment.html
    Properties:
        - Name: Pattern
        - Name: Description
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Pattern_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-segment.html#cfn-evidently-segment-pattern""", alias="Pattern")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-segment.html#cfn-evidently-segment-description""", alias="Description")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-segment.html#cfn-evidently-segment-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-segment.html#cfn-evidently-segment-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.evidently.Segment:
        from troposphere.evidently import Segment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.evidently import Segment as TropoT
        return resource_to_troposphere(self, TropoT)

