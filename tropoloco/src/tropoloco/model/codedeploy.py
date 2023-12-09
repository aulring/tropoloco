from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class MinimumHealthyHosts(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-minimumhealthyhosts.html
    Properties:
        - Name: Type
        - Name: Value
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-minimumhealthyhosts.html#cfn-codedeploy-deploymentconfig-minimumhealthyhosts-type""", alias="Type")
    Value_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-minimumhealthyhosts.html#cfn-codedeploy-deploymentconfig-minimumhealthyhosts-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.codedeploy.MinimumHealthyHosts:
        from troposphere.codedeploy import MinimumHealthyHosts as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MinimumHealthyHostsPerZone(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-minimumhealthyhostsperzone.html
    Properties:
        - Name: Type
        - Name: Value
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-minimumhealthyhostsperzone.html#cfn-codedeploy-deploymentconfig-minimumhealthyhostsperzone-type""", alias="Type")
    Value_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-minimumhealthyhostsperzone.html#cfn-codedeploy-deploymentconfig-minimumhealthyhostsperzone-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.codedeploy.MinimumHealthyHostsPerZone:
        from troposphere.codedeploy import MinimumHealthyHostsPerZone as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TimeBasedCanary(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-timebasedcanary.html
    Properties:
        - Name: CanaryPercentage
        - Name: CanaryInterval
    
    """
    
    CanaryPercentage_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-timebasedcanary.html#cfn-codedeploy-deploymentconfig-timebasedcanary-canarypercentage""", alias="CanaryPercentage")
    CanaryInterval_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-timebasedcanary.html#cfn-codedeploy-deploymentconfig-timebasedcanary-canaryinterval""", alias="CanaryInterval")
    


    @property
    def tropo_type(self) -> troposphere.codedeploy.TimeBasedCanary:
        from troposphere.codedeploy import TimeBasedCanary as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TimeBasedLinear(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-timebasedlinear.html
    Properties:
        - Name: LinearInterval
        - Name: LinearPercentage
    
    """
    
    LinearInterval_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-timebasedlinear.html#cfn-codedeploy-deploymentconfig-timebasedlinear-linearinterval""", alias="LinearInterval")
    LinearPercentage_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-timebasedlinear.html#cfn-codedeploy-deploymentconfig-timebasedlinear-linearpercentage""", alias="LinearPercentage")
    


    @property
    def tropo_type(self) -> troposphere.codedeploy.TimeBasedLinear:
        from troposphere.codedeploy import TimeBasedLinear as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TrafficRoutingConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-trafficroutingconfig.html
    Properties:
        - Name: Type
        - Name: TimeBasedLinear
        - Name: TimeBasedCanary
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-trafficroutingconfig.html#cfn-codedeploy-deploymentconfig-trafficroutingconfig-type""", alias="Type")
    TimeBasedLinear_: Optional['TimeBasedLinear'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-trafficroutingconfig.html#cfn-codedeploy-deploymentconfig-trafficroutingconfig-timebasedlinear""", alias="TimeBasedLinear")
    TimeBasedCanary_: Optional['TimeBasedCanary'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-trafficroutingconfig.html#cfn-codedeploy-deploymentconfig-trafficroutingconfig-timebasedcanary""", alias="TimeBasedCanary")
    


    @property
    def tropo_type(self) -> troposphere.codedeploy.TrafficRoutingConfig:
        from troposphere.codedeploy import TrafficRoutingConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ZonalConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-zonalconfig.html
    Properties:
        - Name: MonitorDurationInSeconds
        - Name: MinimumHealthyHostsPerZone
        - Name: FirstZoneMonitorDurationInSeconds
    
    """
    
    MonitorDurationInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-zonalconfig.html#cfn-codedeploy-deploymentconfig-zonalconfig-monitordurationinseconds""", alias="MonitorDurationInSeconds")
    MinimumHealthyHostsPerZone_: Optional['MinimumHealthyHostsPerZone'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-zonalconfig.html#cfn-codedeploy-deploymentconfig-zonalconfig-minimumhealthyhostsperzone""", alias="MinimumHealthyHostsPerZone")
    FirstZoneMonitorDurationInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-zonalconfig.html#cfn-codedeploy-deploymentconfig-zonalconfig-firstzonemonitordurationinseconds""", alias="FirstZoneMonitorDurationInSeconds")
    


    @property
    def tropo_type(self) -> troposphere.codedeploy.ZonalConfig:
        from troposphere.codedeploy import ZonalConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Alarm(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-alarm.html
    Properties:
        - Name: Name
    
    """
    
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-alarm.html#cfn-codedeploy-deploymentgroup-alarm-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.codedeploy.Alarm:
        from troposphere.codedeploy import Alarm as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AlarmConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-alarmconfiguration.html
    Properties:
        - Name: Alarms
        - Name: Enabled
        - Name: IgnorePollAlarmFailure
    
    """
    
    Alarms_: Optional[List['Alarm']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-alarmconfiguration.html#cfn-codedeploy-deploymentgroup-alarmconfiguration-alarms""", alias="Alarms")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-alarmconfiguration.html#cfn-codedeploy-deploymentgroup-alarmconfiguration-enabled""", alias="Enabled")
    IgnorePollAlarmFailure_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-alarmconfiguration.html#cfn-codedeploy-deploymentgroup-alarmconfiguration-ignorepollalarmfailure""", alias="IgnorePollAlarmFailure")
    


    @property
    def tropo_type(self) -> troposphere.codedeploy.AlarmConfiguration:
        from troposphere.codedeploy import AlarmConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AutoRollbackConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-autorollbackconfiguration.html
    Properties:
        - Name: Enabled
        - Name: Events
    
    """
    
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-autorollbackconfiguration.html#cfn-codedeploy-deploymentgroup-autorollbackconfiguration-enabled""", alias="Enabled")
    Events_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-autorollbackconfiguration.html#cfn-codedeploy-deploymentgroup-autorollbackconfiguration-events""", alias="Events")
    


    @property
    def tropo_type(self) -> troposphere.codedeploy.AutoRollbackConfiguration:
        from troposphere.codedeploy import AutoRollbackConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BlueGreenDeploymentConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-bluegreendeploymentconfiguration.html
    Properties:
        - Name: DeploymentReadyOption
        - Name: GreenFleetProvisioningOption
        - Name: TerminateBlueInstancesOnDeploymentSuccess
    
    """
    
    DeploymentReadyOption_: Optional['DeploymentReadyOption'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-bluegreendeploymentconfiguration.html#cfn-codedeploy-deploymentgroup-bluegreendeploymentconfiguration-deploymentreadyoption""", alias="DeploymentReadyOption")
    GreenFleetProvisioningOption_: Optional['GreenFleetProvisioningOption'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-bluegreendeploymentconfiguration.html#cfn-codedeploy-deploymentgroup-bluegreendeploymentconfiguration-greenfleetprovisioningoption""", alias="GreenFleetProvisioningOption")
    TerminateBlueInstancesOnDeploymentSuccess_: Optional['BlueInstanceTerminationOption'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-bluegreendeploymentconfiguration.html#cfn-codedeploy-deploymentgroup-bluegreendeploymentconfiguration-terminateblueinstancesondeploymentsuccess""", alias="TerminateBlueInstancesOnDeploymentSuccess")
    


    @property
    def tropo_type(self) -> troposphere.codedeploy.BlueGreenDeploymentConfiguration:
        from troposphere.codedeploy import BlueGreenDeploymentConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BlueInstanceTerminationOption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-blueinstanceterminationoption.html
    Properties:
        - Name: Action
        - Name: TerminationWaitTimeInMinutes
    
    """
    
    Action_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-blueinstanceterminationoption.html#cfn-codedeploy-deploymentgroup-bluegreendeploymentconfiguration-blueinstanceterminationoption-action""", alias="Action")
    TerminationWaitTimeInMinutes_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-blueinstanceterminationoption.html#cfn-codedeploy-deploymentgroup-bluegreendeploymentconfiguration-blueinstanceterminationoption-terminationwaittimeinminutes""", alias="TerminationWaitTimeInMinutes")
    


    @property
    def tropo_type(self) -> troposphere.codedeploy.BlueInstanceTerminationOption:
        from troposphere.codedeploy import BlueInstanceTerminationOption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Deployment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment.html
    Properties:
        - Name: Description
        - Name: IgnoreApplicationStopFailures
        - Name: Revision
    
    """
    
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment.html#cfn-properties-codedeploy-deploymentgroup-deployment-description""", alias="Description")
    IgnoreApplicationStopFailures_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment.html#cfn-properties-codedeploy-deploymentgroup-deployment-ignoreapplicationstopfailures""", alias="IgnoreApplicationStopFailures")
    Revision_: 'RevisionLocation' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision""", alias="Revision")
    


    @property
    def tropo_type(self) -> troposphere.codedeploy.Deployment:
        from troposphere.codedeploy import Deployment as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeploymentReadyOption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deploymentreadyoption.html
    Properties:
        - Name: ActionOnTimeout
        - Name: WaitTimeInMinutes
    
    """
    
    ActionOnTimeout_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deploymentreadyoption.html#cfn-codedeploy-deploymentgroup-bluegreendeploymentconfiguration-deploymentreadyoption-actionontimeout""", alias="ActionOnTimeout")
    WaitTimeInMinutes_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deploymentreadyoption.html#cfn-codedeploy-deploymentgroup-bluegreendeploymentconfiguration-deploymentreadyoption-waittimeinminutes""", alias="WaitTimeInMinutes")
    


    @property
    def tropo_type(self) -> troposphere.codedeploy.DeploymentReadyOption:
        from troposphere.codedeploy import DeploymentReadyOption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeploymentStyle(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deploymentstyle.html
    Properties:
        - Name: DeploymentOption
        - Name: DeploymentType
    
    """
    
    DeploymentOption_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deploymentstyle.html#cfn-codedeploy-deploymentgroup-deploymentstyle-deploymentoption""", alias="DeploymentOption")
    DeploymentType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deploymentstyle.html#cfn-codedeploy-deploymentgroup-deploymentstyle-deploymenttype""", alias="DeploymentType")
    


    @property
    def tropo_type(self) -> troposphere.codedeploy.DeploymentStyle:
        from troposphere.codedeploy import DeploymentStyle as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EC2TagFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagfilter.html
    Properties:
        - Name: Key
        - Name: Type
        - Name: Value
    
    """
    
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagfilter.html#cfn-codedeploy-deploymentgroup-ec2tagfilter-key""", alias="Key")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagfilter.html#cfn-codedeploy-deploymentgroup-ec2tagfilter-type""", alias="Type")
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagfilter.html#cfn-codedeploy-deploymentgroup-ec2tagfilter-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.codedeploy.EC2TagFilter:
        from troposphere.codedeploy import EC2TagFilter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EC2TagSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagset.html
    Properties:
        - Name: Ec2TagSetList
    
    """
    
    Ec2TagSetList_: Optional[List['EC2TagSetListObject']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagset.html#cfn-codedeploy-deploymentgroup-ec2tagset-ec2tagsetlist""", alias="Ec2TagSetList")
    


    @property
    def tropo_type(self) -> troposphere.codedeploy.EC2TagSet:
        from troposphere.codedeploy import EC2TagSet as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EC2TagSetListObject(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagsetlistobject.html
    Properties:
        - Name: Ec2TagGroup
    
    """
    
    Ec2TagGroup_: Optional[List['EC2TagFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagsetlistobject.html#cfn-codedeploy-deploymentgroup-ec2tagsetlistobject-ec2taggroup""", alias="Ec2TagGroup")
    


    @property
    def tropo_type(self) -> troposphere.codedeploy.EC2TagSetListObject:
        from troposphere.codedeploy import EC2TagSetListObject as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ECSService(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ecsservice.html
    Properties:
        - Name: ClusterName
        - Name: ServiceName
    
    """
    
    ClusterName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ecsservice.html#cfn-codedeploy-deploymentgroup-ecsservice-clustername""", alias="ClusterName")
    ServiceName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ecsservice.html#cfn-codedeploy-deploymentgroup-ecsservice-servicename""", alias="ServiceName")
    


    @property
    def tropo_type(self) -> troposphere.codedeploy.ECSService:
        from troposphere.codedeploy import ECSService as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ELBInfo(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-elbinfo.html
    Properties:
        - Name: Name
    
    """
    
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-elbinfo.html#cfn-codedeploy-deploymentgroup-elbinfo-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.codedeploy.ELBInfo:
        from troposphere.codedeploy import ELBInfo as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GitHubLocation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-githublocation.html
    Properties:
        - Name: CommitId
        - Name: Repository
    
    """
    
    CommitId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-githublocation.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-githublocation-commitid""", alias="CommitId")
    Repository_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-githublocation.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-githublocation-repository""", alias="Repository")
    


    @property
    def tropo_type(self) -> troposphere.codedeploy.GitHubLocation:
        from troposphere.codedeploy import GitHubLocation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GreenFleetProvisioningOption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-greenfleetprovisioningoption.html
    Properties:
        - Name: Action
    
    """
    
    Action_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-greenfleetprovisioningoption.html#cfn-codedeploy-deploymentgroup-bluegreendeploymentconfiguration-greenfleetprovisioningoption-action""", alias="Action")
    


    @property
    def tropo_type(self) -> troposphere.codedeploy.GreenFleetProvisioningOption:
        from troposphere.codedeploy import GreenFleetProvisioningOption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LoadBalancerInfo(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-loadbalancerinfo.html
    Properties:
        - Name: ElbInfoList
        - Name: TargetGroupInfoList
        - Name: TargetGroupPairInfoList
    
    """
    
    ElbInfoList_: Optional[List['ELBInfo']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-loadbalancerinfo.html#cfn-codedeploy-deploymentgroup-loadbalancerinfo-elbinfolist""", alias="ElbInfoList")
    TargetGroupInfoList_: Optional[List['TargetGroupInfo']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-loadbalancerinfo.html#cfn-codedeploy-deploymentgroup-loadbalancerinfo-targetgroupinfolist""", alias="TargetGroupInfoList")
    TargetGroupPairInfoList_: Optional[List['TargetGroupPairInfo']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-loadbalancerinfo.html#cfn-codedeploy-deploymentgroup-loadbalancerinfo-targetgrouppairinfolist""", alias="TargetGroupPairInfoList")
    


    @property
    def tropo_type(self) -> troposphere.codedeploy.LoadBalancerInfo:
        from troposphere.codedeploy import LoadBalancerInfo as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OnPremisesTagSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-onpremisestagset.html
    Properties:
        - Name: OnPremisesTagSetList
    
    """
    
    OnPremisesTagSetList_: Optional[List['OnPremisesTagSetListObject']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-onpremisestagset.html#cfn-codedeploy-deploymentgroup-onpremisestagset-onpremisestagsetlist""", alias="OnPremisesTagSetList")
    


    @property
    def tropo_type(self) -> troposphere.codedeploy.OnPremisesTagSet:
        from troposphere.codedeploy import OnPremisesTagSet as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OnPremisesTagSetListObject(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-onpremisestagsetlistobject.html
    Properties:
        - Name: OnPremisesTagGroup
    
    """
    
    OnPremisesTagGroup_: Optional[List['TagFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-onpremisestagsetlistobject.html#cfn-codedeploy-deploymentgroup-onpremisestagsetlistobject-onpremisestaggroup""", alias="OnPremisesTagGroup")
    


    @property
    def tropo_type(self) -> troposphere.codedeploy.OnPremisesTagSetListObject:
        from troposphere.codedeploy import OnPremisesTagSetListObject as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RevisionLocation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision.html
    Properties:
        - Name: GitHubLocation
        - Name: RevisionType
        - Name: S3Location
    
    """
    
    GitHubLocation_: Optional['GitHubLocation'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-githublocation""", alias="GitHubLocation")
    RevisionType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-revisiontype""", alias="RevisionType")
    S3Location_: Optional['S3Location'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-s3location""", alias="S3Location")
    


    @property
    def tropo_type(self) -> troposphere.codedeploy.RevisionLocation:
        from troposphere.codedeploy import RevisionLocation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Location(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-s3location.html
    Properties:
        - Name: Bucket
        - Name: BundleType
        - Name: ETag
        - Name: Key
        - Name: Version
    
    """
    
    Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-s3location.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-s3location-bucket""", alias="Bucket")
    BundleType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-s3location.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-s3location-bundletype""", alias="BundleType")
    ETag_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-s3location.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-s3location-etag""", alias="ETag")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-s3location.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-s3location-key""", alias="Key")
    Version_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-s3location.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-s3location-value""", alias="Version")
    


    @property
    def tropo_type(self) -> troposphere.codedeploy.S3Location:
        from troposphere.codedeploy import S3Location as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TagFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-tagfilter.html
    Properties:
        - Name: Key
        - Name: Type
        - Name: Value
    
    """
    
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-tagfilter.html#cfn-codedeploy-deploymentgroup-tagfilter-key""", alias="Key")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-tagfilter.html#cfn-codedeploy-deploymentgroup-tagfilter-type""", alias="Type")
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-tagfilter.html#cfn-codedeploy-deploymentgroup-tagfilter-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.codedeploy.TagFilter:
        from troposphere.codedeploy import TagFilter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TargetGroupInfo(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-targetgroupinfo.html
    Properties:
        - Name: Name
    
    """
    
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-targetgroupinfo.html#cfn-codedeploy-deploymentgroup-targetgroupinfo-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.codedeploy.TargetGroupInfo:
        from troposphere.codedeploy import TargetGroupInfo as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TargetGroupPairInfo(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-targetgrouppairinfo.html
    Properties:
        - Name: ProdTrafficRoute
        - Name: TargetGroups
        - Name: TestTrafficRoute
    
    """
    
    ProdTrafficRoute_: Optional['TrafficRoute'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-targetgrouppairinfo.html#cfn-codedeploy-deploymentgroup-targetgrouppairinfo-prodtrafficroute""", alias="ProdTrafficRoute")
    TargetGroups_: Optional[List['TargetGroupInfo']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-targetgrouppairinfo.html#cfn-codedeploy-deploymentgroup-targetgrouppairinfo-targetgroups""", alias="TargetGroups")
    TestTrafficRoute_: Optional['TrafficRoute'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-targetgrouppairinfo.html#cfn-codedeploy-deploymentgroup-targetgrouppairinfo-testtrafficroute""", alias="TestTrafficRoute")
    


    @property
    def tropo_type(self) -> troposphere.codedeploy.TargetGroupPairInfo:
        from troposphere.codedeploy import TargetGroupPairInfo as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TrafficRoute(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-trafficroute.html
    Properties:
        - Name: ListenerArns
    
    """
    
    ListenerArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-trafficroute.html#cfn-codedeploy-deploymentgroup-trafficroute-listenerarns""", alias="ListenerArns")
    


    @property
    def tropo_type(self) -> troposphere.codedeploy.TrafficRoute:
        from troposphere.codedeploy import TrafficRoute as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TriggerConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-triggerconfig.html
    Properties:
        - Name: TriggerEvents
        - Name: TriggerName
        - Name: TriggerTargetArn
    
    """
    
    TriggerEvents_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-triggerconfig.html#cfn-codedeploy-deploymentgroup-triggerconfig-triggerevents""", alias="TriggerEvents")
    TriggerName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-triggerconfig.html#cfn-codedeploy-deploymentgroup-triggerconfig-triggername""", alias="TriggerName")
    TriggerTargetArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-triggerconfig.html#cfn-codedeploy-deploymentgroup-triggerconfig-triggertargetarn""", alias="TriggerTargetArn")
    


    @property
    def tropo_type(self) -> troposphere.codedeploy.TriggerConfig:
        from troposphere.codedeploy import TriggerConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Application(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-application.html
    Properties:
        - Name: ApplicationName
        - Name: ComputePlatform
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ApplicationName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-application.html#cfn-codedeploy-application-applicationname""", alias="ApplicationName")
    ComputePlatform_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-application.html#cfn-codedeploy-application-computeplatform""", alias="ComputePlatform")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-application.html#cfn-codedeploy-application-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.codedeploy.Application:
        from troposphere.codedeploy import Application as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.codedeploy import Application as TropoT
        return resource_to_troposphere(self, TropoT)


class DeploymentConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.html
    Properties:
        - Name: ComputePlatform
        - Name: ZonalConfig
        - Name: DeploymentConfigName
        - Name: TrafficRoutingConfig
        - Name: MinimumHealthyHosts
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ComputePlatform_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.html#cfn-codedeploy-deploymentconfig-computeplatform""", alias="ComputePlatform")
    ZonalConfig_: Optional['ZonalConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.html#cfn-codedeploy-deploymentconfig-zonalconfig""", alias="ZonalConfig")
    DeploymentConfigName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.html#cfn-codedeploy-deploymentconfig-deploymentconfigname""", alias="DeploymentConfigName")
    TrafficRoutingConfig_: Optional['TrafficRoutingConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.html#cfn-codedeploy-deploymentconfig-trafficroutingconfig""", alias="TrafficRoutingConfig")
    MinimumHealthyHosts_: Optional['MinimumHealthyHosts'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.html#cfn-codedeploy-deploymentconfig-minimumhealthyhosts""", alias="MinimumHealthyHosts")
    

    @property
    def tropo_type(self) -> troposphere.codedeploy.DeploymentConfig:
        from troposphere.codedeploy import DeploymentConfig as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.codedeploy import DeploymentConfig as TropoT
        return resource_to_troposphere(self, TropoT)


class DeploymentGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html
    Properties:
        - Name: AlarmConfiguration
        - Name: ApplicationName
        - Name: AutoRollbackConfiguration
        - Name: AutoScalingGroups
        - Name: BlueGreenDeploymentConfiguration
        - Name: Deployment
        - Name: DeploymentConfigName
        - Name: DeploymentGroupName
        - Name: DeploymentStyle
        - Name: ECSServices
        - Name: Ec2TagFilters
        - Name: Ec2TagSet
        - Name: LoadBalancerInfo
        - Name: OnPremisesInstanceTagFilters
        - Name: OnPremisesTagSet
        - Name: OutdatedInstancesStrategy
        - Name: ServiceRoleArn
        - Name: Tags
        - Name: TerminationHookEnabled
        - Name: TriggerConfigurations
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AlarmConfiguration_: Optional['AlarmConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-alarmconfiguration""", alias="AlarmConfiguration")
    ApplicationName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-applicationname""", alias="ApplicationName")
    AutoRollbackConfiguration_: Optional['AutoRollbackConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-autorollbackconfiguration""", alias="AutoRollbackConfiguration")
    AutoScalingGroups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-autoscalinggroups""", alias="AutoScalingGroups")
    BlueGreenDeploymentConfiguration_: Optional['BlueGreenDeploymentConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-bluegreendeploymentconfiguration""", alias="BlueGreenDeploymentConfiguration")
    Deployment_: Optional['Deployment'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-deployment""", alias="Deployment")
    DeploymentConfigName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-deploymentconfigname""", alias="DeploymentConfigName")
    DeploymentGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-deploymentgroupname""", alias="DeploymentGroupName")
    DeploymentStyle_: Optional['DeploymentStyle'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-deploymentstyle""", alias="DeploymentStyle")
    ECSServices_: Optional[List['ECSService']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-ecsservices""", alias="ECSServices")
    Ec2TagFilters_: Optional[List['EC2TagFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-ec2tagfilters""", alias="Ec2TagFilters")
    Ec2TagSet_: Optional['EC2TagSet'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-ec2tagset""", alias="Ec2TagSet")
    LoadBalancerInfo_: Optional['LoadBalancerInfo'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-loadbalancerinfo""", alias="LoadBalancerInfo")
    OnPremisesInstanceTagFilters_: Optional[List['TagFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-onpremisesinstancetagfilters""", alias="OnPremisesInstanceTagFilters")
    OnPremisesTagSet_: Optional['OnPremisesTagSet'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-onpremisestagset""", alias="OnPremisesTagSet")
    OutdatedInstancesStrategy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-outdatedinstancesstrategy""", alias="OutdatedInstancesStrategy")
    ServiceRoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-servicerolearn""", alias="ServiceRoleArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-tags""", alias="Tags")
    TerminationHookEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-terminationhookenabled""", alias="TerminationHookEnabled")
    TriggerConfigurations_: Optional[List['TriggerConfig']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-triggerconfigurations""", alias="TriggerConfigurations")
    

    @property
    def tropo_type(self) -> troposphere.codedeploy.DeploymentGroup:
        from troposphere.codedeploy import DeploymentGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.codedeploy import DeploymentGroup as TropoT
        return resource_to_troposphere(self, TropoT)

