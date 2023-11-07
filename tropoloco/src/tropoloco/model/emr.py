from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class Application(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-application.html
    Properties:
        - Name: AdditionalInfo
        - Name: Args
        - Name: Name
        - Name: Version
    
    """
    
    AdditionalInfo_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-application.html#cfn-elasticmapreduce-cluster-application-additionalinfo""", alias="AdditionalInfo")
    Args_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-application.html#cfn-elasticmapreduce-cluster-application-args""", alias="Args")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-application.html#cfn-elasticmapreduce-cluster-application-name""", alias="Name")
    Version_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-application.html#cfn-elasticmapreduce-cluster-application-version""", alias="Version")
    


    @property
    def tropo_type(self) -> troposphere.emr.Application:
        from troposphere.emr import Application as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AutoScalingPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-autoscalingpolicy.html
    Properties:
        - Name: Constraints
        - Name: Rules
    
    """
    
    Constraints_: 'ScalingConstraints' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-autoscalingpolicy.html#cfn-elasticmapreduce-cluster-autoscalingpolicy-constraints""", alias="Constraints")
    Rules_: List['ScalingRule'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-autoscalingpolicy.html#cfn-elasticmapreduce-cluster-autoscalingpolicy-rules""", alias="Rules")
    


    @property
    def tropo_type(self) -> troposphere.emr.AutoScalingPolicy:
        from troposphere.emr import AutoScalingPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AutoTerminationPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-autoterminationpolicy.html
    Properties:
        - Name: IdleTimeout
    
    """
    
    IdleTimeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-autoterminationpolicy.html#cfn-elasticmapreduce-cluster-autoterminationpolicy-idletimeout""", alias="IdleTimeout")
    


    @property
    def tropo_type(self) -> troposphere.emr.AutoTerminationPolicy:
        from troposphere.emr import AutoTerminationPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BootstrapActionConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-bootstrapactionconfig.html
    Properties:
        - Name: Name
        - Name: ScriptBootstrapAction
    
    """
    
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-bootstrapactionconfig.html#cfn-elasticmapreduce-cluster-bootstrapactionconfig-name""", alias="Name")
    ScriptBootstrapAction_: 'ScriptBootstrapActionConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-bootstrapactionconfig.html#cfn-elasticmapreduce-cluster-bootstrapactionconfig-scriptbootstrapaction""", alias="ScriptBootstrapAction")
    


    @property
    def tropo_type(self) -> troposphere.emr.BootstrapActionConfig:
        from troposphere.emr import BootstrapActionConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CloudWatchAlarmDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-cloudwatchalarmdefinition.html
    Properties:
        - Name: ComparisonOperator
        - Name: Dimensions
        - Name: EvaluationPeriods
        - Name: MetricName
        - Name: Namespace
        - Name: Period
        - Name: Statistic
        - Name: Threshold
        - Name: Unit
    
    """
    
    ComparisonOperator_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-cluster-cloudwatchalarmdefinition-comparisonoperator""", alias="ComparisonOperator")
    Dimensions_: Optional[List['MetricDimension']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-cluster-cloudwatchalarmdefinition-dimensions""", alias="Dimensions")
    EvaluationPeriods_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-cluster-cloudwatchalarmdefinition-evaluationperiods""", alias="EvaluationPeriods")
    MetricName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-cluster-cloudwatchalarmdefinition-metricname""", alias="MetricName")
    Namespace_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-cluster-cloudwatchalarmdefinition-namespace""", alias="Namespace")
    Period_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-cluster-cloudwatchalarmdefinition-period""", alias="Period")
    Statistic_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-cluster-cloudwatchalarmdefinition-statistic""", alias="Statistic")
    Threshold_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-cluster-cloudwatchalarmdefinition-threshold""", alias="Threshold")
    Unit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-cluster-cloudwatchalarmdefinition-unit""", alias="Unit")
    


    @property
    def tropo_type(self) -> troposphere.emr.CloudWatchAlarmDefinition:
        from troposphere.emr import CloudWatchAlarmDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ComputeLimits(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-computelimits.html
    Properties:
        - Name: MaximumCapacityUnits
        - Name: MaximumCoreCapacityUnits
        - Name: MaximumOnDemandCapacityUnits
        - Name: MinimumCapacityUnits
        - Name: UnitType
    
    """
    
    MaximumCapacityUnits_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-computelimits.html#cfn-elasticmapreduce-cluster-computelimits-maximumcapacityunits""", alias="MaximumCapacityUnits")
    MaximumCoreCapacityUnits_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-computelimits.html#cfn-elasticmapreduce-cluster-computelimits-maximumcorecapacityunits""", alias="MaximumCoreCapacityUnits")
    MaximumOnDemandCapacityUnits_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-computelimits.html#cfn-elasticmapreduce-cluster-computelimits-maximumondemandcapacityunits""", alias="MaximumOnDemandCapacityUnits")
    MinimumCapacityUnits_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-computelimits.html#cfn-elasticmapreduce-cluster-computelimits-minimumcapacityunits""", alias="MinimumCapacityUnits")
    UnitType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-computelimits.html#cfn-elasticmapreduce-cluster-computelimits-unittype""", alias="UnitType")
    


    @property
    def tropo_type(self) -> troposphere.emr.ComputeLimits:
        from troposphere.emr import ComputeLimits as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Configuration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-configuration.html
    Properties:
        - Name: Classification
        - Name: ConfigurationProperties
        - Name: Configurations
    
    """
    
    Classification_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-configuration.html#cfn-elasticmapreduce-cluster-configuration-classification""", alias="Classification")
    ConfigurationProperties_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-configuration.html#cfn-elasticmapreduce-cluster-configuration-configurationproperties""", alias="ConfigurationProperties")
    Configurations_: Optional[List['Configuration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-configuration.html#cfn-elasticmapreduce-cluster-configuration-configurations""", alias="Configurations")
    


    @property
    def tropo_type(self) -> troposphere.emr.Configuration:
        from troposphere.emr import Configuration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EbsBlockDeviceConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-ebsblockdeviceconfig.html
    Properties:
        - Name: VolumeSpecification
        - Name: VolumesPerInstance
    
    """
    
    VolumeSpecification_: 'VolumeSpecification' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-ebsblockdeviceconfig.html#cfn-elasticmapreduce-cluster-ebsblockdeviceconfig-volumespecification""", alias="VolumeSpecification")
    VolumesPerInstance_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-ebsblockdeviceconfig.html#cfn-elasticmapreduce-cluster-ebsblockdeviceconfig-volumesperinstance""", alias="VolumesPerInstance")
    


    @property
    def tropo_type(self) -> troposphere.emr.EbsBlockDeviceConfig:
        from troposphere.emr import EbsBlockDeviceConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EbsConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-ebsconfiguration.html
    Properties:
        - Name: EbsBlockDeviceConfigs
        - Name: EbsOptimized
    
    """
    
    EbsBlockDeviceConfigs_: Optional[List['EbsBlockDeviceConfig']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-ebsconfiguration.html#cfn-elasticmapreduce-cluster-ebsconfiguration-ebsblockdeviceconfigs""", alias="EbsBlockDeviceConfigs")
    EbsOptimized_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-ebsconfiguration.html#cfn-elasticmapreduce-cluster-ebsconfiguration-ebsoptimized""", alias="EbsOptimized")
    


    @property
    def tropo_type(self) -> troposphere.emr.EbsConfiguration:
        from troposphere.emr import EbsConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HadoopJarStepConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-hadoopjarstepconfig.html
    Properties:
        - Name: Args
        - Name: Jar
        - Name: MainClass
        - Name: StepProperties
    
    """
    
    Args_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-hadoopjarstepconfig.html#cfn-elasticmapreduce-cluster-hadoopjarstepconfig-args""", alias="Args")
    Jar_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-hadoopjarstepconfig.html#cfn-elasticmapreduce-cluster-hadoopjarstepconfig-jar""", alias="Jar")
    MainClass_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-hadoopjarstepconfig.html#cfn-elasticmapreduce-cluster-hadoopjarstepconfig-mainclass""", alias="MainClass")
    StepProperties_: Optional[List['KeyValue']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-hadoopjarstepconfig.html#cfn-elasticmapreduce-cluster-hadoopjarstepconfig-stepproperties""", alias="StepProperties")
    


    @property
    def tropo_type(self) -> troposphere.emr.HadoopJarStepConfig:
        from troposphere.emr import HadoopJarStepConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InstanceFleetConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancefleetconfig.html
    Properties:
        - Name: InstanceTypeConfigs
        - Name: LaunchSpecifications
        - Name: Name
        - Name: TargetOnDemandCapacity
        - Name: TargetSpotCapacity
    
    """
    
    InstanceTypeConfigs_: Optional[List['InstanceTypeConfig']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancefleetconfig.html#cfn-elasticmapreduce-cluster-instancefleetconfig-instancetypeconfigs""", alias="InstanceTypeConfigs")
    LaunchSpecifications_: Optional['InstanceFleetProvisioningSpecifications'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancefleetconfig.html#cfn-elasticmapreduce-cluster-instancefleetconfig-launchspecifications""", alias="LaunchSpecifications")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancefleetconfig.html#cfn-elasticmapreduce-cluster-instancefleetconfig-name""", alias="Name")
    TargetOnDemandCapacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancefleetconfig.html#cfn-elasticmapreduce-cluster-instancefleetconfig-targetondemandcapacity""", alias="TargetOnDemandCapacity")
    TargetSpotCapacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancefleetconfig.html#cfn-elasticmapreduce-cluster-instancefleetconfig-targetspotcapacity""", alias="TargetSpotCapacity")
    


    @property
    def tropo_type(self) -> troposphere.emr.InstanceFleetConfig:
        from troposphere.emr import InstanceFleetConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InstanceFleetProvisioningSpecifications(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancefleetprovisioningspecifications.html
    Properties:
        - Name: OnDemandSpecification
        - Name: SpotSpecification
    
    """
    
    OnDemandSpecification_: Optional['OnDemandProvisioningSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancefleetprovisioningspecifications.html#cfn-elasticmapreduce-cluster-instancefleetprovisioningspecifications-ondemandspecification""", alias="OnDemandSpecification")
    SpotSpecification_: Optional['SpotProvisioningSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancefleetprovisioningspecifications.html#cfn-elasticmapreduce-cluster-instancefleetprovisioningspecifications-spotspecification""", alias="SpotSpecification")
    


    @property
    def tropo_type(self) -> troposphere.emr.InstanceFleetProvisioningSpecifications:
        from troposphere.emr import InstanceFleetProvisioningSpecifications as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InstanceGroupConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancegroupconfig.html
    Properties:
        - Name: AutoScalingPolicy
        - Name: BidPrice
        - Name: Configurations
        - Name: CustomAmiId
        - Name: EbsConfiguration
        - Name: InstanceCount
        - Name: InstanceType
        - Name: Market
        - Name: Name
    
    """
    
    AutoScalingPolicy_: Optional['AutoScalingPolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancegroupconfig.html#cfn-elasticmapreduce-cluster-instancegroupconfig-autoscalingpolicy""", alias="AutoScalingPolicy")
    BidPrice_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancegroupconfig.html#cfn-elasticmapreduce-cluster-instancegroupconfig-bidprice""", alias="BidPrice")
    Configurations_: Optional[List['Configuration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancegroupconfig.html#cfn-elasticmapreduce-cluster-instancegroupconfig-configurations""", alias="Configurations")
    CustomAmiId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancegroupconfig.html#cfn-elasticmapreduce-cluster-instancegroupconfig-customamiid""", alias="CustomAmiId")
    EbsConfiguration_: Optional['EbsConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancegroupconfig.html#cfn-elasticmapreduce-cluster-instancegroupconfig-ebsconfiguration""", alias="EbsConfiguration")
    InstanceCount_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancegroupconfig.html#cfn-elasticmapreduce-cluster-instancegroupconfig-instancecount""", alias="InstanceCount")
    InstanceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancegroupconfig.html#cfn-elasticmapreduce-cluster-instancegroupconfig-instancetype""", alias="InstanceType")
    Market_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancegroupconfig.html#cfn-elasticmapreduce-cluster-instancegroupconfig-market""", alias="Market")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancegroupconfig.html#cfn-elasticmapreduce-cluster-instancegroupconfig-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.emr.InstanceGroupConfig:
        from troposphere.emr import InstanceGroupConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InstanceTypeConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancetypeconfig.html
    Properties:
        - Name: BidPrice
        - Name: BidPriceAsPercentageOfOnDemandPrice
        - Name: Configurations
        - Name: CustomAmiId
        - Name: EbsConfiguration
        - Name: InstanceType
        - Name: WeightedCapacity
    
    """
    
    BidPrice_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancetypeconfig.html#cfn-elasticmapreduce-cluster-instancetypeconfig-bidprice""", alias="BidPrice")
    BidPriceAsPercentageOfOnDemandPrice_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancetypeconfig.html#cfn-elasticmapreduce-cluster-instancetypeconfig-bidpriceaspercentageofondemandprice""", alias="BidPriceAsPercentageOfOnDemandPrice")
    Configurations_: Optional[List['Configuration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancetypeconfig.html#cfn-elasticmapreduce-cluster-instancetypeconfig-configurations""", alias="Configurations")
    CustomAmiId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancetypeconfig.html#cfn-elasticmapreduce-cluster-instancetypeconfig-customamiid""", alias="CustomAmiId")
    EbsConfiguration_: Optional['EbsConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancetypeconfig.html#cfn-elasticmapreduce-cluster-instancetypeconfig-ebsconfiguration""", alias="EbsConfiguration")
    InstanceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancetypeconfig.html#cfn-elasticmapreduce-cluster-instancetypeconfig-instancetype""", alias="InstanceType")
    WeightedCapacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancetypeconfig.html#cfn-elasticmapreduce-cluster-instancetypeconfig-weightedcapacity""", alias="WeightedCapacity")
    


    @property
    def tropo_type(self) -> troposphere.emr.InstanceTypeConfig:
        from troposphere.emr import InstanceTypeConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class JobFlowInstancesConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html
    Properties:
        - Name: AdditionalMasterSecurityGroups
        - Name: AdditionalSlaveSecurityGroups
        - Name: CoreInstanceFleet
        - Name: CoreInstanceGroup
        - Name: Ec2KeyName
        - Name: Ec2SubnetId
        - Name: Ec2SubnetIds
        - Name: EmrManagedMasterSecurityGroup
        - Name: EmrManagedSlaveSecurityGroup
        - Name: HadoopVersion
        - Name: KeepJobFlowAliveWhenNoSteps
        - Name: MasterInstanceFleet
        - Name: MasterInstanceGroup
        - Name: Placement
        - Name: ServiceAccessSecurityGroup
        - Name: TaskInstanceFleets
        - Name: TaskInstanceGroups
        - Name: TerminationProtected
    
    """
    
    AdditionalMasterSecurityGroups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-additionalmastersecuritygroups""", alias="AdditionalMasterSecurityGroups")
    AdditionalSlaveSecurityGroups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-additionalslavesecuritygroups""", alias="AdditionalSlaveSecurityGroups")
    CoreInstanceFleet_: Optional['InstanceFleetConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-coreinstancefleet""", alias="CoreInstanceFleet")
    CoreInstanceGroup_: Optional['InstanceGroupConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-coreinstancegroup""", alias="CoreInstanceGroup")
    Ec2KeyName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-ec2keyname""", alias="Ec2KeyName")
    Ec2SubnetId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-ec2subnetid""", alias="Ec2SubnetId")
    Ec2SubnetIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-ec2subnetids""", alias="Ec2SubnetIds")
    EmrManagedMasterSecurityGroup_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-emrmanagedmastersecuritygroup""", alias="EmrManagedMasterSecurityGroup")
    EmrManagedSlaveSecurityGroup_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-emrmanagedslavesecuritygroup""", alias="EmrManagedSlaveSecurityGroup")
    HadoopVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-hadoopversion""", alias="HadoopVersion")
    KeepJobFlowAliveWhenNoSteps_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-keepjobflowalivewhennosteps""", alias="KeepJobFlowAliveWhenNoSteps")
    MasterInstanceFleet_: Optional['InstanceFleetConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-masterinstancefleet""", alias="MasterInstanceFleet")
    MasterInstanceGroup_: Optional['InstanceGroupConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-masterinstancegroup""", alias="MasterInstanceGroup")
    Placement_: Optional['PlacementType'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-placement""", alias="Placement")
    ServiceAccessSecurityGroup_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-serviceaccesssecuritygroup""", alias="ServiceAccessSecurityGroup")
    TaskInstanceFleets_: Optional[List['InstanceFleetConfig']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-taskinstancefleets""", alias="TaskInstanceFleets")
    TaskInstanceGroups_: Optional[List['InstanceGroupConfig']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-taskinstancegroups""", alias="TaskInstanceGroups")
    TerminationProtected_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-terminationprotected""", alias="TerminationProtected")
    


    @property
    def tropo_type(self) -> troposphere.emr.JobFlowInstancesConfig:
        from troposphere.emr import JobFlowInstancesConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KerberosAttributes(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-kerberosattributes.html
    Properties:
        - Name: ADDomainJoinPassword
        - Name: ADDomainJoinUser
        - Name: CrossRealmTrustPrincipalPassword
        - Name: KdcAdminPassword
        - Name: Realm
    
    """
    
    ADDomainJoinPassword_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-kerberosattributes.html#cfn-elasticmapreduce-cluster-kerberosattributes-addomainjoinpassword""", alias="ADDomainJoinPassword")
    ADDomainJoinUser_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-kerberosattributes.html#cfn-elasticmapreduce-cluster-kerberosattributes-addomainjoinuser""", alias="ADDomainJoinUser")
    CrossRealmTrustPrincipalPassword_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-kerberosattributes.html#cfn-elasticmapreduce-cluster-kerberosattributes-crossrealmtrustprincipalpassword""", alias="CrossRealmTrustPrincipalPassword")
    KdcAdminPassword_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-kerberosattributes.html#cfn-elasticmapreduce-cluster-kerberosattributes-kdcadminpassword""", alias="KdcAdminPassword")
    Realm_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-kerberosattributes.html#cfn-elasticmapreduce-cluster-kerberosattributes-realm""", alias="Realm")
    


    @property
    def tropo_type(self) -> troposphere.emr.KerberosAttributes:
        from troposphere.emr import KerberosAttributes as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KeyValue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-keyvalue.html
    Properties:
        - Name: Key
        - Name: Value
    
    """
    
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-keyvalue.html#cfn-elasticmapreduce-cluster-keyvalue-key""", alias="Key")
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-keyvalue.html#cfn-elasticmapreduce-cluster-keyvalue-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.emr.KeyValue:
        from troposphere.emr import KeyValue as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ManagedScalingPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-managedscalingpolicy.html
    Properties:
        - Name: ComputeLimits
    
    """
    
    ComputeLimits_: Optional['ComputeLimits'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-managedscalingpolicy.html#cfn-elasticmapreduce-cluster-managedscalingpolicy-computelimits""", alias="ComputeLimits")
    


    @property
    def tropo_type(self) -> troposphere.emr.ManagedScalingPolicy:
        from troposphere.emr import ManagedScalingPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetricDimension(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-metricdimension.html
    Properties:
        - Name: Key
        - Name: Value
    
    """
    
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-metricdimension.html#cfn-elasticmapreduce-cluster-metricdimension-key""", alias="Key")
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-metricdimension.html#cfn-elasticmapreduce-cluster-metricdimension-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.emr.MetricDimension:
        from troposphere.emr import MetricDimension as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OnDemandProvisioningSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-ondemandprovisioningspecification.html
    Properties:
        - Name: AllocationStrategy
    
    """
    
    AllocationStrategy_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-ondemandprovisioningspecification.html#cfn-elasticmapreduce-cluster-ondemandprovisioningspecification-allocationstrategy""", alias="AllocationStrategy")
    


    @property
    def tropo_type(self) -> troposphere.emr.OnDemandProvisioningSpecification:
        from troposphere.emr import OnDemandProvisioningSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PlacementType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-placementtype.html
    Properties:
        - Name: AvailabilityZone
    
    """
    
    AvailabilityZone_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-placementtype.html#cfn-elasticmapreduce-cluster-placementtype-availabilityzone""", alias="AvailabilityZone")
    


    @property
    def tropo_type(self) -> troposphere.emr.PlacementType:
        from troposphere.emr import PlacementType as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ScalingAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-scalingaction.html
    Properties:
        - Name: Market
        - Name: SimpleScalingPolicyConfiguration
    
    """
    
    Market_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-scalingaction.html#cfn-elasticmapreduce-cluster-scalingaction-market""", alias="Market")
    SimpleScalingPolicyConfiguration_: 'SimpleScalingPolicyConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-scalingaction.html#cfn-elasticmapreduce-cluster-scalingaction-simplescalingpolicyconfiguration""", alias="SimpleScalingPolicyConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.emr.ScalingAction:
        from troposphere.emr import ScalingAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ScalingConstraints(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-scalingconstraints.html
    Properties:
        - Name: MaxCapacity
        - Name: MinCapacity
    
    """
    
    MaxCapacity_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-scalingconstraints.html#cfn-elasticmapreduce-cluster-scalingconstraints-maxcapacity""", alias="MaxCapacity")
    MinCapacity_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-scalingconstraints.html#cfn-elasticmapreduce-cluster-scalingconstraints-mincapacity""", alias="MinCapacity")
    


    @property
    def tropo_type(self) -> troposphere.emr.ScalingConstraints:
        from troposphere.emr import ScalingConstraints as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ScalingRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-scalingrule.html
    Properties:
        - Name: Action
        - Name: Description
        - Name: Name
        - Name: Trigger
    
    """
    
    Action_: 'ScalingAction' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-scalingrule.html#cfn-elasticmapreduce-cluster-scalingrule-action""", alias="Action")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-scalingrule.html#cfn-elasticmapreduce-cluster-scalingrule-description""", alias="Description")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-scalingrule.html#cfn-elasticmapreduce-cluster-scalingrule-name""", alias="Name")
    Trigger_: 'ScalingTrigger' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-scalingrule.html#cfn-elasticmapreduce-cluster-scalingrule-trigger""", alias="Trigger")
    


    @property
    def tropo_type(self) -> troposphere.emr.ScalingRule:
        from troposphere.emr import ScalingRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ScalingTrigger(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-scalingtrigger.html
    Properties:
        - Name: CloudWatchAlarmDefinition
    
    """
    
    CloudWatchAlarmDefinition_: 'CloudWatchAlarmDefinition' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-scalingtrigger.html#cfn-elasticmapreduce-cluster-scalingtrigger-cloudwatchalarmdefinition""", alias="CloudWatchAlarmDefinition")
    


    @property
    def tropo_type(self) -> troposphere.emr.ScalingTrigger:
        from troposphere.emr import ScalingTrigger as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ScriptBootstrapActionConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-scriptbootstrapactionconfig.html
    Properties:
        - Name: Args
        - Name: Path
    
    """
    
    Args_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-scriptbootstrapactionconfig.html#cfn-elasticmapreduce-cluster-scriptbootstrapactionconfig-args""", alias="Args")
    Path_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-scriptbootstrapactionconfig.html#cfn-elasticmapreduce-cluster-scriptbootstrapactionconfig-path""", alias="Path")
    


    @property
    def tropo_type(self) -> troposphere.emr.ScriptBootstrapActionConfig:
        from troposphere.emr import ScriptBootstrapActionConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SimpleScalingPolicyConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-simplescalingpolicyconfiguration.html
    Properties:
        - Name: AdjustmentType
        - Name: CoolDown
        - Name: ScalingAdjustment
    
    """
    
    AdjustmentType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-simplescalingpolicyconfiguration.html#cfn-elasticmapreduce-cluster-simplescalingpolicyconfiguration-adjustmenttype""", alias="AdjustmentType")
    CoolDown_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-simplescalingpolicyconfiguration.html#cfn-elasticmapreduce-cluster-simplescalingpolicyconfiguration-cooldown""", alias="CoolDown")
    ScalingAdjustment_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-simplescalingpolicyconfiguration.html#cfn-elasticmapreduce-cluster-simplescalingpolicyconfiguration-scalingadjustment""", alias="ScalingAdjustment")
    


    @property
    def tropo_type(self) -> troposphere.emr.SimpleScalingPolicyConfiguration:
        from troposphere.emr import SimpleScalingPolicyConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SpotProvisioningSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-spotprovisioningspecification.html
    Properties:
        - Name: AllocationStrategy
        - Name: BlockDurationMinutes
        - Name: TimeoutAction
        - Name: TimeoutDurationMinutes
    
    """
    
    AllocationStrategy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-spotprovisioningspecification.html#cfn-elasticmapreduce-cluster-spotprovisioningspecification-allocationstrategy""", alias="AllocationStrategy")
    BlockDurationMinutes_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-spotprovisioningspecification.html#cfn-elasticmapreduce-cluster-spotprovisioningspecification-blockdurationminutes""", alias="BlockDurationMinutes")
    TimeoutAction_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-spotprovisioningspecification.html#cfn-elasticmapreduce-cluster-spotprovisioningspecification-timeoutaction""", alias="TimeoutAction")
    TimeoutDurationMinutes_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-spotprovisioningspecification.html#cfn-elasticmapreduce-cluster-spotprovisioningspecification-timeoutdurationminutes""", alias="TimeoutDurationMinutes")
    


    @property
    def tropo_type(self) -> troposphere.emr.SpotProvisioningSpecification:
        from troposphere.emr import SpotProvisioningSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StepConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-stepconfig.html
    Properties:
        - Name: ActionOnFailure
        - Name: HadoopJarStep
        - Name: Name
    
    """
    
    ActionOnFailure_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-stepconfig.html#cfn-elasticmapreduce-cluster-stepconfig-actiononfailure""", alias="ActionOnFailure")
    HadoopJarStep_: 'HadoopJarStepConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-stepconfig.html#cfn-elasticmapreduce-cluster-stepconfig-hadoopjarstep""", alias="HadoopJarStep")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-stepconfig.html#cfn-elasticmapreduce-cluster-stepconfig-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.emr.StepConfig:
        from troposphere.emr import StepConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VolumeSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-volumespecification.html
    Properties:
        - Name: Iops
        - Name: SizeInGB
        - Name: Throughput
        - Name: VolumeType
    
    """
    
    Iops_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-volumespecification.html#cfn-elasticmapreduce-cluster-volumespecification-iops""", alias="Iops")
    SizeInGB_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-volumespecification.html#cfn-elasticmapreduce-cluster-volumespecification-sizeingb""", alias="SizeInGB")
    Throughput_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-volumespecification.html#cfn-elasticmapreduce-cluster-volumespecification-throughput""", alias="Throughput")
    VolumeType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-volumespecification.html#cfn-elasticmapreduce-cluster-volumespecification-volumetype""", alias="VolumeType")
    


    @property
    def tropo_type(self) -> troposphere.emr.VolumeSpecification:
        from troposphere.emr import VolumeSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Configuration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-configuration.html
    Properties:
        - Name: Classification
        - Name: ConfigurationProperties
        - Name: Configurations
    
    """
    
    Classification_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-configuration.html#cfn-elasticmapreduce-instancefleetconfig-configuration-classification""", alias="Classification")
    ConfigurationProperties_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-configuration.html#cfn-elasticmapreduce-instancefleetconfig-configuration-configurationproperties""", alias="ConfigurationProperties")
    Configurations_: Optional[List['Configuration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-configuration.html#cfn-elasticmapreduce-instancefleetconfig-configuration-configurations""", alias="Configurations")
    


    @property
    def tropo_type(self) -> troposphere.emr.Configuration:
        from troposphere.emr import Configuration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EbsBlockDeviceConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-ebsblockdeviceconfig.html
    Properties:
        - Name: VolumeSpecification
        - Name: VolumesPerInstance
    
    """
    
    VolumeSpecification_: 'VolumeSpecification' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-ebsblockdeviceconfig.html#cfn-elasticmapreduce-instancefleetconfig-ebsblockdeviceconfig-volumespecification""", alias="VolumeSpecification")
    VolumesPerInstance_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-ebsblockdeviceconfig.html#cfn-elasticmapreduce-instancefleetconfig-ebsblockdeviceconfig-volumesperinstance""", alias="VolumesPerInstance")
    


    @property
    def tropo_type(self) -> troposphere.emr.EbsBlockDeviceConfig:
        from troposphere.emr import EbsBlockDeviceConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EbsConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-ebsconfiguration.html
    Properties:
        - Name: EbsBlockDeviceConfigs
        - Name: EbsOptimized
    
    """
    
    EbsBlockDeviceConfigs_: Optional[List['EbsBlockDeviceConfig']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-ebsconfiguration.html#cfn-elasticmapreduce-instancefleetconfig-ebsconfiguration-ebsblockdeviceconfigs""", alias="EbsBlockDeviceConfigs")
    EbsOptimized_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-ebsconfiguration.html#cfn-elasticmapreduce-instancefleetconfig-ebsconfiguration-ebsoptimized""", alias="EbsOptimized")
    


    @property
    def tropo_type(self) -> troposphere.emr.EbsConfiguration:
        from troposphere.emr import EbsConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InstanceFleetProvisioningSpecifications(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancefleetprovisioningspecifications.html
    Properties:
        - Name: OnDemandSpecification
        - Name: SpotSpecification
    
    """
    
    OnDemandSpecification_: Optional['OnDemandProvisioningSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancefleetprovisioningspecifications.html#cfn-elasticmapreduce-instancefleetconfig-instancefleetprovisioningspecifications-ondemandspecification""", alias="OnDemandSpecification")
    SpotSpecification_: Optional['SpotProvisioningSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancefleetprovisioningspecifications.html#cfn-elasticmapreduce-instancefleetconfig-instancefleetprovisioningspecifications-spotspecification""", alias="SpotSpecification")
    


    @property
    def tropo_type(self) -> troposphere.emr.InstanceFleetProvisioningSpecifications:
        from troposphere.emr import InstanceFleetProvisioningSpecifications as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InstanceTypeConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancetypeconfig.html
    Properties:
        - Name: BidPrice
        - Name: BidPriceAsPercentageOfOnDemandPrice
        - Name: Configurations
        - Name: CustomAmiId
        - Name: EbsConfiguration
        - Name: InstanceType
        - Name: WeightedCapacity
    
    """
    
    BidPrice_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancetypeconfig.html#cfn-elasticmapreduce-instancefleetconfig-instancetypeconfig-bidprice""", alias="BidPrice")
    BidPriceAsPercentageOfOnDemandPrice_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancetypeconfig.html#cfn-elasticmapreduce-instancefleetconfig-instancetypeconfig-bidpriceaspercentageofondemandprice""", alias="BidPriceAsPercentageOfOnDemandPrice")
    Configurations_: Optional[List['Configuration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancetypeconfig.html#cfn-elasticmapreduce-instancefleetconfig-instancetypeconfig-configurations""", alias="Configurations")
    CustomAmiId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancetypeconfig.html#cfn-elasticmapreduce-instancefleetconfig-instancetypeconfig-customamiid""", alias="CustomAmiId")
    EbsConfiguration_: Optional['EbsConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancetypeconfig.html#cfn-elasticmapreduce-instancefleetconfig-instancetypeconfig-ebsconfiguration""", alias="EbsConfiguration")
    InstanceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancetypeconfig.html#cfn-elasticmapreduce-instancefleetconfig-instancetypeconfig-instancetype""", alias="InstanceType")
    WeightedCapacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancetypeconfig.html#cfn-elasticmapreduce-instancefleetconfig-instancetypeconfig-weightedcapacity""", alias="WeightedCapacity")
    


    @property
    def tropo_type(self) -> troposphere.emr.InstanceTypeConfig:
        from troposphere.emr import InstanceTypeConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OnDemandProvisioningSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-ondemandprovisioningspecification.html
    Properties:
        - Name: AllocationStrategy
    
    """
    
    AllocationStrategy_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-ondemandprovisioningspecification.html#cfn-elasticmapreduce-instancefleetconfig-ondemandprovisioningspecification-allocationstrategy""", alias="AllocationStrategy")
    


    @property
    def tropo_type(self) -> troposphere.emr.OnDemandProvisioningSpecification:
        from troposphere.emr import OnDemandProvisioningSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SpotProvisioningSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-spotprovisioningspecification.html
    Properties:
        - Name: AllocationStrategy
        - Name: BlockDurationMinutes
        - Name: TimeoutAction
        - Name: TimeoutDurationMinutes
    
    """
    
    AllocationStrategy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-spotprovisioningspecification.html#cfn-elasticmapreduce-instancefleetconfig-spotprovisioningspecification-allocationstrategy""", alias="AllocationStrategy")
    BlockDurationMinutes_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-spotprovisioningspecification.html#cfn-elasticmapreduce-instancefleetconfig-spotprovisioningspecification-blockdurationminutes""", alias="BlockDurationMinutes")
    TimeoutAction_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-spotprovisioningspecification.html#cfn-elasticmapreduce-instancefleetconfig-spotprovisioningspecification-timeoutaction""", alias="TimeoutAction")
    TimeoutDurationMinutes_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-spotprovisioningspecification.html#cfn-elasticmapreduce-instancefleetconfig-spotprovisioningspecification-timeoutdurationminutes""", alias="TimeoutDurationMinutes")
    


    @property
    def tropo_type(self) -> troposphere.emr.SpotProvisioningSpecification:
        from troposphere.emr import SpotProvisioningSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VolumeSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-volumespecification.html
    Properties:
        - Name: Iops
        - Name: SizeInGB
        - Name: Throughput
        - Name: VolumeType
    
    """
    
    Iops_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-volumespecification.html#cfn-elasticmapreduce-instancefleetconfig-volumespecification-iops""", alias="Iops")
    SizeInGB_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-volumespecification.html#cfn-elasticmapreduce-instancefleetconfig-volumespecification-sizeingb""", alias="SizeInGB")
    Throughput_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-volumespecification.html#cfn-elasticmapreduce-instancefleetconfig-volumespecification-throughput""", alias="Throughput")
    VolumeType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-volumespecification.html#cfn-elasticmapreduce-instancefleetconfig-volumespecification-volumetype""", alias="VolumeType")
    


    @property
    def tropo_type(self) -> troposphere.emr.VolumeSpecification:
        from troposphere.emr import VolumeSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AutoScalingPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-autoscalingpolicy.html
    Properties:
        - Name: Constraints
        - Name: Rules
    
    """
    
    Constraints_: 'ScalingConstraints' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-autoscalingpolicy.html#cfn-elasticmapreduce-instancegroupconfig-autoscalingpolicy-constraints""", alias="Constraints")
    Rules_: List['ScalingRule'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-autoscalingpolicy.html#cfn-elasticmapreduce-instancegroupconfig-autoscalingpolicy-rules""", alias="Rules")
    


    @property
    def tropo_type(self) -> troposphere.emr.AutoScalingPolicy:
        from troposphere.emr import AutoScalingPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CloudWatchAlarmDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition.html
    Properties:
        - Name: ComparisonOperator
        - Name: Dimensions
        - Name: EvaluationPeriods
        - Name: MetricName
        - Name: Namespace
        - Name: Period
        - Name: Statistic
        - Name: Threshold
        - Name: Unit
    
    """
    
    ComparisonOperator_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition-comparisonoperator""", alias="ComparisonOperator")
    Dimensions_: Optional[List['MetricDimension']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition-dimensions""", alias="Dimensions")
    EvaluationPeriods_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition-evaluationperiods""", alias="EvaluationPeriods")
    MetricName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition-metricname""", alias="MetricName")
    Namespace_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition-namespace""", alias="Namespace")
    Period_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition-period""", alias="Period")
    Statistic_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition-statistic""", alias="Statistic")
    Threshold_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition-threshold""", alias="Threshold")
    Unit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition-unit""", alias="Unit")
    


    @property
    def tropo_type(self) -> troposphere.emr.CloudWatchAlarmDefinition:
        from troposphere.emr import CloudWatchAlarmDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Configuration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-configuration.html
    Properties:
        - Name: Classification
        - Name: ConfigurationProperties
        - Name: Configurations
    
    """
    
    Classification_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-configuration.html#cfn-emr-cluster-configuration-classification""", alias="Classification")
    ConfigurationProperties_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-configuration.html#cfn-emr-cluster-configuration-configurationproperties""", alias="ConfigurationProperties")
    Configurations_: Optional[List['Configuration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-configuration.html#cfn-emr-cluster-configuration-configurations""", alias="Configurations")
    


    @property
    def tropo_type(self) -> troposphere.emr.Configuration:
        from troposphere.emr import Configuration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EbsBlockDeviceConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-ebsconfiguration-ebsblockdeviceconfig.html
    Properties:
        - Name: VolumeSpecification
        - Name: VolumesPerInstance
    
    """
    
    VolumeSpecification_: 'VolumeSpecification' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-ebsconfiguration-ebsblockdeviceconfig.html#cfn-emr-ebsconfiguration-ebsblockdeviceconfig-volumespecification""", alias="VolumeSpecification")
    VolumesPerInstance_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-ebsconfiguration-ebsblockdeviceconfig.html#cfn-emr-ebsconfiguration-ebsblockdeviceconfig-volumesperinstance""", alias="VolumesPerInstance")
    


    @property
    def tropo_type(self) -> troposphere.emr.EbsBlockDeviceConfig:
        from troposphere.emr import EbsBlockDeviceConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EbsConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-ebsconfiguration.html
    Properties:
        - Name: EbsBlockDeviceConfigs
        - Name: EbsOptimized
    
    """
    
    EbsBlockDeviceConfigs_: Optional[List['EbsBlockDeviceConfig']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-ebsconfiguration.html#cfn-emr-ebsconfiguration-ebsblockdeviceconfigs""", alias="EbsBlockDeviceConfigs")
    EbsOptimized_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-ebsconfiguration.html#cfn-emr-ebsconfiguration-ebsoptimized""", alias="EbsOptimized")
    


    @property
    def tropo_type(self) -> troposphere.emr.EbsConfiguration:
        from troposphere.emr import EbsConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetricDimension(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-metricdimension.html
    Properties:
        - Name: Key
        - Name: Value
    
    """
    
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-metricdimension.html#cfn-elasticmapreduce-instancegroupconfig-metricdimension-key""", alias="Key")
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-metricdimension.html#cfn-elasticmapreduce-instancegroupconfig-metricdimension-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.emr.MetricDimension:
        from troposphere.emr import MetricDimension as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ScalingAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-scalingaction.html
    Properties:
        - Name: Market
        - Name: SimpleScalingPolicyConfiguration
    
    """
    
    Market_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-scalingaction.html#cfn-elasticmapreduce-instancegroupconfig-scalingaction-market""", alias="Market")
    SimpleScalingPolicyConfiguration_: 'SimpleScalingPolicyConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-scalingaction.html#cfn-elasticmapreduce-instancegroupconfig-scalingaction-simplescalingpolicyconfiguration""", alias="SimpleScalingPolicyConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.emr.ScalingAction:
        from troposphere.emr import ScalingAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ScalingConstraints(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-scalingconstraints.html
    Properties:
        - Name: MaxCapacity
        - Name: MinCapacity
    
    """
    
    MaxCapacity_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-scalingconstraints.html#cfn-elasticmapreduce-instancegroupconfig-scalingconstraints-maxcapacity""", alias="MaxCapacity")
    MinCapacity_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-scalingconstraints.html#cfn-elasticmapreduce-instancegroupconfig-scalingconstraints-mincapacity""", alias="MinCapacity")
    


    @property
    def tropo_type(self) -> troposphere.emr.ScalingConstraints:
        from troposphere.emr import ScalingConstraints as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ScalingRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-scalingrule.html
    Properties:
        - Name: Action
        - Name: Description
        - Name: Name
        - Name: Trigger
    
    """
    
    Action_: 'ScalingAction' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-scalingrule.html#cfn-elasticmapreduce-instancegroupconfig-scalingrule-action""", alias="Action")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-scalingrule.html#cfn-elasticmapreduce-instancegroupconfig-scalingrule-description""", alias="Description")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-scalingrule.html#cfn-elasticmapreduce-instancegroupconfig-scalingrule-name""", alias="Name")
    Trigger_: 'ScalingTrigger' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-scalingrule.html#cfn-elasticmapreduce-instancegroupconfig-scalingrule-trigger""", alias="Trigger")
    


    @property
    def tropo_type(self) -> troposphere.emr.ScalingRule:
        from troposphere.emr import ScalingRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ScalingTrigger(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-scalingtrigger.html
    Properties:
        - Name: CloudWatchAlarmDefinition
    
    """
    
    CloudWatchAlarmDefinition_: 'CloudWatchAlarmDefinition' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-scalingtrigger.html#cfn-elasticmapreduce-instancegroupconfig-scalingtrigger-cloudwatchalarmdefinition""", alias="CloudWatchAlarmDefinition")
    


    @property
    def tropo_type(self) -> troposphere.emr.ScalingTrigger:
        from troposphere.emr import ScalingTrigger as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SimpleScalingPolicyConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-simplescalingpolicyconfiguration.html
    Properties:
        - Name: AdjustmentType
        - Name: CoolDown
        - Name: ScalingAdjustment
    
    """
    
    AdjustmentType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-simplescalingpolicyconfiguration.html#cfn-elasticmapreduce-instancegroupconfig-simplescalingpolicyconfiguration-adjustmenttype""", alias="AdjustmentType")
    CoolDown_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-simplescalingpolicyconfiguration.html#cfn-elasticmapreduce-instancegroupconfig-simplescalingpolicyconfiguration-cooldown""", alias="CoolDown")
    ScalingAdjustment_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-simplescalingpolicyconfiguration.html#cfn-elasticmapreduce-instancegroupconfig-simplescalingpolicyconfiguration-scalingadjustment""", alias="ScalingAdjustment")
    


    @property
    def tropo_type(self) -> troposphere.emr.SimpleScalingPolicyConfiguration:
        from troposphere.emr import SimpleScalingPolicyConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VolumeSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-ebsconfiguration-ebsblockdeviceconfig-volumespecification.html
    Properties:
        - Name: Iops
        - Name: SizeInGB
        - Name: Throughput
        - Name: VolumeType
    
    """
    
    Iops_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-ebsconfiguration-ebsblockdeviceconfig-volumespecification.html#cfn-emr-ebsconfiguration-ebsblockdeviceconfig-volumespecification-iops""", alias="Iops")
    SizeInGB_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-ebsconfiguration-ebsblockdeviceconfig-volumespecification.html#cfn-emr-ebsconfiguration-ebsblockdeviceconfig-volumespecification-sizeingb""", alias="SizeInGB")
    Throughput_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-ebsconfiguration-ebsblockdeviceconfig-volumespecification.html#cfn-emr-ebsconfiguration-ebsblockdeviceconfig-volumespecification-throughput""", alias="Throughput")
    VolumeType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-ebsconfiguration-ebsblockdeviceconfig-volumespecification.html#cfn-emr-ebsconfiguration-ebsblockdeviceconfig-volumespecification-volumetype""", alias="VolumeType")
    


    @property
    def tropo_type(self) -> troposphere.emr.VolumeSpecification:
        from troposphere.emr import VolumeSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HadoopJarStepConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-step-hadoopjarstepconfig.html
    Properties:
        - Name: Args
        - Name: MainClass
        - Name: StepProperties
        - Name: Jar
    
    """
    
    Args_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-step-hadoopjarstepconfig.html#cfn-emr-step-hadoopjarstepconfig-args""", alias="Args")
    MainClass_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-step-hadoopjarstepconfig.html#cfn-emr-step-hadoopjarstepconfig-mainclass""", alias="MainClass")
    StepProperties_: Optional[List['KeyValue']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-step-hadoopjarstepconfig.html#cfn-emr-step-hadoopjarstepconfig-stepproperties""", alias="StepProperties")
    Jar_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-step-hadoopjarstepconfig.html#cfn-emr-step-hadoopjarstepconfig-jar""", alias="Jar")
    


    @property
    def tropo_type(self) -> troposphere.emr.HadoopJarStepConfig:
        from troposphere.emr import HadoopJarStepConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KeyValue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-step-keyvalue.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-step-keyvalue.html#cfn-emr-step-keyvalue-value""", alias="Value")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-step-keyvalue.html#cfn-emr-step-keyvalue-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.emr.KeyValue:
        from troposphere.emr import KeyValue as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Cluster(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html
    Properties:
        - Name: AdditionalInfo
        - Name: Applications
        - Name: AutoScalingRole
        - Name: AutoTerminationPolicy
        - Name: BootstrapActions
        - Name: Configurations
        - Name: CustomAmiId
        - Name: EbsRootVolumeSize
        - Name: Instances
        - Name: JobFlowRole
        - Name: KerberosAttributes
        - Name: LogEncryptionKmsKeyId
        - Name: LogUri
        - Name: ManagedScalingPolicy
        - Name: Name
        - Name: OSReleaseLabel
        - Name: ReleaseLabel
        - Name: ScaleDownBehavior
        - Name: SecurityConfiguration
        - Name: ServiceRole
        - Name: StepConcurrencyLevel
        - Name: Steps
        - Name: Tags
        - Name: VisibleToAllUsers
    Attributes:
        - Name: MasterPublicDNS
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AdditionalInfo_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-additionalinfo""", alias="AdditionalInfo")
    Applications_: Optional[List['Application']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-applications""", alias="Applications")
    AutoScalingRole_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-autoscalingrole""", alias="AutoScalingRole")
    AutoTerminationPolicy_: Optional['AutoTerminationPolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-autoterminationpolicy""", alias="AutoTerminationPolicy")
    BootstrapActions_: Optional[List['BootstrapActionConfig']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-bootstrapactions""", alias="BootstrapActions")
    Configurations_: Optional[List['Configuration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-configurations""", alias="Configurations")
    CustomAmiId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-customamiid""", alias="CustomAmiId")
    EbsRootVolumeSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-ebsrootvolumesize""", alias="EbsRootVolumeSize")
    Instances_: 'JobFlowInstancesConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-instances""", alias="Instances")
    JobFlowRole_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-jobflowrole""", alias="JobFlowRole")
    KerberosAttributes_: Optional['KerberosAttributes'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-kerberosattributes""", alias="KerberosAttributes")
    LogEncryptionKmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-logencryptionkmskeyid""", alias="LogEncryptionKmsKeyId")
    LogUri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-loguri""", alias="LogUri")
    ManagedScalingPolicy_: Optional['ManagedScalingPolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-managedscalingpolicy""", alias="ManagedScalingPolicy")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-name""", alias="Name")
    OSReleaseLabel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-osreleaselabel""", alias="OSReleaseLabel")
    ReleaseLabel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-releaselabel""", alias="ReleaseLabel")
    ScaleDownBehavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-scaledownbehavior""", alias="ScaleDownBehavior")
    SecurityConfiguration_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-securityconfiguration""", alias="SecurityConfiguration")
    ServiceRole_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-servicerole""", alias="ServiceRole")
    StepConcurrencyLevel_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-stepconcurrencylevel""", alias="StepConcurrencyLevel")
    Steps_: Optional[List['StepConfig']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-steps""", alias="Steps")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-tags""", alias="Tags")
    VisibleToAllUsers_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-visibletoallusers""", alias="VisibleToAllUsers")
    

    @property
    def tropo_type(self) -> troposphere.emr.Cluster:
        from troposphere.emr import Cluster as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.emr import Cluster as TropoT
        return resource_to_troposphere(self, TropoT)


class InstanceFleetConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-instancefleetconfig.html
    Properties:
        - Name: ClusterId
        - Name: InstanceFleetType
        - Name: InstanceTypeConfigs
        - Name: LaunchSpecifications
        - Name: Name
        - Name: TargetOnDemandCapacity
        - Name: TargetSpotCapacity
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ClusterId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-instancefleetconfig.html#cfn-elasticmapreduce-instancefleetconfig-clusterid""", alias="ClusterId")
    InstanceFleetType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-instancefleetconfig.html#cfn-elasticmapreduce-instancefleetconfig-instancefleettype""", alias="InstanceFleetType")
    InstanceTypeConfigs_: Optional[List['InstanceTypeConfig']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-instancefleetconfig.html#cfn-elasticmapreduce-instancefleetconfig-instancetypeconfigs""", alias="InstanceTypeConfigs")
    LaunchSpecifications_: Optional['InstanceFleetProvisioningSpecifications'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-instancefleetconfig.html#cfn-elasticmapreduce-instancefleetconfig-launchspecifications""", alias="LaunchSpecifications")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-instancefleetconfig.html#cfn-elasticmapreduce-instancefleetconfig-name""", alias="Name")
    TargetOnDemandCapacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-instancefleetconfig.html#cfn-elasticmapreduce-instancefleetconfig-targetondemandcapacity""", alias="TargetOnDemandCapacity")
    TargetSpotCapacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-instancefleetconfig.html#cfn-elasticmapreduce-instancefleetconfig-targetspotcapacity""", alias="TargetSpotCapacity")
    

    @property
    def tropo_type(self) -> troposphere.emr.InstanceFleetConfig:
        from troposphere.emr import InstanceFleetConfig as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.emr import InstanceFleetConfig as TropoT
        return resource_to_troposphere(self, TropoT)


class InstanceGroupConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html
    Properties:
        - Name: AutoScalingPolicy
        - Name: BidPrice
        - Name: Configurations
        - Name: CustomAmiId
        - Name: EbsConfiguration
        - Name: InstanceCount
        - Name: InstanceRole
        - Name: InstanceType
        - Name: JobFlowId
        - Name: Market
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AutoScalingPolicy_: Optional['AutoScalingPolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-elasticmapreduce-instancegroupconfig-autoscalingpolicy""", alias="AutoScalingPolicy")
    BidPrice_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-bidprice""", alias="BidPrice")
    Configurations_: Optional[List['Configuration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-configurations""", alias="Configurations")
    CustomAmiId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-customamiid""", alias="CustomAmiId")
    EbsConfiguration_: Optional['EbsConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-ebsconfiguration""", alias="EbsConfiguration")
    InstanceCount_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfiginstancecount-""", alias="InstanceCount")
    InstanceRole_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-instancerole""", alias="InstanceRole")
    InstanceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-instancetype""", alias="InstanceType")
    JobFlowId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-jobflowid""", alias="JobFlowId")
    Market_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-market""", alias="Market")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.emr.InstanceGroupConfig:
        from troposphere.emr import InstanceGroupConfig as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.emr import InstanceGroupConfig as TropoT
        return resource_to_troposphere(self, TropoT)


class SecurityConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-securityconfiguration.html
    Properties:
        - Name: SecurityConfiguration
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SecurityConfiguration_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-securityconfiguration.html#cfn-emr-securityconfiguration-securityconfiguration""", alias="SecurityConfiguration")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-securityconfiguration.html#cfn-emr-securityconfiguration-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.emr.SecurityConfiguration:
        from troposphere.emr import SecurityConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.emr import SecurityConfiguration as TropoT
        return resource_to_troposphere(self, TropoT)


