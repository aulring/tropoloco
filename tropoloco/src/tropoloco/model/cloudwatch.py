from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class Dimension(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-dimension.html
    Properties:
        - Name: Value
        - Name: Name
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-dimension.html#cfn-cloudwatch-alarm-dimension-value""", alias="Value")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-dimension.html#cfn-cloudwatch-alarm-dimension-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.cloudwatch.Dimension:
        from troposphere.cloudwatch import Dimension as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Metric(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metric.html
    Properties:
        - Name: MetricName
        - Name: Dimensions
        - Name: Namespace
    
    """
    
    MetricName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metric.html#cfn-cloudwatch-alarm-metric-metricname""", alias="MetricName")
    Dimensions_: Optional[List['Dimension']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metric.html#cfn-cloudwatch-alarm-metric-dimensions""", alias="Dimensions")
    Namespace_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metric.html#cfn-cloudwatch-alarm-metric-namespace""", alias="Namespace")
    


    @property
    def tropo_type(self) -> troposphere.cloudwatch.Metric:
        from troposphere.cloudwatch import Metric as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetricDataQuery(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html
    Properties:
        - Name: AccountId
        - Name: ReturnData
        - Name: Expression
        - Name: Label
        - Name: MetricStat
        - Name: Period
        - Name: Id
    
    """
    
    AccountId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-accountid""", alias="AccountId")
    ReturnData_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-returndata""", alias="ReturnData")
    Expression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-expression""", alias="Expression")
    Label_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-label""", alias="Label")
    MetricStat_: Optional['MetricStat'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-metricstat""", alias="MetricStat")
    Period_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-period""", alias="Period")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-id""", alias="Id")
    


    @property
    def tropo_type(self) -> troposphere.cloudwatch.MetricDataQuery:
        from troposphere.cloudwatch import MetricDataQuery as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetricStat(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricstat.html
    Properties:
        - Name: Stat
        - Name: Period
        - Name: Metric
        - Name: Unit
    
    """
    
    Stat_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricstat.html#cfn-cloudwatch-alarm-metricstat-stat""", alias="Stat")
    Period_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricstat.html#cfn-cloudwatch-alarm-metricstat-period""", alias="Period")
    Metric_: 'Metric' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricstat.html#cfn-cloudwatch-alarm-metricstat-metric""", alias="Metric")
    Unit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricstat.html#cfn-cloudwatch-alarm-metricstat-unit""", alias="Unit")
    


    @property
    def tropo_type(self) -> troposphere.cloudwatch.MetricStat:
        from troposphere.cloudwatch import MetricStat as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Configuration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-configuration.html
    Properties:
        - Name: MetricTimeZone
        - Name: ExcludedTimeRanges
    
    """
    
    MetricTimeZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-configuration.html#cfn-cloudwatch-anomalydetector-configuration-metrictimezone""", alias="MetricTimeZone")
    ExcludedTimeRanges_: Optional[List['Range']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-configuration.html#cfn-cloudwatch-anomalydetector-configuration-excludedtimeranges""", alias="ExcludedTimeRanges")
    


    @property
    def tropo_type(self) -> troposphere.cloudwatch.Configuration:
        from troposphere.cloudwatch import Configuration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Dimension(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-dimension.html
    Properties:
        - Name: Value
        - Name: Name
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-dimension.html#cfn-cloudwatch-anomalydetector-dimension-value""", alias="Value")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-dimension.html#cfn-cloudwatch-anomalydetector-dimension-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.cloudwatch.Dimension:
        from troposphere.cloudwatch import Dimension as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Metric(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metric.html
    Properties:
        - Name: MetricName
        - Name: Dimensions
        - Name: Namespace
    
    """
    
    MetricName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metric.html#cfn-cloudwatch-anomalydetector-metric-metricname""", alias="MetricName")
    Dimensions_: Optional[List['Dimension']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metric.html#cfn-cloudwatch-anomalydetector-metric-dimensions""", alias="Dimensions")
    Namespace_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metric.html#cfn-cloudwatch-anomalydetector-metric-namespace""", alias="Namespace")
    


    @property
    def tropo_type(self) -> troposphere.cloudwatch.Metric:
        from troposphere.cloudwatch import Metric as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetricDataQueries(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataqueries.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.cloudwatch.MetricDataQueries:
        from troposphere.cloudwatch import MetricDataQueries as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetricDataQuery(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html
    Properties:
        - Name: AccountId
        - Name: ReturnData
        - Name: Expression
        - Name: MetricStat
        - Name: Label
        - Name: Period
        - Name: Id
    
    """
    
    AccountId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-accountid""", alias="AccountId")
    ReturnData_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-returndata""", alias="ReturnData")
    Expression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-expression""", alias="Expression")
    MetricStat_: Optional['MetricStat'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-metricstat""", alias="MetricStat")
    Label_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-label""", alias="Label")
    Period_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-period""", alias="Period")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-id""", alias="Id")
    


    @property
    def tropo_type(self) -> troposphere.cloudwatch.MetricDataQuery:
        from troposphere.cloudwatch import MetricDataQuery as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetricMathAnomalyDetector(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricmathanomalydetector.html
    Properties:
        - Name: MetricDataQueries
    
    """
    
    MetricDataQueries_: Optional[List['MetricDataQuery']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricmathanomalydetector.html#cfn-cloudwatch-anomalydetector-metricmathanomalydetector-metricdataqueries""", alias="MetricDataQueries")
    


    @property
    def tropo_type(self) -> troposphere.cloudwatch.MetricMathAnomalyDetector:
        from troposphere.cloudwatch import MetricMathAnomalyDetector as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetricStat(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricstat.html
    Properties:
        - Name: Stat
        - Name: Period
        - Name: Metric
        - Name: Unit
    
    """
    
    Stat_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricstat.html#cfn-cloudwatch-anomalydetector-metricstat-stat""", alias="Stat")
    Period_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricstat.html#cfn-cloudwatch-anomalydetector-metricstat-period""", alias="Period")
    Metric_: 'Metric' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricstat.html#cfn-cloudwatch-anomalydetector-metricstat-metric""", alias="Metric")
    Unit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricstat.html#cfn-cloudwatch-anomalydetector-metricstat-unit""", alias="Unit")
    


    @property
    def tropo_type(self) -> troposphere.cloudwatch.MetricStat:
        from troposphere.cloudwatch import MetricStat as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Range(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-range.html
    Properties:
        - Name: EndTime
        - Name: StartTime
    
    """
    
    EndTime_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-range.html#cfn-cloudwatch-anomalydetector-range-endtime""", alias="EndTime")
    StartTime_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-range.html#cfn-cloudwatch-anomalydetector-range-starttime""", alias="StartTime")
    


    @property
    def tropo_type(self) -> troposphere.cloudwatch.Range:
        from troposphere.cloudwatch import Range as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SingleMetricAnomalyDetector(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-singlemetricanomalydetector.html
    Properties:
        - Name: MetricName
        - Name: Stat
        - Name: Dimensions
        - Name: Namespace
    
    """
    
    MetricName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-singlemetricanomalydetector.html#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-metricname""", alias="MetricName")
    Stat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-singlemetricanomalydetector.html#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-stat""", alias="Stat")
    Dimensions_: Optional[List['Dimension']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-singlemetricanomalydetector.html#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-dimensions""", alias="Dimensions")
    Namespace_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-singlemetricanomalydetector.html#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-namespace""", alias="Namespace")
    


    @property
    def tropo_type(self) -> troposphere.cloudwatch.SingleMetricAnomalyDetector:
        from troposphere.cloudwatch import SingleMetricAnomalyDetector as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Tags(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-insightrule-tags.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.cloudwatch.Tags:
        from troposphere.cloudwatch import Tags as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetricStreamFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-metricstream-metricstreamfilter.html
    Properties:
        - Name: MetricNames
        - Name: Namespace
    
    """
    
    MetricNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-metricstream-metricstreamfilter.html#cfn-cloudwatch-metricstream-metricstreamfilter-metricnames""", alias="MetricNames")
    Namespace_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-metricstream-metricstreamfilter.html#cfn-cloudwatch-metricstream-metricstreamfilter-namespace""", alias="Namespace")
    


    @property
    def tropo_type(self) -> troposphere.cloudwatch.MetricStreamFilter:
        from troposphere.cloudwatch import MetricStreamFilter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetricStreamStatisticsConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-metricstream-metricstreamstatisticsconfiguration.html
    Properties:
        - Name: IncludeMetrics
        - Name: AdditionalStatistics
    
    """
    
    IncludeMetrics_: List['MetricStreamStatisticsMetric'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-metricstream-metricstreamstatisticsconfiguration.html#cfn-cloudwatch-metricstream-metricstreamstatisticsconfiguration-includemetrics""", alias="IncludeMetrics")
    AdditionalStatistics_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-metricstream-metricstreamstatisticsconfiguration.html#cfn-cloudwatch-metricstream-metricstreamstatisticsconfiguration-additionalstatistics""", alias="AdditionalStatistics")
    


    @property
    def tropo_type(self) -> troposphere.cloudwatch.MetricStreamStatisticsConfiguration:
        from troposphere.cloudwatch import MetricStreamStatisticsConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetricStreamStatisticsMetric(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-metricstream-metricstreamstatisticsmetric.html
    Properties:
        - Name: MetricName
        - Name: Namespace
    
    """
    
    MetricName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-metricstream-metricstreamstatisticsmetric.html#cfn-cloudwatch-metricstream-metricstreamstatisticsmetric-metricname""", alias="MetricName")
    Namespace_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-metricstream-metricstreamstatisticsmetric.html#cfn-cloudwatch-metricstream-metricstreamstatisticsmetric-namespace""", alias="Namespace")
    


    @property
    def tropo_type(self) -> troposphere.cloudwatch.MetricStreamStatisticsMetric:
        from troposphere.cloudwatch import MetricStreamStatisticsMetric as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Alarm(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html
    Properties:
        - Name: ThresholdMetricId
        - Name: EvaluateLowSampleCountPercentile
        - Name: ExtendedStatistic
        - Name: ComparisonOperator
        - Name: TreatMissingData
        - Name: Dimensions
        - Name: Period
        - Name: EvaluationPeriods
        - Name: Unit
        - Name: Namespace
        - Name: OKActions
        - Name: AlarmActions
        - Name: MetricName
        - Name: ActionsEnabled
        - Name: Metrics
        - Name: AlarmDescription
        - Name: AlarmName
        - Name: Statistic
        - Name: InsufficientDataActions
        - Name: DatapointsToAlarm
        - Name: Threshold
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ThresholdMetricId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-thresholdmetricid""", alias="ThresholdMetricId")
    EvaluateLowSampleCountPercentile_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-evaluatelowsamplecountpercentile""", alias="EvaluateLowSampleCountPercentile")
    ExtendedStatistic_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-extendedstatistic""", alias="ExtendedStatistic")
    ComparisonOperator_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-comparisonoperator""", alias="ComparisonOperator")
    TreatMissingData_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-treatmissingdata""", alias="TreatMissingData")
    Dimensions_: Optional[List['Dimension']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-dimensions""", alias="Dimensions")
    Period_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-period""", alias="Period")
    EvaluationPeriods_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-evaluationperiods""", alias="EvaluationPeriods")
    Unit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-unit""", alias="Unit")
    Namespace_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-namespace""", alias="Namespace")
    OKActions_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-okactions""", alias="OKActions")
    AlarmActions_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-alarmactions""", alias="AlarmActions")
    MetricName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-metricname""", alias="MetricName")
    ActionsEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-actionsenabled""", alias="ActionsEnabled")
    Metrics_: Optional[List['MetricDataQuery']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-metrics""", alias="Metrics")
    AlarmDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-alarmdescription""", alias="AlarmDescription")
    AlarmName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-alarmname""", alias="AlarmName")
    Statistic_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-statistic""", alias="Statistic")
    InsufficientDataActions_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-insufficientdataactions""", alias="InsufficientDataActions")
    DatapointsToAlarm_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-datapointstoalarm""", alias="DatapointsToAlarm")
    Threshold_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-threshold""", alias="Threshold")
    

    @property
    def tropo_type(self) -> troposphere.cloudwatch.Alarm:
        from troposphere.cloudwatch import Alarm as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudwatch import Alarm as TropoT
        return resource_to_troposphere(self, TropoT)


class AnomalyDetector(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html
    Properties:
        - Name: MetricName
        - Name: Stat
        - Name: Configuration
        - Name: MetricMathAnomalyDetector
        - Name: Dimensions
        - Name: Namespace
        - Name: SingleMetricAnomalyDetector
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MetricName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-metricname""", alias="MetricName")
    Stat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-stat""", alias="Stat")
    Configuration_: Optional['Configuration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-configuration""", alias="Configuration")
    MetricMathAnomalyDetector_: Optional['MetricMathAnomalyDetector'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-metricmathanomalydetector""", alias="MetricMathAnomalyDetector")
    Dimensions_: Optional[List['Dimension']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-dimensions""", alias="Dimensions")
    Namespace_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-namespace""", alias="Namespace")
    SingleMetricAnomalyDetector_: Optional['SingleMetricAnomalyDetector'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector""", alias="SingleMetricAnomalyDetector")
    

    @property
    def tropo_type(self) -> troposphere.cloudwatch.AnomalyDetector:
        from troposphere.cloudwatch import AnomalyDetector as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudwatch import AnomalyDetector as TropoT
        return resource_to_troposphere(self, TropoT)


