from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AutoScalingGroupProvider(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-capacityprovider-autoscalinggroupprovider.html
    Properties:
        - Name: ManagedScaling
        - Name: AutoScalingGroupArn
        - Name: ManagedTerminationProtection
    
    """
    
    ManagedScaling_: Optional['ManagedScaling'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-capacityprovider-autoscalinggroupprovider.html#cfn-ecs-capacityprovider-autoscalinggroupprovider-managedscaling""", alias="ManagedScaling")
    AutoScalingGroupArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-capacityprovider-autoscalinggroupprovider.html#cfn-ecs-capacityprovider-autoscalinggroupprovider-autoscalinggrouparn""", alias="AutoScalingGroupArn")
    ManagedTerminationProtection_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-capacityprovider-autoscalinggroupprovider.html#cfn-ecs-capacityprovider-autoscalinggroupprovider-managedterminationprotection""", alias="ManagedTerminationProtection")
    


    @property
    def tropo_type(self) -> troposphere.ecs.AutoScalingGroupProvider:
        from troposphere.ecs import AutoScalingGroupProvider as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ManagedScaling(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-capacityprovider-managedscaling.html
    Properties:
        - Name: Status
        - Name: MinimumScalingStepSize
        - Name: InstanceWarmupPeriod
        - Name: TargetCapacity
        - Name: MaximumScalingStepSize
    
    """
    
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-capacityprovider-managedscaling.html#cfn-ecs-capacityprovider-managedscaling-status""", alias="Status")
    MinimumScalingStepSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-capacityprovider-managedscaling.html#cfn-ecs-capacityprovider-managedscaling-minimumscalingstepsize""", alias="MinimumScalingStepSize")
    InstanceWarmupPeriod_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-capacityprovider-managedscaling.html#cfn-ecs-capacityprovider-managedscaling-instancewarmupperiod""", alias="InstanceWarmupPeriod")
    TargetCapacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-capacityprovider-managedscaling.html#cfn-ecs-capacityprovider-managedscaling-targetcapacity""", alias="TargetCapacity")
    MaximumScalingStepSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-capacityprovider-managedscaling.html#cfn-ecs-capacityprovider-managedscaling-maximumscalingstepsize""", alias="MaximumScalingStepSize")
    


    @property
    def tropo_type(self) -> troposphere.ecs.ManagedScaling:
        from troposphere.ecs import ManagedScaling as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CapacityProviderStrategyItem(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-capacityproviderstrategyitem.html
    Properties:
        - Name: CapacityProvider
        - Name: Weight
        - Name: Base
    
    """
    
    CapacityProvider_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-capacityproviderstrategyitem.html#cfn-ecs-cluster-capacityproviderstrategyitem-capacityprovider""", alias="CapacityProvider")
    Weight_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-capacityproviderstrategyitem.html#cfn-ecs-cluster-capacityproviderstrategyitem-weight""", alias="Weight")
    Base_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-capacityproviderstrategyitem.html#cfn-ecs-cluster-capacityproviderstrategyitem-base""", alias="Base")
    


    @property
    def tropo_type(self) -> troposphere.ecs.CapacityProviderStrategyItem:
        from troposphere.ecs import CapacityProviderStrategyItem as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ClusterConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clusterconfiguration.html
    Properties:
        - Name: ExecuteCommandConfiguration
    
    """
    
    ExecuteCommandConfiguration_: Optional['ExecuteCommandConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clusterconfiguration.html#cfn-ecs-cluster-clusterconfiguration-executecommandconfiguration""", alias="ExecuteCommandConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.ecs.ClusterConfiguration:
        from troposphere.ecs import ClusterConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ClusterSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clustersettings.html
    Properties:
        - Name: Value
        - Name: Name
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clustersettings.html#cfn-ecs-cluster-clustersettings-value""", alias="Value")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clustersettings.html#cfn-ecs-cluster-clustersettings-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.ecs.ClusterSetting:
        from troposphere.ecs import ClusterSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ExecuteCommandConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandconfiguration.html
    Properties:
        - Name: Logging
        - Name: KmsKeyId
        - Name: LogConfiguration
    
    """
    
    Logging_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandconfiguration.html#cfn-ecs-cluster-executecommandconfiguration-logging""", alias="Logging")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandconfiguration.html#cfn-ecs-cluster-executecommandconfiguration-kmskeyid""", alias="KmsKeyId")
    LogConfiguration_: Optional['ExecuteCommandLogConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandconfiguration.html#cfn-ecs-cluster-executecommandconfiguration-logconfiguration""", alias="LogConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.ecs.ExecuteCommandConfiguration:
        from troposphere.ecs import ExecuteCommandConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ExecuteCommandLogConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandlogconfiguration.html
    Properties:
        - Name: S3EncryptionEnabled
        - Name: CloudWatchEncryptionEnabled
        - Name: CloudWatchLogGroupName
        - Name: S3KeyPrefix
        - Name: S3BucketName
    
    """
    
    S3EncryptionEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandlogconfiguration.html#cfn-ecs-cluster-executecommandlogconfiguration-s3encryptionenabled""", alias="S3EncryptionEnabled")
    CloudWatchEncryptionEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandlogconfiguration.html#cfn-ecs-cluster-executecommandlogconfiguration-cloudwatchencryptionenabled""", alias="CloudWatchEncryptionEnabled")
    CloudWatchLogGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandlogconfiguration.html#cfn-ecs-cluster-executecommandlogconfiguration-cloudwatchloggroupname""", alias="CloudWatchLogGroupName")
    S3KeyPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandlogconfiguration.html#cfn-ecs-cluster-executecommandlogconfiguration-s3keyprefix""", alias="S3KeyPrefix")
    S3BucketName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandlogconfiguration.html#cfn-ecs-cluster-executecommandlogconfiguration-s3bucketname""", alias="S3BucketName")
    


    @property
    def tropo_type(self) -> troposphere.ecs.ExecuteCommandLogConfiguration:
        from troposphere.ecs import ExecuteCommandLogConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ServiceConnectDefaults(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-serviceconnectdefaults.html
    Properties:
        - Name: Namespace
    
    """
    
    Namespace_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-serviceconnectdefaults.html#cfn-ecs-cluster-serviceconnectdefaults-namespace""", alias="Namespace")
    


    @property
    def tropo_type(self) -> troposphere.ecs.ServiceConnectDefaults:
        from troposphere.ecs import ServiceConnectDefaults as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CapacityProviderStrategy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-clustercapacityproviderassociations-capacityproviderstrategy.html
    Properties:
        - Name: CapacityProvider
        - Name: Base
        - Name: Weight
    
    """
    
    CapacityProvider_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-clustercapacityproviderassociations-capacityproviderstrategy.html#cfn-ecs-clustercapacityproviderassociations-capacityproviderstrategy-capacityprovider""", alias="CapacityProvider")
    Base_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-clustercapacityproviderassociations-capacityproviderstrategy.html#cfn-ecs-clustercapacityproviderassociations-capacityproviderstrategy-base""", alias="Base")
    Weight_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-clustercapacityproviderassociations-capacityproviderstrategy.html#cfn-ecs-clustercapacityproviderassociations-capacityproviderstrategy-weight""", alias="Weight")
    


    @property
    def tropo_type(self) -> troposphere.ecs.CapacityProviderStrategy:
        from troposphere.ecs import CapacityProviderStrategy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AwsVpcConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-awsvpcconfiguration.html
    Properties:
        - Name: SecurityGroups
        - Name: Subnets
        - Name: AssignPublicIp
    
    """
    
    SecurityGroups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-awsvpcconfiguration.html#cfn-ecs-service-awsvpcconfiguration-securitygroups""", alias="SecurityGroups")
    Subnets_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-awsvpcconfiguration.html#cfn-ecs-service-awsvpcconfiguration-subnets""", alias="Subnets")
    AssignPublicIp_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-awsvpcconfiguration.html#cfn-ecs-service-awsvpcconfiguration-assignpublicip""", alias="AssignPublicIp")
    


    @property
    def tropo_type(self) -> troposphere.ecs.AwsVpcConfiguration:
        from troposphere.ecs import AwsVpcConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CapacityProviderStrategyItem(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-capacityproviderstrategyitem.html
    Properties:
        - Name: CapacityProvider
        - Name: Base
        - Name: Weight
    
    """
    
    CapacityProvider_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-capacityproviderstrategyitem.html#cfn-ecs-service-capacityproviderstrategyitem-capacityprovider""", alias="CapacityProvider")
    Base_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-capacityproviderstrategyitem.html#cfn-ecs-service-capacityproviderstrategyitem-base""", alias="Base")
    Weight_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-capacityproviderstrategyitem.html#cfn-ecs-service-capacityproviderstrategyitem-weight""", alias="Weight")
    


    @property
    def tropo_type(self) -> troposphere.ecs.CapacityProviderStrategyItem:
        from troposphere.ecs import CapacityProviderStrategyItem as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeploymentAlarms(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentalarms.html
    Properties:
        - Name: AlarmNames
        - Name: Enable
        - Name: Rollback
    
    """
    
    AlarmNames_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentalarms.html#cfn-ecs-service-deploymentalarms-alarmnames""", alias="AlarmNames")
    Enable_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentalarms.html#cfn-ecs-service-deploymentalarms-enable""", alias="Enable")
    Rollback_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentalarms.html#cfn-ecs-service-deploymentalarms-rollback""", alias="Rollback")
    


    @property
    def tropo_type(self) -> troposphere.ecs.DeploymentAlarms:
        from troposphere.ecs import DeploymentAlarms as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeploymentCircuitBreaker(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentcircuitbreaker.html
    Properties:
        - Name: Enable
        - Name: Rollback
    
    """
    
    Enable_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentcircuitbreaker.html#cfn-ecs-service-deploymentcircuitbreaker-enable""", alias="Enable")
    Rollback_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentcircuitbreaker.html#cfn-ecs-service-deploymentcircuitbreaker-rollback""", alias="Rollback")
    


    @property
    def tropo_type(self) -> troposphere.ecs.DeploymentCircuitBreaker:
        from troposphere.ecs import DeploymentCircuitBreaker as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeploymentConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentconfiguration.html
    Properties:
        - Name: Alarms
        - Name: DeploymentCircuitBreaker
        - Name: MaximumPercent
        - Name: MinimumHealthyPercent
    
    """
    
    Alarms_: Optional['DeploymentAlarms'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentconfiguration.html#cfn-ecs-service-deploymentconfiguration-alarms""", alias="Alarms")
    DeploymentCircuitBreaker_: Optional['DeploymentCircuitBreaker'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentconfiguration.html#cfn-ecs-service-deploymentconfiguration-deploymentcircuitbreaker""", alias="DeploymentCircuitBreaker")
    MaximumPercent_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentconfiguration.html#cfn-ecs-service-deploymentconfiguration-maximumpercent""", alias="MaximumPercent")
    MinimumHealthyPercent_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentconfiguration.html#cfn-ecs-service-deploymentconfiguration-minimumhealthypercent""", alias="MinimumHealthyPercent")
    


    @property
    def tropo_type(self) -> troposphere.ecs.DeploymentConfiguration:
        from troposphere.ecs import DeploymentConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeploymentController(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentcontroller.html
    Properties:
        - Name: Type
    
    """
    
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentcontroller.html#cfn-ecs-service-deploymentcontroller-type""", alias="Type")
    


    @property
    def tropo_type(self) -> troposphere.ecs.DeploymentController:
        from troposphere.ecs import DeploymentController as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LoadBalancer(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-loadbalancer.html
    Properties:
        - Name: TargetGroupArn
        - Name: LoadBalancerName
        - Name: ContainerName
        - Name: ContainerPort
    
    """
    
    TargetGroupArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-loadbalancer.html#cfn-ecs-service-loadbalancer-targetgrouparn""", alias="TargetGroupArn")
    LoadBalancerName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-loadbalancer.html#cfn-ecs-service-loadbalancer-loadbalancername""", alias="LoadBalancerName")
    ContainerName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-loadbalancer.html#cfn-ecs-service-loadbalancer-containername""", alias="ContainerName")
    ContainerPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-loadbalancer.html#cfn-ecs-service-loadbalancer-containerport""", alias="ContainerPort")
    


    @property
    def tropo_type(self) -> troposphere.ecs.LoadBalancer:
        from troposphere.ecs import LoadBalancer as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LogConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-logconfiguration.html
    Properties:
        - Name: SecretOptions
        - Name: Options
        - Name: LogDriver
    
    """
    
    SecretOptions_: Optional[List['Secret']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-logconfiguration.html#cfn-ecs-service-logconfiguration-secretoptions""", alias="SecretOptions")
    Options_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-logconfiguration.html#cfn-ecs-service-logconfiguration-options""", alias="Options")
    LogDriver_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-logconfiguration.html#cfn-ecs-service-logconfiguration-logdriver""", alias="LogDriver")
    


    @property
    def tropo_type(self) -> troposphere.ecs.LogConfiguration:
        from troposphere.ecs import LogConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-networkconfiguration.html
    Properties:
        - Name: AwsvpcConfiguration
    
    """
    
    AwsvpcConfiguration_: Optional['AwsVpcConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-networkconfiguration.html#cfn-ecs-service-networkconfiguration-awsvpcconfiguration""", alias="AwsvpcConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.ecs.NetworkConfiguration:
        from troposphere.ecs import NetworkConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PlacementConstraint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-placementconstraint.html
    Properties:
        - Name: Type
        - Name: Expression
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-placementconstraint.html#cfn-ecs-service-placementconstraint-type""", alias="Type")
    Expression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-placementconstraint.html#cfn-ecs-service-placementconstraint-expression""", alias="Expression")
    


    @property
    def tropo_type(self) -> troposphere.ecs.PlacementConstraint:
        from troposphere.ecs import PlacementConstraint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PlacementStrategy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-placementstrategy.html
    Properties:
        - Name: Field
        - Name: Type
    
    """
    
    Field_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-placementstrategy.html#cfn-ecs-service-placementstrategy-field""", alias="Field")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-placementstrategy.html#cfn-ecs-service-placementstrategy-type""", alias="Type")
    


    @property
    def tropo_type(self) -> troposphere.ecs.PlacementStrategy:
        from troposphere.ecs import PlacementStrategy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Secret(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-secret.html
    Properties:
        - Name: ValueFrom
        - Name: Name
    
    """
    
    ValueFrom_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-secret.html#cfn-ecs-service-secret-valuefrom""", alias="ValueFrom")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-secret.html#cfn-ecs-service-secret-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.ecs.Secret:
        from troposphere.ecs import Secret as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ServiceConnectClientAlias(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceconnectclientalias.html
    Properties:
        - Name: DnsName
        - Name: Port
    
    """
    
    DnsName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceconnectclientalias.html#cfn-ecs-service-serviceconnectclientalias-dnsname""", alias="DnsName")
    Port_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceconnectclientalias.html#cfn-ecs-service-serviceconnectclientalias-port""", alias="Port")
    


    @property
    def tropo_type(self) -> troposphere.ecs.ServiceConnectClientAlias:
        from troposphere.ecs import ServiceConnectClientAlias as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ServiceConnectConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceconnectconfiguration.html
    Properties:
        - Name: Services
        - Name: Enabled
        - Name: LogConfiguration
        - Name: Namespace
    
    """
    
    Services_: Optional[List['ServiceConnectService']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceconnectconfiguration.html#cfn-ecs-service-serviceconnectconfiguration-services""", alias="Services")
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceconnectconfiguration.html#cfn-ecs-service-serviceconnectconfiguration-enabled""", alias="Enabled")
    LogConfiguration_: Optional['LogConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceconnectconfiguration.html#cfn-ecs-service-serviceconnectconfiguration-logconfiguration""", alias="LogConfiguration")
    Namespace_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceconnectconfiguration.html#cfn-ecs-service-serviceconnectconfiguration-namespace""", alias="Namespace")
    


    @property
    def tropo_type(self) -> troposphere.ecs.ServiceConnectConfiguration:
        from troposphere.ecs import ServiceConnectConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ServiceConnectService(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceconnectservice.html
    Properties:
        - Name: IngressPortOverride
        - Name: ClientAliases
        - Name: DiscoveryName
        - Name: PortName
    
    """
    
    IngressPortOverride_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceconnectservice.html#cfn-ecs-service-serviceconnectservice-ingressportoverride""", alias="IngressPortOverride")
    ClientAliases_: Optional[List['ServiceConnectClientAlias']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceconnectservice.html#cfn-ecs-service-serviceconnectservice-clientaliases""", alias="ClientAliases")
    DiscoveryName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceconnectservice.html#cfn-ecs-service-serviceconnectservice-discoveryname""", alias="DiscoveryName")
    PortName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceconnectservice.html#cfn-ecs-service-serviceconnectservice-portname""", alias="PortName")
    


    @property
    def tropo_type(self) -> troposphere.ecs.ServiceConnectService:
        from troposphere.ecs import ServiceConnectService as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ServiceRegistry(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceregistry.html
    Properties:
        - Name: ContainerName
        - Name: Port
        - Name: ContainerPort
        - Name: RegistryArn
    
    """
    
    ContainerName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceregistry.html#cfn-ecs-service-serviceregistry-containername""", alias="ContainerName")
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceregistry.html#cfn-ecs-service-serviceregistry-port""", alias="Port")
    ContainerPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceregistry.html#cfn-ecs-service-serviceregistry-containerport""", alias="ContainerPort")
    RegistryArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceregistry.html#cfn-ecs-service-serviceregistry-registryarn""", alias="RegistryArn")
    


    @property
    def tropo_type(self) -> troposphere.ecs.ServiceRegistry:
        from troposphere.ecs import ServiceRegistry as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AuthorizationConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-authorizationconfig.html
    Properties:
        - Name: IAM
        - Name: AccessPointId
    
    """
    
    IAM_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-authorizationconfig.html#cfn-ecs-taskdefinition-authorizationconfig-iam""", alias="IAM")
    AccessPointId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-authorizationconfig.html#cfn-ecs-taskdefinition-authorizationconfig-accesspointid""", alias="AccessPointId")
    


    @property
    def tropo_type(self) -> troposphere.ecs.AuthorizationConfig:
        from troposphere.ecs import AuthorizationConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ContainerDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html
    Properties:
        - Name: User
        - Name: Secrets
        - Name: Memory
        - Name: Privileged
        - Name: HealthCheck
        - Name: StartTimeout
        - Name: VolumesFrom
        - Name: Cpu
        - Name: EntryPoint
        - Name: DnsServers
        - Name: ReadonlyRootFilesystem
        - Name: Image
        - Name: Essential
        - Name: LogConfiguration
        - Name: ResourceRequirements
        - Name: EnvironmentFiles
        - Name: Name
        - Name: FirelensConfiguration
        - Name: DockerSecurityOptions
        - Name: SystemControls
        - Name: Interactive
        - Name: DnsSearchDomains
        - Name: Ulimits
        - Name: StopTimeout
        - Name: WorkingDirectory
        - Name: MemoryReservation
        - Name: RepositoryCredentials
        - Name: ExtraHosts
        - Name: Hostname
        - Name: LinuxParameters
        - Name: DisableNetworking
        - Name: PseudoTerminal
        - Name: MountPoints
        - Name: DependsOn
        - Name: DockerLabels
        - Name: PortMappings
        - Name: Command
        - Name: Environment
        - Name: Links
    
    """
    
    User_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-user""", alias="User")
    Secrets_: Optional[List['Secret']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-secrets""", alias="Secrets")
    Memory_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-memory""", alias="Memory")
    Privileged_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-privileged""", alias="Privileged")
    HealthCheck_: Optional['HealthCheck'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-healthcheck""", alias="HealthCheck")
    StartTimeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-starttimeout""", alias="StartTimeout")
    VolumesFrom_: Optional[List['VolumeFrom']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-volumesfrom""", alias="VolumesFrom")
    Cpu_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-cpu""", alias="Cpu")
    EntryPoint_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-entrypoint""", alias="EntryPoint")
    DnsServers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-dnsservers""", alias="DnsServers")
    ReadonlyRootFilesystem_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-readonlyrootfilesystem""", alias="ReadonlyRootFilesystem")
    Image_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-image""", alias="Image")
    Essential_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-essential""", alias="Essential")
    LogConfiguration_: Optional['LogConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-logconfiguration""", alias="LogConfiguration")
    ResourceRequirements_: Optional[List['ResourceRequirement']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-resourcerequirements""", alias="ResourceRequirements")
    EnvironmentFiles_: Optional[List['EnvironmentFile']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-environmentfiles""", alias="EnvironmentFiles")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-name""", alias="Name")
    FirelensConfiguration_: Optional['FirelensConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-firelensconfiguration""", alias="FirelensConfiguration")
    DockerSecurityOptions_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-dockersecurityoptions""", alias="DockerSecurityOptions")
    SystemControls_: Optional[List['SystemControl']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-systemcontrols""", alias="SystemControls")
    Interactive_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-interactive""", alias="Interactive")
    DnsSearchDomains_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-dnssearchdomains""", alias="DnsSearchDomains")
    Ulimits_: Optional[List['Ulimit']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-ulimits""", alias="Ulimits")
    StopTimeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-stoptimeout""", alias="StopTimeout")
    WorkingDirectory_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-workingdirectory""", alias="WorkingDirectory")
    MemoryReservation_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-memoryreservation""", alias="MemoryReservation")
    RepositoryCredentials_: Optional['RepositoryCredentials'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-repositorycredentials""", alias="RepositoryCredentials")
    ExtraHosts_: Optional[List['HostEntry']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-extrahosts""", alias="ExtraHosts")
    Hostname_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-hostname""", alias="Hostname")
    LinuxParameters_: Optional['LinuxParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-linuxparameters""", alias="LinuxParameters")
    DisableNetworking_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-disablenetworking""", alias="DisableNetworking")
    PseudoTerminal_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-pseudoterminal""", alias="PseudoTerminal")
    MountPoints_: Optional[List['MountPoint']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-mountpoints""", alias="MountPoints")
    DependsOn_: Optional[List['ContainerDependency']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-dependson""", alias="DependsOn")
    DockerLabels_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-dockerlabels""", alias="DockerLabels")
    PortMappings_: Optional[List['PortMapping']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-portmappings""", alias="PortMappings")
    Command_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-command""", alias="Command")
    Environment_: Optional[List['KeyValuePair']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-environment""", alias="Environment")
    Links_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html#cfn-ecs-taskdefinition-containerdefinition-links""", alias="Links")
    


    @property
    def tropo_type(self) -> troposphere.ecs.ContainerDefinition:
        from troposphere.ecs import ContainerDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ContainerDependency(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdependency.html
    Properties:
        - Name: Condition
        - Name: ContainerName
    
    """
    
    Condition_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdependency.html#cfn-ecs-taskdefinition-containerdependency-condition""", alias="Condition")
    ContainerName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdependency.html#cfn-ecs-taskdefinition-containerdependency-containername""", alias="ContainerName")
    


    @property
    def tropo_type(self) -> troposphere.ecs.ContainerDependency:
        from troposphere.ecs import ContainerDependency as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Device(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-device.html
    Properties:
        - Name: HostPath
        - Name: Permissions
        - Name: ContainerPath
    
    """
    
    HostPath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-device.html#cfn-ecs-taskdefinition-device-hostpath""", alias="HostPath")
    Permissions_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-device.html#cfn-ecs-taskdefinition-device-permissions""", alias="Permissions")
    ContainerPath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-device.html#cfn-ecs-taskdefinition-device-containerpath""", alias="ContainerPath")
    


    @property
    def tropo_type(self) -> troposphere.ecs.Device:
        from troposphere.ecs import Device as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DockerVolumeConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-dockervolumeconfiguration.html
    Properties:
        - Name: DriverOpts
        - Name: Scope
        - Name: Autoprovision
        - Name: Driver
        - Name: Labels
    
    """
    
    DriverOpts_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-dockervolumeconfiguration.html#cfn-ecs-taskdefinition-dockervolumeconfiguration-driveropts""", alias="DriverOpts")
    Scope_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-dockervolumeconfiguration.html#cfn-ecs-taskdefinition-dockervolumeconfiguration-scope""", alias="Scope")
    Autoprovision_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-dockervolumeconfiguration.html#cfn-ecs-taskdefinition-dockervolumeconfiguration-autoprovision""", alias="Autoprovision")
    Driver_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-dockervolumeconfiguration.html#cfn-ecs-taskdefinition-dockervolumeconfiguration-driver""", alias="Driver")
    Labels_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-dockervolumeconfiguration.html#cfn-ecs-taskdefinition-dockervolumeconfiguration-labels""", alias="Labels")
    


    @property
    def tropo_type(self) -> troposphere.ecs.DockerVolumeConfiguration:
        from troposphere.ecs import DockerVolumeConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EFSVolumeConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-efsvolumeconfiguration.html
    Properties:
        - Name: FilesystemId
        - Name: TransitEncryption
        - Name: AuthorizationConfig
        - Name: RootDirectory
        - Name: TransitEncryptionPort
    
    """
    
    FilesystemId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-efsvolumeconfiguration.html#cfn-ecs-taskdefinition-efsvolumeconfiguration-filesystemid""", alias="FilesystemId")
    TransitEncryption_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-efsvolumeconfiguration.html#cfn-ecs-taskdefinition-efsvolumeconfiguration-transitencryption""", alias="TransitEncryption")
    AuthorizationConfig_: Optional['AuthorizationConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-efsvolumeconfiguration.html#cfn-ecs-taskdefinition-efsvolumeconfiguration-authorizationconfig""", alias="AuthorizationConfig")
    RootDirectory_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-efsvolumeconfiguration.html#cfn-ecs-taskdefinition-efsvolumeconfiguration-rootdirectory""", alias="RootDirectory")
    TransitEncryptionPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-efsvolumeconfiguration.html#cfn-ecs-taskdefinition-efsvolumeconfiguration-transitencryptionport""", alias="TransitEncryptionPort")
    


    @property
    def tropo_type(self) -> troposphere.ecs.EFSVolumeConfiguration:
        from troposphere.ecs import EFSVolumeConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EnvironmentFile(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-environmentfile.html
    Properties:
        - Name: Type
        - Name: Value
    
    """
    
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-environmentfile.html#cfn-ecs-taskdefinition-environmentfile-type""", alias="Type")
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-environmentfile.html#cfn-ecs-taskdefinition-environmentfile-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.ecs.EnvironmentFile:
        from troposphere.ecs import EnvironmentFile as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EphemeralStorage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-ephemeralstorage.html
    Properties:
        - Name: SizeInGiB
    
    """
    
    SizeInGiB_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-ephemeralstorage.html#cfn-ecs-taskdefinition-ephemeralstorage-sizeingib""", alias="SizeInGiB")
    


    @property
    def tropo_type(self) -> troposphere.ecs.EphemeralStorage:
        from troposphere.ecs import EphemeralStorage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FirelensConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-firelensconfiguration.html
    Properties:
        - Name: Options
        - Name: Type
    
    """
    
    Options_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-firelensconfiguration.html#cfn-ecs-taskdefinition-firelensconfiguration-options""", alias="Options")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-firelensconfiguration.html#cfn-ecs-taskdefinition-firelensconfiguration-type""", alias="Type")
    


    @property
    def tropo_type(self) -> troposphere.ecs.FirelensConfiguration:
        from troposphere.ecs import FirelensConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HealthCheck(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-healthcheck.html
    Properties:
        - Name: Command
        - Name: Timeout
        - Name: Retries
        - Name: Interval
        - Name: StartPeriod
    
    """
    
    Command_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-healthcheck.html#cfn-ecs-taskdefinition-healthcheck-command""", alias="Command")
    Timeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-healthcheck.html#cfn-ecs-taskdefinition-healthcheck-timeout""", alias="Timeout")
    Retries_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-healthcheck.html#cfn-ecs-taskdefinition-healthcheck-retries""", alias="Retries")
    Interval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-healthcheck.html#cfn-ecs-taskdefinition-healthcheck-interval""", alias="Interval")
    StartPeriod_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-healthcheck.html#cfn-ecs-taskdefinition-healthcheck-startperiod""", alias="StartPeriod")
    


    @property
    def tropo_type(self) -> troposphere.ecs.HealthCheck:
        from troposphere.ecs import HealthCheck as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HostEntry(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-hostentry.html
    Properties:
        - Name: Hostname
        - Name: IpAddress
    
    """
    
    Hostname_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-hostentry.html#cfn-ecs-taskdefinition-hostentry-hostname""", alias="Hostname")
    IpAddress_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-hostentry.html#cfn-ecs-taskdefinition-hostentry-ipaddress""", alias="IpAddress")
    


    @property
    def tropo_type(self) -> troposphere.ecs.HostEntry:
        from troposphere.ecs import HostEntry as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HostVolumeProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-hostvolumeproperties.html
    Properties:
        - Name: SourcePath
    
    """
    
    SourcePath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-hostvolumeproperties.html#cfn-ecs-taskdefinition-hostvolumeproperties-sourcepath""", alias="SourcePath")
    


    @property
    def tropo_type(self) -> troposphere.ecs.HostVolumeProperties:
        from troposphere.ecs import HostVolumeProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InferenceAccelerator(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-inferenceaccelerator.html
    Properties:
        - Name: DeviceType
        - Name: DeviceName
    
    """
    
    DeviceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-inferenceaccelerator.html#cfn-ecs-taskdefinition-inferenceaccelerator-devicetype""", alias="DeviceType")
    DeviceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-inferenceaccelerator.html#cfn-ecs-taskdefinition-inferenceaccelerator-devicename""", alias="DeviceName")
    


    @property
    def tropo_type(self) -> troposphere.ecs.InferenceAccelerator:
        from troposphere.ecs import InferenceAccelerator as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KernelCapabilities(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-kernelcapabilities.html
    Properties:
        - Name: Add
        - Name: Drop
    
    """
    
    Add_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-kernelcapabilities.html#cfn-ecs-taskdefinition-kernelcapabilities-add""", alias="Add")
    Drop_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-kernelcapabilities.html#cfn-ecs-taskdefinition-kernelcapabilities-drop""", alias="Drop")
    


    @property
    def tropo_type(self) -> troposphere.ecs.KernelCapabilities:
        from troposphere.ecs import KernelCapabilities as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KeyValuePair(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-keyvaluepair.html
    Properties:
        - Name: Value
        - Name: Name
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-keyvaluepair.html#cfn-ecs-taskdefinition-keyvaluepair-value""", alias="Value")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-keyvaluepair.html#cfn-ecs-taskdefinition-keyvaluepair-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.ecs.KeyValuePair:
        from troposphere.ecs import KeyValuePair as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LinuxParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-linuxparameters.html
    Properties:
        - Name: Capabilities
        - Name: Swappiness
        - Name: Tmpfs
        - Name: SharedMemorySize
        - Name: Devices
        - Name: InitProcessEnabled
        - Name: MaxSwap
    
    """
    
    Capabilities_: Optional['KernelCapabilities'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-linuxparameters.html#cfn-ecs-taskdefinition-linuxparameters-capabilities""", alias="Capabilities")
    Swappiness_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-linuxparameters.html#cfn-ecs-taskdefinition-linuxparameters-swappiness""", alias="Swappiness")
    Tmpfs_: Optional[List['Tmpfs']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-linuxparameters.html#cfn-ecs-taskdefinition-linuxparameters-tmpfs""", alias="Tmpfs")
    SharedMemorySize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-linuxparameters.html#cfn-ecs-taskdefinition-linuxparameters-sharedmemorysize""", alias="SharedMemorySize")
    Devices_: Optional[List['Device']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-linuxparameters.html#cfn-ecs-taskdefinition-linuxparameters-devices""", alias="Devices")
    InitProcessEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-linuxparameters.html#cfn-ecs-taskdefinition-linuxparameters-initprocessenabled""", alias="InitProcessEnabled")
    MaxSwap_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-linuxparameters.html#cfn-ecs-taskdefinition-linuxparameters-maxswap""", alias="MaxSwap")
    


    @property
    def tropo_type(self) -> troposphere.ecs.LinuxParameters:
        from troposphere.ecs import LinuxParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LogConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-logconfiguration.html
    Properties:
        - Name: SecretOptions
        - Name: Options
        - Name: LogDriver
    
    """
    
    SecretOptions_: Optional[List['Secret']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-logconfiguration.html#cfn-ecs-taskdefinition-logconfiguration-secretoptions""", alias="SecretOptions")
    Options_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-logconfiguration.html#cfn-ecs-taskdefinition-logconfiguration-options""", alias="Options")
    LogDriver_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-logconfiguration.html#cfn-ecs-taskdefinition-logconfiguration-logdriver""", alias="LogDriver")
    


    @property
    def tropo_type(self) -> troposphere.ecs.LogConfiguration:
        from troposphere.ecs import LogConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MountPoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-mountpoint.html
    Properties:
        - Name: ReadOnly
        - Name: SourceVolume
        - Name: ContainerPath
    
    """
    
    ReadOnly_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-mountpoint.html#cfn-ecs-taskdefinition-mountpoint-readonly""", alias="ReadOnly")
    SourceVolume_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-mountpoint.html#cfn-ecs-taskdefinition-mountpoint-sourcevolume""", alias="SourceVolume")
    ContainerPath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-mountpoint.html#cfn-ecs-taskdefinition-mountpoint-containerpath""", alias="ContainerPath")
    


    @property
    def tropo_type(self) -> troposphere.ecs.MountPoint:
        from troposphere.ecs import MountPoint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PortMapping(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-portmapping.html
    Properties:
        - Name: AppProtocol
        - Name: ContainerPortRange
        - Name: HostPort
        - Name: ContainerPort
        - Name: Protocol
        - Name: Name
    
    """
    
    AppProtocol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-portmapping.html#cfn-ecs-taskdefinition-portmapping-appprotocol""", alias="AppProtocol")
    ContainerPortRange_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-portmapping.html#cfn-ecs-taskdefinition-portmapping-containerportrange""", alias="ContainerPortRange")
    HostPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-portmapping.html#cfn-ecs-taskdefinition-portmapping-hostport""", alias="HostPort")
    ContainerPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-portmapping.html#cfn-ecs-taskdefinition-portmapping-containerport""", alias="ContainerPort")
    Protocol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-portmapping.html#cfn-ecs-taskdefinition-portmapping-protocol""", alias="Protocol")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-portmapping.html#cfn-ecs-taskdefinition-portmapping-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.ecs.PortMapping:
        from troposphere.ecs import PortMapping as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProxyConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-proxyconfiguration.html
    Properties:
        - Name: ProxyConfigurationProperties
        - Name: Type
        - Name: ContainerName
    
    """
    
    ProxyConfigurationProperties_: Optional[List['KeyValuePair']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-proxyconfiguration.html#cfn-ecs-taskdefinition-proxyconfiguration-proxyconfigurationproperties""", alias="ProxyConfigurationProperties")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-proxyconfiguration.html#cfn-ecs-taskdefinition-proxyconfiguration-type""", alias="Type")
    ContainerName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-proxyconfiguration.html#cfn-ecs-taskdefinition-proxyconfiguration-containername""", alias="ContainerName")
    


    @property
    def tropo_type(self) -> troposphere.ecs.ProxyConfiguration:
        from troposphere.ecs import ProxyConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RepositoryCredentials(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-repositorycredentials.html
    Properties:
        - Name: CredentialsParameter
    
    """
    
    CredentialsParameter_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-repositorycredentials.html#cfn-ecs-taskdefinition-repositorycredentials-credentialsparameter""", alias="CredentialsParameter")
    


    @property
    def tropo_type(self) -> troposphere.ecs.RepositoryCredentials:
        from troposphere.ecs import RepositoryCredentials as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResourceRequirement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-resourcerequirement.html
    Properties:
        - Name: Type
        - Name: Value
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-resourcerequirement.html#cfn-ecs-taskdefinition-resourcerequirement-type""", alias="Type")
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-resourcerequirement.html#cfn-ecs-taskdefinition-resourcerequirement-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.ecs.ResourceRequirement:
        from troposphere.ecs import ResourceRequirement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RuntimePlatform(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-runtimeplatform.html
    Properties:
        - Name: OperatingSystemFamily
        - Name: CpuArchitecture
    
    """
    
    OperatingSystemFamily_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-runtimeplatform.html#cfn-ecs-taskdefinition-runtimeplatform-operatingsystemfamily""", alias="OperatingSystemFamily")
    CpuArchitecture_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-runtimeplatform.html#cfn-ecs-taskdefinition-runtimeplatform-cpuarchitecture""", alias="CpuArchitecture")
    


    @property
    def tropo_type(self) -> troposphere.ecs.RuntimePlatform:
        from troposphere.ecs import RuntimePlatform as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Secret(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-secret.html
    Properties:
        - Name: ValueFrom
        - Name: Name
    
    """
    
    ValueFrom_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-secret.html#cfn-ecs-taskdefinition-secret-valuefrom""", alias="ValueFrom")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-secret.html#cfn-ecs-taskdefinition-secret-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.ecs.Secret:
        from troposphere.ecs import Secret as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SystemControl(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-systemcontrol.html
    Properties:
        - Name: Value
        - Name: Namespace
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-systemcontrol.html#cfn-ecs-taskdefinition-systemcontrol-value""", alias="Value")
    Namespace_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-systemcontrol.html#cfn-ecs-taskdefinition-systemcontrol-namespace""", alias="Namespace")
    


    @property
    def tropo_type(self) -> troposphere.ecs.SystemControl:
        from troposphere.ecs import SystemControl as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TaskDefinitionPlacementConstraint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-taskdefinitionplacementconstraint.html
    Properties:
        - Name: Type
        - Name: Expression
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-taskdefinitionplacementconstraint.html#cfn-ecs-taskdefinition-taskdefinitionplacementconstraint-type""", alias="Type")
    Expression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-taskdefinitionplacementconstraint.html#cfn-ecs-taskdefinition-taskdefinitionplacementconstraint-expression""", alias="Expression")
    


    @property
    def tropo_type(self) -> troposphere.ecs.TaskDefinitionPlacementConstraint:
        from troposphere.ecs import TaskDefinitionPlacementConstraint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Tmpfs(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-tmpfs.html
    Properties:
        - Name: Size
        - Name: ContainerPath
        - Name: MountOptions
    
    """
    
    Size_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-tmpfs.html#cfn-ecs-taskdefinition-tmpfs-size""", alias="Size")
    ContainerPath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-tmpfs.html#cfn-ecs-taskdefinition-tmpfs-containerpath""", alias="ContainerPath")
    MountOptions_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-tmpfs.html#cfn-ecs-taskdefinition-tmpfs-mountoptions""", alias="MountOptions")
    


    @property
    def tropo_type(self) -> troposphere.ecs.Tmpfs:
        from troposphere.ecs import Tmpfs as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Ulimit(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-ulimit.html
    Properties:
        - Name: SoftLimit
        - Name: HardLimit
        - Name: Name
    
    """
    
    SoftLimit_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-ulimit.html#cfn-ecs-taskdefinition-ulimit-softlimit""", alias="SoftLimit")
    HardLimit_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-ulimit.html#cfn-ecs-taskdefinition-ulimit-hardlimit""", alias="HardLimit")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-ulimit.html#cfn-ecs-taskdefinition-ulimit-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.ecs.Ulimit:
        from troposphere.ecs import Ulimit as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Volume(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-volume.html
    Properties:
        - Name: EFSVolumeConfiguration
        - Name: Host
        - Name: DockerVolumeConfiguration
        - Name: Name
    
    """
    
    EFSVolumeConfiguration_: Optional['EFSVolumeConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-volume.html#cfn-ecs-taskdefinition-volume-efsvolumeconfiguration""", alias="EFSVolumeConfiguration")
    Host_: Optional['HostVolumeProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-volume.html#cfn-ecs-taskdefinition-volume-host""", alias="Host")
    DockerVolumeConfiguration_: Optional['DockerVolumeConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-volume.html#cfn-ecs-taskdefinition-volume-dockervolumeconfiguration""", alias="DockerVolumeConfiguration")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-volume.html#cfn-ecs-taskdefinition-volume-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.ecs.Volume:
        from troposphere.ecs import Volume as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VolumeFrom(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-volumefrom.html
    Properties:
        - Name: ReadOnly
        - Name: SourceContainer
    
    """
    
    ReadOnly_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-volumefrom.html#cfn-ecs-taskdefinition-volumefrom-readonly""", alias="ReadOnly")
    SourceContainer_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-volumefrom.html#cfn-ecs-taskdefinition-volumefrom-sourcecontainer""", alias="SourceContainer")
    


    @property
    def tropo_type(self) -> troposphere.ecs.VolumeFrom:
        from troposphere.ecs import VolumeFrom as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AwsVpcConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-awsvpcconfiguration.html
    Properties:
        - Name: SecurityGroups
        - Name: Subnets
        - Name: AssignPublicIp
    
    """
    
    SecurityGroups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-awsvpcconfiguration.html#cfn-ecs-taskset-awsvpcconfiguration-securitygroups""", alias="SecurityGroups")
    Subnets_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-awsvpcconfiguration.html#cfn-ecs-taskset-awsvpcconfiguration-subnets""", alias="Subnets")
    AssignPublicIp_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-awsvpcconfiguration.html#cfn-ecs-taskset-awsvpcconfiguration-assignpublicip""", alias="AssignPublicIp")
    


    @property
    def tropo_type(self) -> troposphere.ecs.AwsVpcConfiguration:
        from troposphere.ecs import AwsVpcConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LoadBalancer(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-loadbalancer.html
    Properties:
        - Name: TargetGroupArn
        - Name: ContainerName
        - Name: ContainerPort
    
    """
    
    TargetGroupArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-loadbalancer.html#cfn-ecs-taskset-loadbalancer-targetgrouparn""", alias="TargetGroupArn")
    ContainerName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-loadbalancer.html#cfn-ecs-taskset-loadbalancer-containername""", alias="ContainerName")
    ContainerPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-loadbalancer.html#cfn-ecs-taskset-loadbalancer-containerport""", alias="ContainerPort")
    


    @property
    def tropo_type(self) -> troposphere.ecs.LoadBalancer:
        from troposphere.ecs import LoadBalancer as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-networkconfiguration.html
    Properties:
        - Name: AwsVpcConfiguration
    
    """
    
    AwsVpcConfiguration_: Optional['AwsVpcConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-networkconfiguration.html#cfn-ecs-taskset-networkconfiguration-awsvpcconfiguration""", alias="AwsVpcConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.ecs.NetworkConfiguration:
        from troposphere.ecs import NetworkConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Scale(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-scale.html
    Properties:
        - Name: Value
        - Name: Unit
    
    """
    
    Value_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-scale.html#cfn-ecs-taskset-scale-value""", alias="Value")
    Unit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-scale.html#cfn-ecs-taskset-scale-unit""", alias="Unit")
    


    @property
    def tropo_type(self) -> troposphere.ecs.Scale:
        from troposphere.ecs import Scale as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ServiceRegistry(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-serviceregistry.html
    Properties:
        - Name: ContainerName
        - Name: Port
        - Name: ContainerPort
        - Name: RegistryArn
    
    """
    
    ContainerName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-serviceregistry.html#cfn-ecs-taskset-serviceregistry-containername""", alias="ContainerName")
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-serviceregistry.html#cfn-ecs-taskset-serviceregistry-port""", alias="Port")
    ContainerPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-serviceregistry.html#cfn-ecs-taskset-serviceregistry-containerport""", alias="ContainerPort")
    RegistryArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-serviceregistry.html#cfn-ecs-taskset-serviceregistry-registryarn""", alias="RegistryArn")
    


    @property
    def tropo_type(self) -> troposphere.ecs.ServiceRegistry:
        from troposphere.ecs import ServiceRegistry as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class CapacityProvider(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-capacityprovider.html
    Properties:
        - Name: AutoScalingGroupProvider
        - Name: Tags
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AutoScalingGroupProvider_: 'AutoScalingGroupProvider' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-capacityprovider.html#cfn-ecs-capacityprovider-autoscalinggroupprovider""", alias="AutoScalingGroupProvider")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-capacityprovider.html#cfn-ecs-capacityprovider-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-capacityprovider.html#cfn-ecs-capacityprovider-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.ecs.CapacityProvider:
        from troposphere.ecs import CapacityProvider as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ecs import CapacityProvider as TropoT
        return resource_to_troposphere(self, TropoT)


class Cluster(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.html
    Properties:
        - Name: ClusterSettings
        - Name: DefaultCapacityProviderStrategy
        - Name: Configuration
        - Name: ServiceConnectDefaults
        - Name: CapacityProviders
        - Name: ClusterName
        - Name: Tags
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ClusterSettings_: Optional[List['ClusterSettings']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.html#cfn-ecs-cluster-clustersettings""", alias="ClusterSettings")
    DefaultCapacityProviderStrategy_: Optional[List['CapacityProviderStrategyItem']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.html#cfn-ecs-cluster-defaultcapacityproviderstrategy""", alias="DefaultCapacityProviderStrategy")
    Configuration_: Optional['ClusterConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.html#cfn-ecs-cluster-configuration""", alias="Configuration")
    ServiceConnectDefaults_: Optional['ServiceConnectDefaults'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.html#cfn-ecs-cluster-serviceconnectdefaults""", alias="ServiceConnectDefaults")
    CapacityProviders_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.html#cfn-ecs-cluster-capacityproviders""", alias="CapacityProviders")
    ClusterName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.html#cfn-ecs-cluster-clustername""", alias="ClusterName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.html#cfn-ecs-cluster-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ecs.Cluster:
        from troposphere.ecs import Cluster as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ecs import Cluster as TropoT
        return resource_to_troposphere(self, TropoT)


class ClusterCapacityProviderAssociations(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-clustercapacityproviderassociations.html
    Properties:
        - Name: DefaultCapacityProviderStrategy
        - Name: CapacityProviders
        - Name: Cluster
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DefaultCapacityProviderStrategy_: List['CapacityProviderStrategy'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-clustercapacityproviderassociations.html#cfn-ecs-clustercapacityproviderassociations-defaultcapacityproviderstrategy""", alias="DefaultCapacityProviderStrategy")
    CapacityProviders_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-clustercapacityproviderassociations.html#cfn-ecs-clustercapacityproviderassociations-capacityproviders""", alias="CapacityProviders")
    Cluster_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-clustercapacityproviderassociations.html#cfn-ecs-clustercapacityproviderassociations-cluster""", alias="Cluster")
    

    @property
    def tropo_type(self) -> troposphere.ecs.ClusterCapacityProviderAssociations:
        from troposphere.ecs import ClusterCapacityProviderAssociations as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ecs import ClusterCapacityProviderAssociations as TropoT
        return resource_to_troposphere(self, TropoT)


class PrimaryTaskSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-primarytaskset.html
    Properties:
        - Name: TaskSetId
        - Name: Cluster
        - Name: Service
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TaskSetId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-primarytaskset.html#cfn-ecs-primarytaskset-tasksetid""", alias="TaskSetId")
    Cluster_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-primarytaskset.html#cfn-ecs-primarytaskset-cluster""", alias="Cluster")
    Service_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-primarytaskset.html#cfn-ecs-primarytaskset-service""", alias="Service")
    

    @property
    def tropo_type(self) -> troposphere.ecs.PrimaryTaskSet:
        from troposphere.ecs import PrimaryTaskSet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ecs import PrimaryTaskSet as TropoT
        return resource_to_troposphere(self, TropoT)


class Service(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html
    Properties:
        - Name: PlatformVersion
        - Name: HealthCheckGracePeriodSeconds
        - Name: EnableECSManagedTags
        - Name: EnableExecuteCommand
        - Name: PlacementConstraints
        - Name: PropagateTags
        - Name: Cluster
        - Name: LoadBalancers
        - Name: ServiceConnectConfiguration
        - Name: DesiredCount
        - Name: PlacementStrategies
        - Name: DeploymentController
        - Name: ServiceRegistries
        - Name: CapacityProviderStrategy
        - Name: LaunchType
        - Name: Role
        - Name: SchedulingStrategy
        - Name: TaskDefinition
        - Name: ServiceName
        - Name: NetworkConfiguration
        - Name: DeploymentConfiguration
        - Name: Tags
    Attributes:
        - Name: ServiceArn
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PlatformVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-platformversion""", alias="PlatformVersion")
    HealthCheckGracePeriodSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-healthcheckgraceperiodseconds""", alias="HealthCheckGracePeriodSeconds")
    EnableECSManagedTags_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-enableecsmanagedtags""", alias="EnableECSManagedTags")
    EnableExecuteCommand_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-enableexecutecommand""", alias="EnableExecuteCommand")
    PlacementConstraints_: Optional[List['PlacementConstraint']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-placementconstraints""", alias="PlacementConstraints")
    PropagateTags_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-propagatetags""", alias="PropagateTags")
    Cluster_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-cluster""", alias="Cluster")
    LoadBalancers_: Optional[List['LoadBalancer']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-loadbalancers""", alias="LoadBalancers")
    ServiceConnectConfiguration_: Optional['ServiceConnectConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-serviceconnectconfiguration""", alias="ServiceConnectConfiguration")
    DesiredCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-desiredcount""", alias="DesiredCount")
    PlacementStrategies_: Optional[List['PlacementStrategy']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-placementstrategies""", alias="PlacementStrategies")
    DeploymentController_: Optional['DeploymentController'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-deploymentcontroller""", alias="DeploymentController")
    ServiceRegistries_: Optional[List['ServiceRegistry']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-serviceregistries""", alias="ServiceRegistries")
    CapacityProviderStrategy_: Optional[List['CapacityProviderStrategyItem']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-capacityproviderstrategy""", alias="CapacityProviderStrategy")
    LaunchType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-launchtype""", alias="LaunchType")
    Role_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-role""", alias="Role")
    SchedulingStrategy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-schedulingstrategy""", alias="SchedulingStrategy")
    TaskDefinition_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-taskdefinition""", alias="TaskDefinition")
    ServiceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-servicename""", alias="ServiceName")
    NetworkConfiguration_: Optional['NetworkConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-networkconfiguration""", alias="NetworkConfiguration")
    DeploymentConfiguration_: Optional['DeploymentConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-deploymentconfiguration""", alias="DeploymentConfiguration")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ecs.Service:
        from troposphere.ecs import Service as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ecs import Service as TropoT
        return resource_to_troposphere(self, TropoT)


class TaskDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html
    Properties:
        - Name: TaskRoleArn
        - Name: IpcMode
        - Name: InferenceAccelerators
        - Name: Memory
        - Name: PlacementConstraints
        - Name: Cpu
        - Name: RequiresCompatibilities
        - Name: NetworkMode
        - Name: PidMode
        - Name: ExecutionRoleArn
        - Name: RuntimePlatform
        - Name: ProxyConfiguration
        - Name: Volumes
        - Name: ContainerDefinitions
        - Name: Family
        - Name: EphemeralStorage
        - Name: Tags
    Attributes:
        - Name: TaskDefinitionArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TaskRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-taskrolearn""", alias="TaskRoleArn")
    IpcMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-ipcmode""", alias="IpcMode")
    InferenceAccelerators_: Optional[List['InferenceAccelerator']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-inferenceaccelerators""", alias="InferenceAccelerators")
    Memory_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-memory""", alias="Memory")
    PlacementConstraints_: Optional[List['TaskDefinitionPlacementConstraint']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-placementconstraints""", alias="PlacementConstraints")
    Cpu_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-cpu""", alias="Cpu")
    RequiresCompatibilities_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-requirescompatibilities""", alias="RequiresCompatibilities")
    NetworkMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-networkmode""", alias="NetworkMode")
    PidMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-pidmode""", alias="PidMode")
    ExecutionRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-executionrolearn""", alias="ExecutionRoleArn")
    RuntimePlatform_: Optional['RuntimePlatform'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-runtimeplatform""", alias="RuntimePlatform")
    ProxyConfiguration_: Optional['ProxyConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-proxyconfiguration""", alias="ProxyConfiguration")
    Volumes_: Optional[List['Volume']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-volumes""", alias="Volumes")
    ContainerDefinitions_: Optional[List['ContainerDefinition']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-containerdefinitions""", alias="ContainerDefinitions")
    Family_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-family""", alias="Family")
    EphemeralStorage_: Optional['EphemeralStorage'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-ephemeralstorage""", alias="EphemeralStorage")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ecs.TaskDefinition:
        from troposphere.ecs import TaskDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ecs import TaskDefinition as TropoT
        return resource_to_troposphere(self, TropoT)


class TaskSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html
    Properties:
        - Name: PlatformVersion
        - Name: TaskDefinition
        - Name: ExternalId
        - Name: Cluster
        - Name: LoadBalancers
        - Name: Service
        - Name: NetworkConfiguration
        - Name: Scale
        - Name: ServiceRegistries
        - Name: LaunchType
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PlatformVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html#cfn-ecs-taskset-platformversion""", alias="PlatformVersion")
    TaskDefinition_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html#cfn-ecs-taskset-taskdefinition""", alias="TaskDefinition")
    ExternalId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html#cfn-ecs-taskset-externalid""", alias="ExternalId")
    Cluster_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html#cfn-ecs-taskset-cluster""", alias="Cluster")
    LoadBalancers_: Optional[List['LoadBalancer']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html#cfn-ecs-taskset-loadbalancers""", alias="LoadBalancers")
    Service_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html#cfn-ecs-taskset-service""", alias="Service")
    NetworkConfiguration_: Optional['NetworkConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html#cfn-ecs-taskset-networkconfiguration""", alias="NetworkConfiguration")
    Scale_: Optional['Scale'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html#cfn-ecs-taskset-scale""", alias="Scale")
    ServiceRegistries_: Optional[List['ServiceRegistry']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html#cfn-ecs-taskset-serviceregistries""", alias="ServiceRegistries")
    LaunchType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html#cfn-ecs-taskset-launchtype""", alias="LaunchType")
    

    @property
    def tropo_type(self) -> troposphere.ecs.TaskSet:
        from troposphere.ecs import TaskSet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ecs import TaskSet as TropoT
        return resource_to_troposphere(self, TropoT)