class Step(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-step.html
    Properties:
        - Name: JobFlowId
        - Name: ActionOnFailure
        - Name: HadoopJarStep
        - Name: Name
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    JobFlowId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-step.html#cfn-emr-step-jobflowid""", alias="JobFlowId")
    ActionOnFailure_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-step.html#cfn-emr-step-actiononfailure""", alias="ActionOnFailure")
    HadoopJarStep_: 'HadoopJarStepConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-step.html#cfn-emr-step-hadoopjarstep""", alias="HadoopJarStep")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-step.html#cfn-emr-step-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.emr.Step:
        from troposphere.emr import Step as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.emr import Step as TropoT
        return resource_to_troposphere(self, TropoT)


class Studio(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html
    Properties:
        - Name: WorkspaceSecurityGroupId
        - Name: Description
        - Name: DefaultS3Location
        - Name: SubnetIds
        - Name: IdpAuthUrl
        - Name: Name
        - Name: ServiceRole
        - Name: VpcId
        - Name: EngineSecurityGroupId
        - Name: UserRole
        - Name: IdpRelayStateParameterName
        - Name: AuthMode
        - Name: Tags
    Attributes:
        - Name: Arn
        - Name: StudioId
        - Name: Url
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    WorkspaceSecurityGroupId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-workspacesecuritygroupid""", alias="WorkspaceSecurityGroupId")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-description""", alias="Description")
    DefaultS3Location_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-defaults3location""", alias="DefaultS3Location")
    SubnetIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-subnetids""", alias="SubnetIds")
    IdpAuthUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-idpauthurl""", alias="IdpAuthUrl")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-name""", alias="Name")
    ServiceRole_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-servicerole""", alias="ServiceRole")
    VpcId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-vpcid""", alias="VpcId")
    EngineSecurityGroupId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-enginesecuritygroupid""", alias="EngineSecurityGroupId")
    UserRole_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-userrole""", alias="UserRole")
    IdpRelayStateParameterName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-idprelaystateparametername""", alias="IdpRelayStateParameterName")
    AuthMode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-authmode""", alias="AuthMode")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.emr.Studio:
        from troposphere.emr import Studio as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.emr import Studio as TropoT
        return resource_to_troposphere(self, TropoT)