class CompositeAlarm(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html
    Properties:
        - Name: AlarmActions
        - Name: ActionsSuppressorWaitPeriod
        - Name: ActionsEnabled
        - Name: AlarmName
        - Name: AlarmDescription
        - Name: ActionsSuppressor
        - Name: AlarmRule
        - Name: InsufficientDataActions
        - Name: OKActions
        - Name: ActionsSuppressorExtensionPeriod
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AlarmActions_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-alarmactions""", alias="AlarmActions")
    ActionsSuppressorWaitPeriod_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-actionssuppressorwaitperiod""", alias="ActionsSuppressorWaitPeriod")
    ActionsEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-actionsenabled""", alias="ActionsEnabled")
    AlarmName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-alarmname""", alias="AlarmName")
    AlarmDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-alarmdescription""", alias="AlarmDescription")
    ActionsSuppressor_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-actionssuppressor""", alias="ActionsSuppressor")
    AlarmRule_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-alarmrule""", alias="AlarmRule")
    InsufficientDataActions_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-insufficientdataactions""", alias="InsufficientDataActions")
    OKActions_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-okactions""", alias="OKActions")
    ActionsSuppressorExtensionPeriod_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-actionssuppressorextensionperiod""", alias="ActionsSuppressorExtensionPeriod")
    

    @property
    def tropo_type(self) -> troposphere.cloudwatch.CompositeAlarm:
        from troposphere.cloudwatch import CompositeAlarm as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudwatch import CompositeAlarm as TropoT
        return resource_to_troposphere(self, TropoT)


