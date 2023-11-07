from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class Alarm(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-alarm.html
    Properties:
        - Name: AlarmName
        - Name: Severity
    
    """
    
    AlarmName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-alarm.html#cfn-applicationinsights-application-alarm-alarmname""", alias="AlarmName")
    Severity_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-alarm.html#cfn-applicationinsights-application-alarm-severity""", alias="Severity")
    


    @property
    def tropo_type(self) -> troposphere.applicationinsights.Alarm:
        from troposphere.applicationinsights import Alarm as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AlarmMetric(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-alarmmetric.html
    Properties:
        - Name: AlarmMetricName
    
    """
    
    AlarmMetricName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-alarmmetric.html#cfn-applicationinsights-application-alarmmetric-alarmmetricname""", alias="AlarmMetricName")
    


    @property
    def tropo_type(self) -> troposphere.applicationinsights.AlarmMetric:
        from troposphere.applicationinsights import AlarmMetric as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ComponentConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentconfiguration.html
    Properties:
        - Name: SubComponentTypeConfigurations
        - Name: ConfigurationDetails
    
    """
    
    SubComponentTypeConfigurations_: Optional[List['SubComponentTypeConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentconfiguration.html#cfn-applicationinsights-application-componentconfiguration-subcomponenttypeconfigurations""", alias="SubComponentTypeConfigurations")
    ConfigurationDetails_: Optional['ConfigurationDetails'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentconfiguration.html#cfn-applicationinsights-application-componentconfiguration-configurationdetails""", alias="ConfigurationDetails")
    


    @property
    def tropo_type(self) -> troposphere.applicationinsights.ComponentConfiguration:
        from troposphere.applicationinsights import ComponentConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ComponentMonitoringSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html
    Properties:
        - Name: CustomComponentConfiguration
        - Name: Tier
        - Name: ComponentConfigurationMode
        - Name: DefaultOverwriteComponentConfiguration
        - Name: ComponentName
        - Name: ComponentARN
    
    """
    
    CustomComponentConfiguration_: Optional['ComponentConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html#cfn-applicationinsights-application-componentmonitoringsetting-customcomponentconfiguration""", alias="CustomComponentConfiguration")
    Tier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html#cfn-applicationinsights-application-componentmonitoringsetting-tier""", alias="Tier")
    ComponentConfigurationMode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html#cfn-applicationinsights-application-componentmonitoringsetting-componentconfigurationmode""", alias="ComponentConfigurationMode")
    DefaultOverwriteComponentConfiguration_: Optional['ComponentConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html#cfn-applicationinsights-application-componentmonitoringsetting-defaultoverwritecomponentconfiguration""", alias="DefaultOverwriteComponentConfiguration")
    ComponentName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html#cfn-applicationinsights-application-componentmonitoringsetting-componentname""", alias="ComponentName")
    ComponentARN_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html#cfn-applicationinsights-application-componentmonitoringsetting-componentarn""", alias="ComponentARN")
    


    @property
    def tropo_type(self) -> troposphere.applicationinsights.ComponentMonitoringSetting:
        from troposphere.applicationinsights import ComponentMonitoringSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConfigurationDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html
    Properties:
        - Name: WindowsEvents
        - Name: AlarmMetrics
        - Name: Alarms
        - Name: HAClusterPrometheusExporter
        - Name: HANAPrometheusExporter
        - Name: Logs
        - Name: JMXPrometheusExporter
    
    """
    
    WindowsEvents_: Optional[List['WindowsEvent']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html#cfn-applicationinsights-application-configurationdetails-windowsevents""", alias="WindowsEvents")
    AlarmMetrics_: Optional[List['AlarmMetric']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html#cfn-applicationinsights-application-configurationdetails-alarmmetrics""", alias="AlarmMetrics")
    Alarms_: Optional[List['Alarm']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html#cfn-applicationinsights-application-configurationdetails-alarms""", alias="Alarms")
    HAClusterPrometheusExporter_: Optional['HAClusterPrometheusExporter'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html#cfn-applicationinsights-application-configurationdetails-haclusterprometheusexporter""", alias="HAClusterPrometheusExporter")
    HANAPrometheusExporter_: Optional['HANAPrometheusExporter'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html#cfn-applicationinsights-application-configurationdetails-hanaprometheusexporter""", alias="HANAPrometheusExporter")
    Logs_: Optional[List['Log']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html#cfn-applicationinsights-application-configurationdetails-logs""", alias="Logs")
    JMXPrometheusExporter_: Optional['JMXPrometheusExporter'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html#cfn-applicationinsights-application-configurationdetails-jmxprometheusexporter""", alias="JMXPrometheusExporter")
    


    @property
    def tropo_type(self) -> troposphere.applicationinsights.ConfigurationDetails:
        from troposphere.applicationinsights import ConfigurationDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomComponent(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-customcomponent.html
    Properties:
        - Name: ResourceList
        - Name: ComponentName
    
    """
    
    ResourceList_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-customcomponent.html#cfn-applicationinsights-application-customcomponent-resourcelist""", alias="ResourceList")
    ComponentName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-customcomponent.html#cfn-applicationinsights-application-customcomponent-componentname""", alias="ComponentName")
    


    @property
    def tropo_type(self) -> troposphere.applicationinsights.CustomComponent:
        from troposphere.applicationinsights import CustomComponent as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HAClusterPrometheusExporter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-haclusterprometheusexporter.html
    Properties:
        - Name: PrometheusPort
    
    """
    
    PrometheusPort_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-haclusterprometheusexporter.html#cfn-applicationinsights-application-haclusterprometheusexporter-prometheusport""", alias="PrometheusPort")
    


    @property
    def tropo_type(self) -> troposphere.applicationinsights.HAClusterPrometheusExporter:
        from troposphere.applicationinsights import HAClusterPrometheusExporter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HANAPrometheusExporter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-hanaprometheusexporter.html
    Properties:
        - Name: HANAPort
        - Name: PrometheusPort
        - Name: HANASecretName
        - Name: HANASID
        - Name: AgreeToInstallHANADBClient
    
    """
    
    HANAPort_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-hanaprometheusexporter.html#cfn-applicationinsights-application-hanaprometheusexporter-hanaport""", alias="HANAPort")
    PrometheusPort_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-hanaprometheusexporter.html#cfn-applicationinsights-application-hanaprometheusexporter-prometheusport""", alias="PrometheusPort")
    HANASecretName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-hanaprometheusexporter.html#cfn-applicationinsights-application-hanaprometheusexporter-hanasecretname""", alias="HANASecretName")
    HANASID_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-hanaprometheusexporter.html#cfn-applicationinsights-application-hanaprometheusexporter-hanasid""", alias="HANASID")
    AgreeToInstallHANADBClient_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-hanaprometheusexporter.html#cfn-applicationinsights-application-hanaprometheusexporter-agreetoinstallhanadbclient""", alias="AgreeToInstallHANADBClient")
    


    @property
    def tropo_type(self) -> troposphere.applicationinsights.HANAPrometheusExporter:
        from troposphere.applicationinsights import HANAPrometheusExporter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class JMXPrometheusExporter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-jmxprometheusexporter.html
    Properties:
        - Name: PrometheusPort
        - Name: JMXURL
        - Name: HostPort
    
    """
    
    PrometheusPort_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-jmxprometheusexporter.html#cfn-applicationinsights-application-jmxprometheusexporter-prometheusport""", alias="PrometheusPort")
    JMXURL_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-jmxprometheusexporter.html#cfn-applicationinsights-application-jmxprometheusexporter-jmxurl""", alias="JMXURL")
    HostPort_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-jmxprometheusexporter.html#cfn-applicationinsights-application-jmxprometheusexporter-hostport""", alias="HostPort")
    


    @property
    def tropo_type(self) -> troposphere.applicationinsights.JMXPrometheusExporter:
        from troposphere.applicationinsights import JMXPrometheusExporter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Log(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-log.html
    Properties:
        - Name: LogType
        - Name: Encoding
        - Name: LogGroupName
        - Name: LogPath
        - Name: PatternSet
    
    """
    
    LogType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-log.html#cfn-applicationinsights-application-log-logtype""", alias="LogType")
    Encoding_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-log.html#cfn-applicationinsights-application-log-encoding""", alias="Encoding")
    LogGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-log.html#cfn-applicationinsights-application-log-loggroupname""", alias="LogGroupName")
    LogPath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-log.html#cfn-applicationinsights-application-log-logpath""", alias="LogPath")
    PatternSet_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-log.html#cfn-applicationinsights-application-log-patternset""", alias="PatternSet")
    


    @property
    def tropo_type(self) -> troposphere.applicationinsights.Log:
        from troposphere.applicationinsights import Log as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LogPattern(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpattern.html
    Properties:
        - Name: Pattern
        - Name: Rank
        - Name: PatternName
    
    """
    
    Pattern_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpattern.html#cfn-applicationinsights-application-logpattern-pattern""", alias="Pattern")
    Rank_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpattern.html#cfn-applicationinsights-application-logpattern-rank""", alias="Rank")
    PatternName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpattern.html#cfn-applicationinsights-application-logpattern-patternname""", alias="PatternName")
    


    @property
    def tropo_type(self) -> troposphere.applicationinsights.LogPattern:
        from troposphere.applicationinsights import LogPattern as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LogPatternSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpatternset.html
    Properties:
        - Name: PatternSetName
        - Name: LogPatterns
    
    """
    
    PatternSetName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpatternset.html#cfn-applicationinsights-application-logpatternset-patternsetname""", alias="PatternSetName")
    LogPatterns_: List['LogPattern'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpatternset.html#cfn-applicationinsights-application-logpatternset-logpatterns""", alias="LogPatterns")
    


    @property
    def tropo_type(self) -> troposphere.applicationinsights.LogPatternSet:
        from troposphere.applicationinsights import LogPatternSet as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SubComponentConfigurationDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponentconfigurationdetails.html
    Properties:
        - Name: WindowsEvents
        - Name: AlarmMetrics
        - Name: Logs
    
    """
    
    WindowsEvents_: Optional[List['WindowsEvent']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponentconfigurationdetails.html#cfn-applicationinsights-application-subcomponentconfigurationdetails-windowsevents""", alias="WindowsEvents")
    AlarmMetrics_: Optional[List['AlarmMetric']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponentconfigurationdetails.html#cfn-applicationinsights-application-subcomponentconfigurationdetails-alarmmetrics""", alias="AlarmMetrics")
    Logs_: Optional[List['Log']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponentconfigurationdetails.html#cfn-applicationinsights-application-subcomponentconfigurationdetails-logs""", alias="Logs")
    


    @property
    def tropo_type(self) -> troposphere.applicationinsights.SubComponentConfigurationDetails:
        from troposphere.applicationinsights import SubComponentConfigurationDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SubComponentTypeConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponenttypeconfiguration.html
    Properties:
        - Name: SubComponentType
        - Name: SubComponentConfigurationDetails
    
    """
    
    SubComponentType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponenttypeconfiguration.html#cfn-applicationinsights-application-subcomponenttypeconfiguration-subcomponenttype""", alias="SubComponentType")
    SubComponentConfigurationDetails_: 'SubComponentConfigurationDetails' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponenttypeconfiguration.html#cfn-applicationinsights-application-subcomponenttypeconfiguration-subcomponentconfigurationdetails""", alias="SubComponentConfigurationDetails")
    


    @property
    def tropo_type(self) -> troposphere.applicationinsights.SubComponentTypeConfiguration:
        from troposphere.applicationinsights import SubComponentTypeConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WindowsEvent(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-windowsevent.html
    Properties:
        - Name: EventLevels
        - Name: LogGroupName
        - Name: EventName
        - Name: PatternSet
    
    """
    
    EventLevels_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-windowsevent.html#cfn-applicationinsights-application-windowsevent-eventlevels""", alias="EventLevels")
    LogGroupName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-windowsevent.html#cfn-applicationinsights-application-windowsevent-loggroupname""", alias="LogGroupName")
    EventName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-windowsevent.html#cfn-applicationinsights-application-windowsevent-eventname""", alias="EventName")
    PatternSet_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-windowsevent.html#cfn-applicationinsights-application-windowsevent-patternset""", alias="PatternSet")
    


    @property
    def tropo_type(self) -> troposphere.applicationinsights.WindowsEvent:
        from troposphere.applicationinsights import WindowsEvent as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Application(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html
    Properties:
        - Name: AutoConfigurationEnabled
        - Name: OpsItemSNSTopicArn
        - Name: OpsCenterEnabled
        - Name: CustomComponents
        - Name: LogPatternSets
        - Name: GroupingType
        - Name: ComponentMonitoringSettings
        - Name: CWEMonitorEnabled
        - Name: Tags
        - Name: ResourceGroupName
    Attributes:
        - Name: ApplicationARN
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AutoConfigurationEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-autoconfigurationenabled""", alias="AutoConfigurationEnabled")
    OpsItemSNSTopicArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-opsitemsnstopicarn""", alias="OpsItemSNSTopicArn")
    OpsCenterEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-opscenterenabled""", alias="OpsCenterEnabled")
    CustomComponents_: Optional[List['CustomComponent']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-customcomponents""", alias="CustomComponents")
    LogPatternSets_: Optional[List['LogPatternSet']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-logpatternsets""", alias="LogPatternSets")
    GroupingType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-groupingtype""", alias="GroupingType")
    ComponentMonitoringSettings_: Optional[List['ComponentMonitoringSetting']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-componentmonitoringsettings""", alias="ComponentMonitoringSettings")
    CWEMonitorEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-cwemonitorenabled""", alias="CWEMonitorEnabled")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-tags""", alias="Tags")
    ResourceGroupName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-resourcegroupname""", alias="ResourceGroupName")
    

    @property
    def tropo_type(self) -> troposphere.applicationinsights.Application:
        from troposphere.applicationinsights import Application as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.applicationinsights import Application as TropoT
        return resource_to_troposphere(self, TropoT)