class StudioSessionMapping(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studiosessionmapping.html
    Properties:
        - Name: IdentityType
        - Name: SessionPolicyArn
        - Name: StudioId
        - Name: IdentityName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    IdentityType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studiosessionmapping.html#cfn-emr-studiosessionmapping-identitytype""", alias="IdentityType")
    SessionPolicyArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studiosessionmapping.html#cfn-emr-studiosessionmapping-sessionpolicyarn""", alias="SessionPolicyArn")
    StudioId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studiosessionmapping.html#cfn-emr-studiosessionmapping-studioid""", alias="StudioId")
    IdentityName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studiosessionmapping.html#cfn-emr-studiosessionmapping-identityname""", alias="IdentityName")
    

    @property
    def tropo_type(self) -> troposphere.emr.StudioSessionMapping:
        from troposphere.emr import StudioSessionMapping as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.emr import StudioSessionMapping as TropoT
        return resource_to_troposphere(self, TropoT)


class WALWorkspace(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-walworkspace.html
    Properties:
        - Name: WALWorkspaceName
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    WALWorkspaceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-walworkspace.html#cfn-emr-walworkspace-walworkspacename""", alias="WALWorkspaceName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-walworkspace.html#cfn-emr-walworkspace-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.emr.WALWorkspace:
        from troposphere.emr import WALWorkspace as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.emr import WALWorkspace as TropoT
        return resource_to_troposphere(self, TropoT)

