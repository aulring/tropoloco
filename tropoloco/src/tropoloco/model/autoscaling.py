from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AcceleratorCountRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-acceleratorcountrequest.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-acceleratorcountrequest.html#cfn-autoscaling-autoscalinggroup-acceleratorcountrequest-min""", alias="Min")
    Max_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-acceleratorcountrequest.html#cfn-autoscaling-autoscalinggroup-acceleratorcountrequest-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.AcceleratorCountRequest:
        from troposphere.autoscaling import AcceleratorCountRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AcceleratorTotalMemoryMiBRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-acceleratortotalmemorymibrequest.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-acceleratortotalmemorymibrequest.html#cfn-autoscaling-autoscalinggroup-acceleratortotalmemorymibrequest-min""", alias="Min")
    Max_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-acceleratortotalmemorymibrequest.html#cfn-autoscaling-autoscalinggroup-acceleratortotalmemorymibrequest-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.AcceleratorTotalMemoryMiBRequest:
        from troposphere.autoscaling import AcceleratorTotalMemoryMiBRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BaselineEbsBandwidthMbpsRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-baselineebsbandwidthmbpsrequest.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-baselineebsbandwidthmbpsrequest.html#cfn-autoscaling-autoscalinggroup-baselineebsbandwidthmbpsrequest-min""", alias="Min")
    Max_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-baselineebsbandwidthmbpsrequest.html#cfn-autoscaling-autoscalinggroup-baselineebsbandwidthmbpsrequest-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.BaselineEbsBandwidthMbpsRequest:
        from troposphere.autoscaling import BaselineEbsBandwidthMbpsRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InstanceMaintenancePolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancemaintenancepolicy.html
    Properties:
        - Name: MaxHealthyPercentage
        - Name: MinHealthyPercentage
    
    """
    
    MaxHealthyPercentage_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancemaintenancepolicy.html#cfn-autoscaling-autoscalinggroup-instancemaintenancepolicy-maxhealthypercentage""", alias="MaxHealthyPercentage")
    MinHealthyPercentage_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancemaintenancepolicy.html#cfn-autoscaling-autoscalinggroup-instancemaintenancepolicy-minhealthypercentage""", alias="MinHealthyPercentage")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.InstanceMaintenancePolicy:
        from troposphere.autoscaling import InstanceMaintenancePolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InstanceRequirements(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancerequirements.html
    Properties:
        - Name: LocalStorageTypes
        - Name: InstanceGenerations
        - Name: NetworkInterfaceCount
        - Name: AcceleratorTypes
        - Name: MemoryGiBPerVCpu
        - Name: AcceleratorManufacturers
        - Name: ExcludedInstanceTypes
        - Name: VCpuCount
        - Name: AllowedInstanceTypes
        - Name: LocalStorage
        - Name: CpuManufacturers
        - Name: AcceleratorCount
        - Name: NetworkBandwidthGbps
        - Name: BareMetal
        - Name: RequireHibernateSupport
        - Name: BaselineEbsBandwidthMbps
        - Name: SpotMaxPricePercentageOverLowestPrice
        - Name: AcceleratorNames
        - Name: AcceleratorTotalMemoryMiB
        - Name: OnDemandMaxPricePercentageOverLowestPrice
        - Name: BurstablePerformance
        - Name: MemoryMiB
        - Name: TotalLocalStorageGB
    
    """
    
    LocalStorageTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancerequirements.html#cfn-autoscaling-autoscalinggroup-instancerequirements-localstoragetypes""", alias="LocalStorageTypes")
    InstanceGenerations_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancerequirements.html#cfn-autoscaling-autoscalinggroup-instancerequirements-instancegenerations""", alias="InstanceGenerations")
    NetworkInterfaceCount_: Optional['NetworkInterfaceCountRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancerequirements.html#cfn-autoscaling-autoscalinggroup-instancerequirements-networkinterfacecount""", alias="NetworkInterfaceCount")
    AcceleratorTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancerequirements.html#cfn-autoscaling-autoscalinggroup-instancerequirements-acceleratortypes""", alias="AcceleratorTypes")
    MemoryGiBPerVCpu_: Optional['MemoryGiBPerVCpuRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancerequirements.html#cfn-autoscaling-autoscalinggroup-instancerequirements-memorygibpervcpu""", alias="MemoryGiBPerVCpu")
    AcceleratorManufacturers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancerequirements.html#cfn-autoscaling-autoscalinggroup-instancerequirements-acceleratormanufacturers""", alias="AcceleratorManufacturers")
    ExcludedInstanceTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancerequirements.html#cfn-autoscaling-autoscalinggroup-instancerequirements-excludedinstancetypes""", alias="ExcludedInstanceTypes")
    VCpuCount_: Optional['VCpuCountRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancerequirements.html#cfn-autoscaling-autoscalinggroup-instancerequirements-vcpucount""", alias="VCpuCount")
    AllowedInstanceTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancerequirements.html#cfn-autoscaling-autoscalinggroup-instancerequirements-allowedinstancetypes""", alias="AllowedInstanceTypes")
    LocalStorage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancerequirements.html#cfn-autoscaling-autoscalinggroup-instancerequirements-localstorage""", alias="LocalStorage")
    CpuManufacturers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancerequirements.html#cfn-autoscaling-autoscalinggroup-instancerequirements-cpumanufacturers""", alias="CpuManufacturers")
    AcceleratorCount_: Optional['AcceleratorCountRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancerequirements.html#cfn-autoscaling-autoscalinggroup-instancerequirements-acceleratorcount""", alias="AcceleratorCount")
    NetworkBandwidthGbps_: Optional['NetworkBandwidthGbpsRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancerequirements.html#cfn-autoscaling-autoscalinggroup-instancerequirements-networkbandwidthgbps""", alias="NetworkBandwidthGbps")
    BareMetal_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancerequirements.html#cfn-autoscaling-autoscalinggroup-instancerequirements-baremetal""", alias="BareMetal")
    RequireHibernateSupport_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancerequirements.html#cfn-autoscaling-autoscalinggroup-instancerequirements-requirehibernatesupport""", alias="RequireHibernateSupport")
    BaselineEbsBandwidthMbps_: Optional['BaselineEbsBandwidthMbpsRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancerequirements.html#cfn-autoscaling-autoscalinggroup-instancerequirements-baselineebsbandwidthmbps""", alias="BaselineEbsBandwidthMbps")
    SpotMaxPricePercentageOverLowestPrice_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancerequirements.html#cfn-autoscaling-autoscalinggroup-instancerequirements-spotmaxpricepercentageoverlowestprice""", alias="SpotMaxPricePercentageOverLowestPrice")
    AcceleratorNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancerequirements.html#cfn-autoscaling-autoscalinggroup-instancerequirements-acceleratornames""", alias="AcceleratorNames")
    AcceleratorTotalMemoryMiB_: Optional['AcceleratorTotalMemoryMiBRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancerequirements.html#cfn-autoscaling-autoscalinggroup-instancerequirements-acceleratortotalmemorymib""", alias="AcceleratorTotalMemoryMiB")
    OnDemandMaxPricePercentageOverLowestPrice_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancerequirements.html#cfn-autoscaling-autoscalinggroup-instancerequirements-ondemandmaxpricepercentageoverlowestprice""", alias="OnDemandMaxPricePercentageOverLowestPrice")
    BurstablePerformance_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancerequirements.html#cfn-autoscaling-autoscalinggroup-instancerequirements-burstableperformance""", alias="BurstablePerformance")
    MemoryMiB_: Optional['MemoryMiBRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancerequirements.html#cfn-autoscaling-autoscalinggroup-instancerequirements-memorymib""", alias="MemoryMiB")
    TotalLocalStorageGB_: Optional['TotalLocalStorageGBRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancerequirements.html#cfn-autoscaling-autoscalinggroup-instancerequirements-totallocalstoragegb""", alias="TotalLocalStorageGB")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.InstanceRequirements:
        from troposphere.autoscaling import InstanceRequirements as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InstancesDistribution(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancesdistribution.html
    Properties:
        - Name: OnDemandAllocationStrategy
        - Name: OnDemandBaseCapacity
        - Name: OnDemandPercentageAboveBaseCapacity
        - Name: SpotInstancePools
        - Name: SpotAllocationStrategy
        - Name: SpotMaxPrice
    
    """
    
    OnDemandAllocationStrategy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancesdistribution.html#cfn-autoscaling-autoscalinggroup-instancesdistribution-ondemandallocationstrategy""", alias="OnDemandAllocationStrategy")
    OnDemandBaseCapacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancesdistribution.html#cfn-autoscaling-autoscalinggroup-instancesdistribution-ondemandbasecapacity""", alias="OnDemandBaseCapacity")
    OnDemandPercentageAboveBaseCapacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancesdistribution.html#cfn-autoscaling-autoscalinggroup-instancesdistribution-ondemandpercentageabovebasecapacity""", alias="OnDemandPercentageAboveBaseCapacity")
    SpotInstancePools_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancesdistribution.html#cfn-autoscaling-autoscalinggroup-instancesdistribution-spotinstancepools""", alias="SpotInstancePools")
    SpotAllocationStrategy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancesdistribution.html#cfn-autoscaling-autoscalinggroup-instancesdistribution-spotallocationstrategy""", alias="SpotAllocationStrategy")
    SpotMaxPrice_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancesdistribution.html#cfn-autoscaling-autoscalinggroup-instancesdistribution-spotmaxprice""", alias="SpotMaxPrice")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.InstancesDistribution:
        from troposphere.autoscaling import InstancesDistribution as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LaunchTemplate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-launchtemplate.html
    Properties:
        - Name: LaunchTemplateSpecification
        - Name: Overrides
    
    """
    
    LaunchTemplateSpecification_: 'LaunchTemplateSpecification' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-launchtemplate.html#cfn-autoscaling-autoscalinggroup-launchtemplate-launchtemplatespecification""", alias="LaunchTemplateSpecification")
    Overrides_: Optional[List['LaunchTemplateOverrides']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-launchtemplate.html#cfn-autoscaling-autoscalinggroup-launchtemplate-overrides""", alias="Overrides")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.LaunchTemplate:
        from troposphere.autoscaling import LaunchTemplate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LaunchTemplateOverrides(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-launchtemplateoverrides.html
    Properties:
        - Name: LaunchTemplateSpecification
        - Name: WeightedCapacity
        - Name: InstanceRequirements
        - Name: InstanceType
    
    """
    
    LaunchTemplateSpecification_: Optional['LaunchTemplateSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-launchtemplateoverrides.html#cfn-autoscaling-autoscalinggroup-launchtemplateoverrides-launchtemplatespecification""", alias="LaunchTemplateSpecification")
    WeightedCapacity_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-launchtemplateoverrides.html#cfn-autoscaling-autoscalinggroup-launchtemplateoverrides-weightedcapacity""", alias="WeightedCapacity")
    InstanceRequirements_: Optional['InstanceRequirements'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-launchtemplateoverrides.html#cfn-autoscaling-autoscalinggroup-launchtemplateoverrides-instancerequirements""", alias="InstanceRequirements")
    InstanceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-launchtemplateoverrides.html#cfn-autoscaling-autoscalinggroup-launchtemplateoverrides-instancetype""", alias="InstanceType")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.LaunchTemplateOverrides:
        from troposphere.autoscaling import LaunchTemplateOverrides as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LaunchTemplateSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-launchtemplatespecification.html
    Properties:
        - Name: LaunchTemplateName
        - Name: Version
        - Name: LaunchTemplateId
    
    """
    
    LaunchTemplateName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-launchtemplatespecification.html#cfn-autoscaling-autoscalinggroup-launchtemplatespecification-launchtemplatename""", alias="LaunchTemplateName")
    Version_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-launchtemplatespecification.html#cfn-autoscaling-autoscalinggroup-launchtemplatespecification-version""", alias="Version")
    LaunchTemplateId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-launchtemplatespecification.html#cfn-autoscaling-autoscalinggroup-launchtemplatespecification-launchtemplateid""", alias="LaunchTemplateId")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.LaunchTemplateSpecification:
        from troposphere.autoscaling import LaunchTemplateSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LifecycleHookSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-lifecyclehookspecification.html
    Properties:
        - Name: LifecycleHookName
        - Name: LifecycleTransition
        - Name: HeartbeatTimeout
        - Name: NotificationMetadata
        - Name: DefaultResult
        - Name: NotificationTargetARN
        - Name: RoleARN
    
    """
    
    LifecycleHookName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-lifecyclehookspecification.html#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-lifecyclehookname""", alias="LifecycleHookName")
    LifecycleTransition_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-lifecyclehookspecification.html#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-lifecycletransition""", alias="LifecycleTransition")
    HeartbeatTimeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-lifecyclehookspecification.html#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-heartbeattimeout""", alias="HeartbeatTimeout")
    NotificationMetadata_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-lifecyclehookspecification.html#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-notificationmetadata""", alias="NotificationMetadata")
    DefaultResult_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-lifecyclehookspecification.html#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-defaultresult""", alias="DefaultResult")
    NotificationTargetARN_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-lifecyclehookspecification.html#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-notificationtargetarn""", alias="NotificationTargetARN")
    RoleARN_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-lifecyclehookspecification.html#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-rolearn""", alias="RoleARN")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.LifecycleHookSpecification:
        from troposphere.autoscaling import LifecycleHookSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MemoryGiBPerVCpuRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-memorygibpervcpurequest.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-memorygibpervcpurequest.html#cfn-autoscaling-autoscalinggroup-memorygibpervcpurequest-min""", alias="Min")
    Max_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-memorygibpervcpurequest.html#cfn-autoscaling-autoscalinggroup-memorygibpervcpurequest-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.MemoryGiBPerVCpuRequest:
        from troposphere.autoscaling import MemoryGiBPerVCpuRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MemoryMiBRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-memorymibrequest.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-memorymibrequest.html#cfn-autoscaling-autoscalinggroup-memorymibrequest-min""", alias="Min")
    Max_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-memorymibrequest.html#cfn-autoscaling-autoscalinggroup-memorymibrequest-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.MemoryMiBRequest:
        from troposphere.autoscaling import MemoryMiBRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetricsCollection(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-metricscollection.html
    Properties:
        - Name: Metrics
        - Name: Granularity
    
    """
    
    Metrics_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-metricscollection.html#cfn-autoscaling-autoscalinggroup-metricscollection-metrics""", alias="Metrics")
    Granularity_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-metricscollection.html#cfn-autoscaling-autoscalinggroup-metricscollection-granularity""", alias="Granularity")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.MetricsCollection:
        from troposphere.autoscaling import MetricsCollection as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MixedInstancesPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-mixedinstancespolicy.html
    Properties:
        - Name: InstancesDistribution
        - Name: LaunchTemplate
    
    """
    
    InstancesDistribution_: Optional['InstancesDistribution'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-mixedinstancespolicy.html#cfn-autoscaling-autoscalinggroup-mixedinstancespolicy-instancesdistribution""", alias="InstancesDistribution")
    LaunchTemplate_: 'LaunchTemplate' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-mixedinstancespolicy.html#cfn-autoscaling-autoscalinggroup-mixedinstancespolicy-launchtemplate""", alias="LaunchTemplate")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.MixedInstancesPolicy:
        from troposphere.autoscaling import MixedInstancesPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkBandwidthGbpsRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-networkbandwidthgbpsrequest.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-networkbandwidthgbpsrequest.html#cfn-autoscaling-autoscalinggroup-networkbandwidthgbpsrequest-min""", alias="Min")
    Max_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-networkbandwidthgbpsrequest.html#cfn-autoscaling-autoscalinggroup-networkbandwidthgbpsrequest-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.NetworkBandwidthGbpsRequest:
        from troposphere.autoscaling import NetworkBandwidthGbpsRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkInterfaceCountRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-networkinterfacecountrequest.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-networkinterfacecountrequest.html#cfn-autoscaling-autoscalinggroup-networkinterfacecountrequest-min""", alias="Min")
    Max_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-networkinterfacecountrequest.html#cfn-autoscaling-autoscalinggroup-networkinterfacecountrequest-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.NetworkInterfaceCountRequest:
        from troposphere.autoscaling import NetworkInterfaceCountRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NotificationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-notificationconfiguration.html
    Properties:
        - Name: TopicARN
        - Name: NotificationTypes
    
    """
    
    TopicARN_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-notificationconfiguration.html#cfn-autoscaling-autoscalinggroup-notificationconfiguration-topicarn""", alias="TopicARN")
    NotificationTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-notificationconfiguration.html#cfn-autoscaling-autoscalinggroup-notificationconfiguration-notificationtypes""", alias="NotificationTypes")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.NotificationConfiguration:
        from troposphere.autoscaling import NotificationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TagProperty(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-tagproperty.html
    Properties:
        - Name: Value
        - Name: Key
        - Name: PropagateAtLaunch
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-tagproperty.html#cfn-autoscaling-autoscalinggroup-tagproperty-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-tagproperty.html#cfn-autoscaling-autoscalinggroup-tagproperty-key""", alias="Key")
    PropagateAtLaunch_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-tagproperty.html#cfn-autoscaling-autoscalinggroup-tagproperty-propagateatlaunch""", alias="PropagateAtLaunch")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.TagProperty:
        from troposphere.autoscaling import TagProperty as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TotalLocalStorageGBRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-totallocalstoragegbrequest.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-totallocalstoragegbrequest.html#cfn-autoscaling-autoscalinggroup-totallocalstoragegbrequest-min""", alias="Min")
    Max_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-totallocalstoragegbrequest.html#cfn-autoscaling-autoscalinggroup-totallocalstoragegbrequest-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.TotalLocalStorageGBRequest:
        from troposphere.autoscaling import TotalLocalStorageGBRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VCpuCountRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-vcpucountrequest.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-vcpucountrequest.html#cfn-autoscaling-autoscalinggroup-vcpucountrequest-min""", alias="Min")
    Max_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-vcpucountrequest.html#cfn-autoscaling-autoscalinggroup-vcpucountrequest-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.VCpuCountRequest:
        from troposphere.autoscaling import VCpuCountRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BlockDevice(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-launchconfiguration-blockdevice.html
    Properties:
        - Name: SnapshotId
        - Name: VolumeType
        - Name: Encrypted
        - Name: Throughput
        - Name: Iops
        - Name: VolumeSize
        - Name: DeleteOnTermination
    
    """
    
    SnapshotId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-launchconfiguration-blockdevice.html#cfn-autoscaling-launchconfiguration-blockdevice-snapshotid""", alias="SnapshotId")
    VolumeType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-launchconfiguration-blockdevice.html#cfn-autoscaling-launchconfiguration-blockdevice-volumetype""", alias="VolumeType")
    Encrypted_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-launchconfiguration-blockdevice.html#cfn-autoscaling-launchconfiguration-blockdevice-encrypted""", alias="Encrypted")
    Throughput_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-launchconfiguration-blockdevice.html#cfn-autoscaling-launchconfiguration-blockdevice-throughput""", alias="Throughput")
    Iops_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-launchconfiguration-blockdevice.html#cfn-autoscaling-launchconfiguration-blockdevice-iops""", alias="Iops")
    VolumeSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-launchconfiguration-blockdevice.html#cfn-autoscaling-launchconfiguration-blockdevice-volumesize""", alias="VolumeSize")
    DeleteOnTermination_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-launchconfiguration-blockdevice.html#cfn-autoscaling-launchconfiguration-blockdevice-deleteontermination""", alias="DeleteOnTermination")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.BlockDevice:
        from troposphere.autoscaling import BlockDevice as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BlockDeviceMapping(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-launchconfiguration-blockdevicemapping.html
    Properties:
        - Name: Ebs
        - Name: NoDevice
        - Name: VirtualName
        - Name: DeviceName
    
    """
    
    Ebs_: Optional['BlockDevice'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-launchconfiguration-blockdevicemapping.html#cfn-autoscaling-launchconfiguration-blockdevicemapping-ebs""", alias="Ebs")
    NoDevice_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-launchconfiguration-blockdevicemapping.html#cfn-autoscaling-launchconfiguration-blockdevicemapping-nodevice""", alias="NoDevice")
    VirtualName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-launchconfiguration-blockdevicemapping.html#cfn-autoscaling-launchconfiguration-blockdevicemapping-virtualname""", alias="VirtualName")
    DeviceName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-launchconfiguration-blockdevicemapping.html#cfn-autoscaling-launchconfiguration-blockdevicemapping-devicename""", alias="DeviceName")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.BlockDeviceMapping:
        from troposphere.autoscaling import BlockDeviceMapping as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetadataOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-launchconfiguration-metadataoptions.html
    Properties:
        - Name: HttpPutResponseHopLimit
        - Name: HttpTokens
        - Name: HttpEndpoint
    
    """
    
    HttpPutResponseHopLimit_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-launchconfiguration-metadataoptions.html#cfn-autoscaling-launchconfiguration-metadataoptions-httpputresponsehoplimit""", alias="HttpPutResponseHopLimit")
    HttpTokens_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-launchconfiguration-metadataoptions.html#cfn-autoscaling-launchconfiguration-metadataoptions-httptokens""", alias="HttpTokens")
    HttpEndpoint_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-launchconfiguration-metadataoptions.html#cfn-autoscaling-launchconfiguration-metadataoptions-httpendpoint""", alias="HttpEndpoint")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.MetadataOptions:
        from troposphere.autoscaling import MetadataOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomizedMetricSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-customizedmetricspecification.html
    Properties:
        - Name: MetricName
        - Name: Statistic
        - Name: Dimensions
        - Name: Unit
        - Name: Namespace
    
    """
    
    MetricName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-customizedmetricspecification.html#cfn-autoscaling-scalingpolicy-customizedmetricspecification-metricname""", alias="MetricName")
    Statistic_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-customizedmetricspecification.html#cfn-autoscaling-scalingpolicy-customizedmetricspecification-statistic""", alias="Statistic")
    Dimensions_: Optional[List['MetricDimension']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-customizedmetricspecification.html#cfn-autoscaling-scalingpolicy-customizedmetricspecification-dimensions""", alias="Dimensions")
    Unit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-customizedmetricspecification.html#cfn-autoscaling-scalingpolicy-customizedmetricspecification-unit""", alias="Unit")
    Namespace_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-customizedmetricspecification.html#cfn-autoscaling-scalingpolicy-customizedmetricspecification-namespace""", alias="Namespace")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.CustomizedMetricSpecification:
        from troposphere.autoscaling import CustomizedMetricSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Metric(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-metric.html
    Properties:
        - Name: MetricName
        - Name: Dimensions
        - Name: Namespace
    
    """
    
    MetricName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-metric.html#cfn-autoscaling-scalingpolicy-metric-metricname""", alias="MetricName")
    Dimensions_: Optional[List['MetricDimension']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-metric.html#cfn-autoscaling-scalingpolicy-metric-dimensions""", alias="Dimensions")
    Namespace_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-metric.html#cfn-autoscaling-scalingpolicy-metric-namespace""", alias="Namespace")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.Metric:
        from troposphere.autoscaling import Metric as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetricDataQuery(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-metricdataquery.html
    Properties:
        - Name: ReturnData
        - Name: Expression
        - Name: Label
        - Name: MetricStat
        - Name: Id
    
    """
    
    ReturnData_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-metricdataquery.html#cfn-autoscaling-scalingpolicy-metricdataquery-returndata""", alias="ReturnData")
    Expression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-metricdataquery.html#cfn-autoscaling-scalingpolicy-metricdataquery-expression""", alias="Expression")
    Label_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-metricdataquery.html#cfn-autoscaling-scalingpolicy-metricdataquery-label""", alias="Label")
    MetricStat_: Optional['MetricStat'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-metricdataquery.html#cfn-autoscaling-scalingpolicy-metricdataquery-metricstat""", alias="MetricStat")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-metricdataquery.html#cfn-autoscaling-scalingpolicy-metricdataquery-id""", alias="Id")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.MetricDataQuery:
        from troposphere.autoscaling import MetricDataQuery as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetricDimension(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-metricdimension.html
    Properties:
        - Name: Value
        - Name: Name
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-metricdimension.html#cfn-autoscaling-scalingpolicy-metricdimension-value""", alias="Value")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-metricdimension.html#cfn-autoscaling-scalingpolicy-metricdimension-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.MetricDimension:
        from troposphere.autoscaling import MetricDimension as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetricStat(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-metricstat.html
    Properties:
        - Name: Stat
        - Name: Metric
        - Name: Unit
    
    """
    
    Stat_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-metricstat.html#cfn-autoscaling-scalingpolicy-metricstat-stat""", alias="Stat")
    Metric_: 'Metric' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-metricstat.html#cfn-autoscaling-scalingpolicy-metricstat-metric""", alias="Metric")
    Unit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-metricstat.html#cfn-autoscaling-scalingpolicy-metricstat-unit""", alias="Unit")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.MetricStat:
        from troposphere.autoscaling import MetricStat as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PredefinedMetricSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predefinedmetricspecification.html
    Properties:
        - Name: PredefinedMetricType
        - Name: ResourceLabel
    
    """
    
    PredefinedMetricType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predefinedmetricspecification.html#cfn-autoscaling-scalingpolicy-predefinedmetricspecification-predefinedmetrictype""", alias="PredefinedMetricType")
    ResourceLabel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predefinedmetricspecification.html#cfn-autoscaling-scalingpolicy-predefinedmetricspecification-resourcelabel""", alias="ResourceLabel")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.PredefinedMetricSpecification:
        from troposphere.autoscaling import PredefinedMetricSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PredictiveScalingConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingconfiguration.html
    Properties:
        - Name: MaxCapacityBreachBehavior
        - Name: MaxCapacityBuffer
        - Name: Mode
        - Name: MetricSpecifications
        - Name: SchedulingBufferTime
    
    """
    
    MaxCapacityBreachBehavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingconfiguration.html#cfn-autoscaling-scalingpolicy-predictivescalingconfiguration-maxcapacitybreachbehavior""", alias="MaxCapacityBreachBehavior")
    MaxCapacityBuffer_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingconfiguration.html#cfn-autoscaling-scalingpolicy-predictivescalingconfiguration-maxcapacitybuffer""", alias="MaxCapacityBuffer")
    Mode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingconfiguration.html#cfn-autoscaling-scalingpolicy-predictivescalingconfiguration-mode""", alias="Mode")
    MetricSpecifications_: List['PredictiveScalingMetricSpecification'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingconfiguration.html#cfn-autoscaling-scalingpolicy-predictivescalingconfiguration-metricspecifications""", alias="MetricSpecifications")
    SchedulingBufferTime_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingconfiguration.html#cfn-autoscaling-scalingpolicy-predictivescalingconfiguration-schedulingbuffertime""", alias="SchedulingBufferTime")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.PredictiveScalingConfiguration:
        from troposphere.autoscaling import PredictiveScalingConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PredictiveScalingCustomizedCapacityMetric(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingcustomizedcapacitymetric.html
    Properties:
        - Name: MetricDataQueries
    
    """
    
    MetricDataQueries_: List['MetricDataQuery'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingcustomizedcapacitymetric.html#cfn-autoscaling-scalingpolicy-predictivescalingcustomizedcapacitymetric-metricdataqueries""", alias="MetricDataQueries")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.PredictiveScalingCustomizedCapacityMetric:
        from troposphere.autoscaling import PredictiveScalingCustomizedCapacityMetric as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PredictiveScalingCustomizedLoadMetric(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingcustomizedloadmetric.html
    Properties:
        - Name: MetricDataQueries
    
    """
    
    MetricDataQueries_: List['MetricDataQuery'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingcustomizedloadmetric.html#cfn-autoscaling-scalingpolicy-predictivescalingcustomizedloadmetric-metricdataqueries""", alias="MetricDataQueries")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.PredictiveScalingCustomizedLoadMetric:
        from troposphere.autoscaling import PredictiveScalingCustomizedLoadMetric as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PredictiveScalingCustomizedScalingMetric(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingcustomizedscalingmetric.html
    Properties:
        - Name: MetricDataQueries
    
    """
    
    MetricDataQueries_: List['MetricDataQuery'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingcustomizedscalingmetric.html#cfn-autoscaling-scalingpolicy-predictivescalingcustomizedscalingmetric-metricdataqueries""", alias="MetricDataQueries")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.PredictiveScalingCustomizedScalingMetric:
        from troposphere.autoscaling import PredictiveScalingCustomizedScalingMetric as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PredictiveScalingMetricSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingmetricspecification.html
    Properties:
        - Name: CustomizedLoadMetricSpecification
        - Name: PredefinedLoadMetricSpecification
        - Name: TargetValue
        - Name: PredefinedScalingMetricSpecification
        - Name: CustomizedCapacityMetricSpecification
        - Name: CustomizedScalingMetricSpecification
        - Name: PredefinedMetricPairSpecification
    
    """
    
    CustomizedLoadMetricSpecification_: Optional['PredictiveScalingCustomizedLoadMetric'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingmetricspecification.html#cfn-autoscaling-scalingpolicy-predictivescalingmetricspecification-customizedloadmetricspecification""", alias="CustomizedLoadMetricSpecification")
    PredefinedLoadMetricSpecification_: Optional['PredictiveScalingPredefinedLoadMetric'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingmetricspecification.html#cfn-autoscaling-scalingpolicy-predictivescalingmetricspecification-predefinedloadmetricspecification""", alias="PredefinedLoadMetricSpecification")
    TargetValue_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingmetricspecification.html#cfn-autoscaling-scalingpolicy-predictivescalingmetricspecification-targetvalue""", alias="TargetValue")
    PredefinedScalingMetricSpecification_: Optional['PredictiveScalingPredefinedScalingMetric'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingmetricspecification.html#cfn-autoscaling-scalingpolicy-predictivescalingmetricspecification-predefinedscalingmetricspecification""", alias="PredefinedScalingMetricSpecification")
    CustomizedCapacityMetricSpecification_: Optional['PredictiveScalingCustomizedCapacityMetric'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingmetricspecification.html#cfn-autoscaling-scalingpolicy-predictivescalingmetricspecification-customizedcapacitymetricspecification""", alias="CustomizedCapacityMetricSpecification")
    CustomizedScalingMetricSpecification_: Optional['PredictiveScalingCustomizedScalingMetric'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingmetricspecification.html#cfn-autoscaling-scalingpolicy-predictivescalingmetricspecification-customizedscalingmetricspecification""", alias="CustomizedScalingMetricSpecification")
    PredefinedMetricPairSpecification_: Optional['PredictiveScalingPredefinedMetricPair'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingmetricspecification.html#cfn-autoscaling-scalingpolicy-predictivescalingmetricspecification-predefinedmetricpairspecification""", alias="PredefinedMetricPairSpecification")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.PredictiveScalingMetricSpecification:
        from troposphere.autoscaling import PredictiveScalingMetricSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PredictiveScalingPredefinedLoadMetric(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingpredefinedloadmetric.html
    Properties:
        - Name: PredefinedMetricType
        - Name: ResourceLabel
    
    """
    
    PredefinedMetricType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingpredefinedloadmetric.html#cfn-autoscaling-scalingpolicy-predictivescalingpredefinedloadmetric-predefinedmetrictype""", alias="PredefinedMetricType")
    ResourceLabel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingpredefinedloadmetric.html#cfn-autoscaling-scalingpolicy-predictivescalingpredefinedloadmetric-resourcelabel""", alias="ResourceLabel")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.PredictiveScalingPredefinedLoadMetric:
        from troposphere.autoscaling import PredictiveScalingPredefinedLoadMetric as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PredictiveScalingPredefinedMetricPair(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingpredefinedmetricpair.html
    Properties:
        - Name: PredefinedMetricType
        - Name: ResourceLabel
    
    """
    
    PredefinedMetricType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingpredefinedmetricpair.html#cfn-autoscaling-scalingpolicy-predictivescalingpredefinedmetricpair-predefinedmetrictype""", alias="PredefinedMetricType")
    ResourceLabel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingpredefinedmetricpair.html#cfn-autoscaling-scalingpolicy-predictivescalingpredefinedmetricpair-resourcelabel""", alias="ResourceLabel")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.PredictiveScalingPredefinedMetricPair:
        from troposphere.autoscaling import PredictiveScalingPredefinedMetricPair as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PredictiveScalingPredefinedScalingMetric(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingpredefinedscalingmetric.html
    Properties:
        - Name: PredefinedMetricType
        - Name: ResourceLabel
    
    """
    
    PredefinedMetricType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingpredefinedscalingmetric.html#cfn-autoscaling-scalingpolicy-predictivescalingpredefinedscalingmetric-predefinedmetrictype""", alias="PredefinedMetricType")
    ResourceLabel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingpredefinedscalingmetric.html#cfn-autoscaling-scalingpolicy-predictivescalingpredefinedscalingmetric-resourcelabel""", alias="ResourceLabel")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.PredictiveScalingPredefinedScalingMetric:
        from troposphere.autoscaling import PredictiveScalingPredefinedScalingMetric as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StepAdjustment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-stepadjustment.html
    Properties:
        - Name: MetricIntervalUpperBound
        - Name: MetricIntervalLowerBound
        - Name: ScalingAdjustment
    
    """
    
    MetricIntervalUpperBound_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-stepadjustment.html#cfn-autoscaling-scalingpolicy-stepadjustment-metricintervalupperbound""", alias="MetricIntervalUpperBound")
    MetricIntervalLowerBound_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-stepadjustment.html#cfn-autoscaling-scalingpolicy-stepadjustment-metricintervallowerbound""", alias="MetricIntervalLowerBound")
    ScalingAdjustment_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-stepadjustment.html#cfn-autoscaling-scalingpolicy-stepadjustment-scalingadjustment""", alias="ScalingAdjustment")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.StepAdjustment:
        from troposphere.autoscaling import StepAdjustment as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TargetTrackingConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-targettrackingconfiguration.html
    Properties:
        - Name: TargetValue
        - Name: CustomizedMetricSpecification
        - Name: DisableScaleIn
        - Name: PredefinedMetricSpecification
    
    """
    
    TargetValue_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-targettrackingconfiguration.html#cfn-autoscaling-scalingpolicy-targettrackingconfiguration-targetvalue""", alias="TargetValue")
    CustomizedMetricSpecification_: Optional['CustomizedMetricSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-targettrackingconfiguration.html#cfn-autoscaling-scalingpolicy-targettrackingconfiguration-customizedmetricspecification""", alias="CustomizedMetricSpecification")
    DisableScaleIn_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-targettrackingconfiguration.html#cfn-autoscaling-scalingpolicy-targettrackingconfiguration-disablescalein""", alias="DisableScaleIn")
    PredefinedMetricSpecification_: Optional['PredefinedMetricSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-targettrackingconfiguration.html#cfn-autoscaling-scalingpolicy-targettrackingconfiguration-predefinedmetricspecification""", alias="PredefinedMetricSpecification")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.TargetTrackingConfiguration:
        from troposphere.autoscaling import TargetTrackingConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InstanceReusePolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-warmpool-instancereusepolicy.html
    Properties:
        - Name: ReuseOnScaleIn
    
    """
    
    ReuseOnScaleIn_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-warmpool-instancereusepolicy.html#cfn-autoscaling-warmpool-instancereusepolicy-reuseonscalein""", alias="ReuseOnScaleIn")
    


    @property
    def tropo_type(self) -> troposphere.autoscaling.InstanceReusePolicy:
        from troposphere.autoscaling import InstanceReusePolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class AutoScalingGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html
    Properties:
        - Name: LifecycleHookSpecificationList
        - Name: LoadBalancerNames
        - Name: LaunchConfigurationName
        - Name: ServiceLinkedRoleARN
        - Name: TargetGroupARNs
        - Name: Cooldown
        - Name: NotificationConfigurations
        - Name: DesiredCapacity
        - Name: HealthCheckGracePeriod
        - Name: DefaultInstanceWarmup
        - Name: NewInstancesProtectedFromScaleIn
        - Name: LaunchTemplate
        - Name: MixedInstancesPolicy
        - Name: VPCZoneIdentifier
        - Name: Tags
        - Name: Context
        - Name: CapacityRebalance
        - Name: InstanceId
        - Name: AvailabilityZones
        - Name: MetricsCollection
        - Name: InstanceMaintenancePolicy
        - Name: MaxSize
        - Name: MinSize
        - Name: TerminationPolicies
        - Name: AutoScalingGroupName
        - Name: DesiredCapacityType
        - Name: PlacementGroup
        - Name: HealthCheckType
        - Name: MaxInstanceLifetime
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    LifecycleHookSpecificationList_: Optional[List['LifecycleHookSpecification']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html#cfn-autoscaling-autoscalinggroup-lifecyclehookspecificationlist""", alias="LifecycleHookSpecificationList")
    LoadBalancerNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html#cfn-autoscaling-autoscalinggroup-loadbalancernames""", alias="LoadBalancerNames")
    LaunchConfigurationName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html#cfn-autoscaling-autoscalinggroup-launchconfigurationname""", alias="LaunchConfigurationName")
    ServiceLinkedRoleARN_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html#cfn-autoscaling-autoscalinggroup-servicelinkedrolearn""", alias="ServiceLinkedRoleARN")
    TargetGroupARNs_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html#cfn-autoscaling-autoscalinggroup-targetgrouparns""", alias="TargetGroupARNs")
    Cooldown_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html#cfn-autoscaling-autoscalinggroup-cooldown""", alias="Cooldown")
    NotificationConfigurations_: Optional[List['NotificationConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html#cfn-autoscaling-autoscalinggroup-notificationconfigurations""", alias="NotificationConfigurations")
    DesiredCapacity_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html#cfn-autoscaling-autoscalinggroup-desiredcapacity""", alias="DesiredCapacity")
    HealthCheckGracePeriod_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html#cfn-autoscaling-autoscalinggroup-healthcheckgraceperiod""", alias="HealthCheckGracePeriod")
    DefaultInstanceWarmup_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html#cfn-autoscaling-autoscalinggroup-defaultinstancewarmup""", alias="DefaultInstanceWarmup")
    NewInstancesProtectedFromScaleIn_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html#cfn-autoscaling-autoscalinggroup-newinstancesprotectedfromscalein""", alias="NewInstancesProtectedFromScaleIn")
    LaunchTemplate_: Optional['LaunchTemplateSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html#cfn-autoscaling-autoscalinggroup-launchtemplate""", alias="LaunchTemplate")
    MixedInstancesPolicy_: Optional['MixedInstancesPolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html#cfn-autoscaling-autoscalinggroup-mixedinstancespolicy""", alias="MixedInstancesPolicy")
    VPCZoneIdentifier_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html#cfn-autoscaling-autoscalinggroup-vpczoneidentifier""", alias="VPCZoneIdentifier")
    Tags_: Optional[List['TagProperty']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html#cfn-autoscaling-autoscalinggroup-tags""", alias="Tags")
    Context_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html#cfn-autoscaling-autoscalinggroup-context""", alias="Context")
    CapacityRebalance_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html#cfn-autoscaling-autoscalinggroup-capacityrebalance""", alias="CapacityRebalance")
    InstanceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html#cfn-autoscaling-autoscalinggroup-instanceid""", alias="InstanceId")
    AvailabilityZones_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html#cfn-autoscaling-autoscalinggroup-availabilityzones""", alias="AvailabilityZones")
    MetricsCollection_: Optional[List['MetricsCollection']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html#cfn-autoscaling-autoscalinggroup-metricscollection""", alias="MetricsCollection")
    InstanceMaintenancePolicy_: Optional['InstanceMaintenancePolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html#cfn-autoscaling-autoscalinggroup-instancemaintenancepolicy""", alias="InstanceMaintenancePolicy")
    MaxSize_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html#cfn-autoscaling-autoscalinggroup-maxsize""", alias="MaxSize")
    MinSize_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html#cfn-autoscaling-autoscalinggroup-minsize""", alias="MinSize")
    TerminationPolicies_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html#cfn-autoscaling-autoscalinggroup-terminationpolicies""", alias="TerminationPolicies")
    AutoScalingGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html#cfn-autoscaling-autoscalinggroup-autoscalinggroupname""", alias="AutoScalingGroupName")
    DesiredCapacityType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html#cfn-autoscaling-autoscalinggroup-desiredcapacitytype""", alias="DesiredCapacityType")
    PlacementGroup_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html#cfn-autoscaling-autoscalinggroup-placementgroup""", alias="PlacementGroup")
    HealthCheckType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html#cfn-autoscaling-autoscalinggroup-healthchecktype""", alias="HealthCheckType")
    MaxInstanceLifetime_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html#cfn-autoscaling-autoscalinggroup-maxinstancelifetime""", alias="MaxInstanceLifetime")
    

    @property
    def tropo_type(self) -> troposphere.autoscaling.AutoScalingGroup:
        from troposphere.autoscaling import AutoScalingGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.autoscaling import AutoScalingGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class LaunchConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-launchconfiguration.html
    Properties:
        - Name: PlacementTenancy
        - Name: SecurityGroups
        - Name: LaunchConfigurationName
        - Name: MetadataOptions
        - Name: InstanceId
        - Name: UserData
        - Name: ClassicLinkVPCSecurityGroups
        - Name: BlockDeviceMappings
        - Name: IamInstanceProfile
        - Name: KernelId
        - Name: AssociatePublicIpAddress
        - Name: ClassicLinkVPCId
        - Name: EbsOptimized
        - Name: KeyName
        - Name: SpotPrice
        - Name: ImageId
        - Name: InstanceType
        - Name: RamDiskId
        - Name: InstanceMonitoring
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PlacementTenancy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-launchconfiguration.html#cfn-autoscaling-launchconfiguration-placementtenancy""", alias="PlacementTenancy")
    SecurityGroups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-launchconfiguration.html#cfn-autoscaling-launchconfiguration-securitygroups""", alias="SecurityGroups")
    LaunchConfigurationName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-launchconfiguration.html#cfn-autoscaling-launchconfiguration-launchconfigurationname""", alias="LaunchConfigurationName")
    MetadataOptions_: Optional['MetadataOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-launchconfiguration.html#cfn-autoscaling-launchconfiguration-metadataoptions""", alias="MetadataOptions")
    InstanceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-launchconfiguration.html#cfn-autoscaling-launchconfiguration-instanceid""", alias="InstanceId")
    UserData_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-launchconfiguration.html#cfn-autoscaling-launchconfiguration-userdata""", alias="UserData")
    ClassicLinkVPCSecurityGroups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-launchconfiguration.html#cfn-autoscaling-launchconfiguration-classiclinkvpcsecuritygroups""", alias="ClassicLinkVPCSecurityGroups")
    BlockDeviceMappings_: Optional[List['BlockDeviceMapping']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-launchconfiguration.html#cfn-autoscaling-launchconfiguration-blockdevicemappings""", alias="BlockDeviceMappings")
    IamInstanceProfile_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-launchconfiguration.html#cfn-autoscaling-launchconfiguration-iaminstanceprofile""", alias="IamInstanceProfile")
    KernelId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-launchconfiguration.html#cfn-autoscaling-launchconfiguration-kernelid""", alias="KernelId")
    AssociatePublicIpAddress_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-launchconfiguration.html#cfn-autoscaling-launchconfiguration-associatepublicipaddress""", alias="AssociatePublicIpAddress")
    ClassicLinkVPCId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-launchconfiguration.html#cfn-autoscaling-launchconfiguration-classiclinkvpcid""", alias="ClassicLinkVPCId")
    EbsOptimized_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-launchconfiguration.html#cfn-autoscaling-launchconfiguration-ebsoptimized""", alias="EbsOptimized")
    KeyName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-launchconfiguration.html#cfn-autoscaling-launchconfiguration-keyname""", alias="KeyName")
    SpotPrice_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-launchconfiguration.html#cfn-autoscaling-launchconfiguration-spotprice""", alias="SpotPrice")
    ImageId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-launchconfiguration.html#cfn-autoscaling-launchconfiguration-imageid""", alias="ImageId")
    InstanceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-launchconfiguration.html#cfn-autoscaling-launchconfiguration-instancetype""", alias="InstanceType")
    RamDiskId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-launchconfiguration.html#cfn-autoscaling-launchconfiguration-ramdiskid""", alias="RamDiskId")
    InstanceMonitoring_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-launchconfiguration.html#cfn-autoscaling-launchconfiguration-instancemonitoring""", alias="InstanceMonitoring")
    

    @property
    def tropo_type(self) -> troposphere.autoscaling.LaunchConfiguration:
        from troposphere.autoscaling import LaunchConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.autoscaling import LaunchConfiguration as TropoT
        return resource_to_troposphere(self, TropoT)


class LifecycleHook(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-lifecyclehook.html
    Properties:
        - Name: LifecycleHookName
        - Name: LifecycleTransition
        - Name: AutoScalingGroupName
        - Name: HeartbeatTimeout
        - Name: NotificationMetadata
        - Name: DefaultResult
        - Name: NotificationTargetARN
        - Name: RoleARN
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    LifecycleHookName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-lifecyclehook.html#cfn-autoscaling-lifecyclehook-lifecyclehookname""", alias="LifecycleHookName")
    LifecycleTransition_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-lifecyclehook.html#cfn-autoscaling-lifecyclehook-lifecycletransition""", alias="LifecycleTransition")
    AutoScalingGroupName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-lifecyclehook.html#cfn-autoscaling-lifecyclehook-autoscalinggroupname""", alias="AutoScalingGroupName")
    HeartbeatTimeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-lifecyclehook.html#cfn-autoscaling-lifecyclehook-heartbeattimeout""", alias="HeartbeatTimeout")
    NotificationMetadata_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-lifecyclehook.html#cfn-autoscaling-lifecyclehook-notificationmetadata""", alias="NotificationMetadata")
    DefaultResult_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-lifecyclehook.html#cfn-autoscaling-lifecyclehook-defaultresult""", alias="DefaultResult")
    NotificationTargetARN_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-lifecyclehook.html#cfn-autoscaling-lifecyclehook-notificationtargetarn""", alias="NotificationTargetARN")
    RoleARN_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-lifecyclehook.html#cfn-autoscaling-lifecyclehook-rolearn""", alias="RoleARN")
    

    @property
    def tropo_type(self) -> troposphere.autoscaling.LifecycleHook:
        from troposphere.autoscaling import LifecycleHook as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.autoscaling import LifecycleHook as TropoT
        return resource_to_troposphere(self, TropoT)


class ScalingPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-scalingpolicy.html
    Properties:
        - Name: MetricAggregationType
        - Name: PolicyType
        - Name: PredictiveScalingConfiguration
        - Name: ScalingAdjustment
        - Name: Cooldown
        - Name: StepAdjustments
        - Name: AutoScalingGroupName
        - Name: MinAdjustmentMagnitude
        - Name: TargetTrackingConfiguration
        - Name: EstimatedInstanceWarmup
        - Name: AdjustmentType
    Attributes:
        - Name: PolicyName
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MetricAggregationType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-scalingpolicy.html#cfn-autoscaling-scalingpolicy-metricaggregationtype""", alias="MetricAggregationType")
    PolicyType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-scalingpolicy.html#cfn-autoscaling-scalingpolicy-policytype""", alias="PolicyType")
    PredictiveScalingConfiguration_: Optional['PredictiveScalingConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-scalingpolicy.html#cfn-autoscaling-scalingpolicy-predictivescalingconfiguration""", alias="PredictiveScalingConfiguration")
    ScalingAdjustment_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-scalingpolicy.html#cfn-autoscaling-scalingpolicy-scalingadjustment""", alias="ScalingAdjustment")
    Cooldown_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-scalingpolicy.html#cfn-autoscaling-scalingpolicy-cooldown""", alias="Cooldown")
    StepAdjustments_: Optional[List['StepAdjustment']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-scalingpolicy.html#cfn-autoscaling-scalingpolicy-stepadjustments""", alias="StepAdjustments")
    AutoScalingGroupName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-scalingpolicy.html#cfn-autoscaling-scalingpolicy-autoscalinggroupname""", alias="AutoScalingGroupName")
    MinAdjustmentMagnitude_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-scalingpolicy.html#cfn-autoscaling-scalingpolicy-minadjustmentmagnitude""", alias="MinAdjustmentMagnitude")
    TargetTrackingConfiguration_: Optional['TargetTrackingConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-scalingpolicy.html#cfn-autoscaling-scalingpolicy-targettrackingconfiguration""", alias="TargetTrackingConfiguration")
    EstimatedInstanceWarmup_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-scalingpolicy.html#cfn-autoscaling-scalingpolicy-estimatedinstancewarmup""", alias="EstimatedInstanceWarmup")
    AdjustmentType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-scalingpolicy.html#cfn-autoscaling-scalingpolicy-adjustmenttype""", alias="AdjustmentType")
    

    @property
    def tropo_type(self) -> troposphere.autoscaling.ScalingPolicy:
        from troposphere.autoscaling import ScalingPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.autoscaling import ScalingPolicy as TropoT
        return resource_to_troposphere(self, TropoT)


class ScheduledAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-scheduledaction.html
    Properties:
        - Name: MinSize
        - Name: Recurrence
        - Name: TimeZone
        - Name: EndTime
        - Name: AutoScalingGroupName
        - Name: StartTime
        - Name: DesiredCapacity
        - Name: MaxSize
    Attributes:
        - Name: ScheduledActionName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MinSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-scheduledaction.html#cfn-autoscaling-scheduledaction-minsize""", alias="MinSize")
    Recurrence_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-scheduledaction.html#cfn-autoscaling-scheduledaction-recurrence""", alias="Recurrence")
    TimeZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-scheduledaction.html#cfn-autoscaling-scheduledaction-timezone""", alias="TimeZone")
    EndTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-scheduledaction.html#cfn-autoscaling-scheduledaction-endtime""", alias="EndTime")
    AutoScalingGroupName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-scheduledaction.html#cfn-autoscaling-scheduledaction-autoscalinggroupname""", alias="AutoScalingGroupName")
    StartTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-scheduledaction.html#cfn-autoscaling-scheduledaction-starttime""", alias="StartTime")
    DesiredCapacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-scheduledaction.html#cfn-autoscaling-scheduledaction-desiredcapacity""", alias="DesiredCapacity")
    MaxSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-scheduledaction.html#cfn-autoscaling-scheduledaction-maxsize""", alias="MaxSize")
    

    @property
    def tropo_type(self) -> troposphere.autoscaling.ScheduledAction:
        from troposphere.autoscaling import ScheduledAction as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.autoscaling import ScheduledAction as TropoT
        return resource_to_troposphere(self, TropoT)


class WarmPool(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-warmpool.html
    Properties:
        - Name: MinSize
        - Name: MaxGroupPreparedCapacity
        - Name: AutoScalingGroupName
        - Name: PoolState
        - Name: InstanceReusePolicy
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MinSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-warmpool.html#cfn-autoscaling-warmpool-minsize""", alias="MinSize")
    MaxGroupPreparedCapacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-warmpool.html#cfn-autoscaling-warmpool-maxgrouppreparedcapacity""", alias="MaxGroupPreparedCapacity")
    AutoScalingGroupName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-warmpool.html#cfn-autoscaling-warmpool-autoscalinggroupname""", alias="AutoScalingGroupName")
    PoolState_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-warmpool.html#cfn-autoscaling-warmpool-poolstate""", alias="PoolState")
    InstanceReusePolicy_: Optional['InstanceReusePolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-warmpool.html#cfn-autoscaling-warmpool-instancereusepolicy""", alias="InstanceReusePolicy")
    

    @property
    def tropo_type(self) -> troposphere.autoscaling.WarmPool:
        from troposphere.autoscaling import WarmPool as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.autoscaling import WarmPool as TropoT
        return resource_to_troposphere(self, TropoT)