class Dashboard(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-dashboard.html
    Properties:
        - Name: DashboardName
        - Name: DashboardBody
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DashboardName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-dashboard.html#cfn-cloudwatch-dashboard-dashboardname""", alias="DashboardName")
    DashboardBody_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-dashboard.html#cfn-cloudwatch-dashboard-dashboardbody""", alias="DashboardBody")
    

    @property
    def tropo_type(self) -> troposphere.cloudwatch.Dashboard:
        from troposphere.cloudwatch import Dashboard as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudwatch import Dashboard as TropoT
        return resource_to_troposphere(self, TropoT)


class InsightRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html
    Properties:
        - Name: RuleState
        - Name: RuleBody
        - Name: RuleName
        - Name: Tags
    Attributes:
        - Name: Arn
        - Name: RuleName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    RuleState_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html#cfn-cloudwatch-insightrule-rulestate""", alias="RuleState")
    RuleBody_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html#cfn-cloudwatch-insightrule-rulebody""", alias="RuleBody")
    RuleName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html#cfn-cloudwatch-insightrule-rulename""", alias="RuleName")
    Tags_: Optional['Tags'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html#cfn-cloudwatch-insightrule-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.cloudwatch.InsightRule:
        from troposphere.cloudwatch import InsightRule as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudwatch import InsightRule as TropoT
        return resource_to_troposphere(self, TropoT)


class MetricStream(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html
    Properties:
        - Name: StatisticsConfigurations
        - Name: FirehoseArn
        - Name: IncludeLinkedAccountsMetrics
        - Name: IncludeFilters
        - Name: OutputFormat
        - Name: ExcludeFilters
        - Name: RoleArn
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: CreationDate
        - Name: State
        - Name: Arn
        - Name: LastUpdateDate
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    StatisticsConfigurations_: Optional[List['MetricStreamStatisticsConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-statisticsconfigurations""", alias="StatisticsConfigurations")
    FirehoseArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-firehosearn""", alias="FirehoseArn")
    IncludeLinkedAccountsMetrics_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-includelinkedaccountsmetrics""", alias="IncludeLinkedAccountsMetrics")
    IncludeFilters_: Optional[List['MetricStreamFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-includefilters""", alias="IncludeFilters")
    OutputFormat_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-outputformat""", alias="OutputFormat")
    ExcludeFilters_: Optional[List['MetricStreamFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-excludefilters""", alias="ExcludeFilters")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-rolearn""", alias="RoleArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.cloudwatch.MetricStream:
        from troposphere.cloudwatch import MetricStream as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudwatch import MetricStream as TropoT
        return resource_to_troposphere(self, TropoT)

