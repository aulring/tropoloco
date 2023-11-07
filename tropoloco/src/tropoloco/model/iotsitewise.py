from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AccessPolicyIdentity(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-accesspolicyidentity.html
    Properties:
        - Name: User
        - Name: IamUser
        - Name: IamRole
    
    """
    
    User_: Optional['User'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-accesspolicyidentity.html#cfn-iotsitewise-accesspolicy-accesspolicyidentity-user""", alias="User")
    IamUser_: Optional['IamUser'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-accesspolicyidentity.html#cfn-iotsitewise-accesspolicy-accesspolicyidentity-iamuser""", alias="IamUser")
    IamRole_: Optional['IamRole'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-accesspolicyidentity.html#cfn-iotsitewise-accesspolicy-accesspolicyidentity-iamrole""", alias="IamRole")
    


    @property
    def tropo_type(self) -> troposphere.iotsitewise.AccessPolicyIdentity:
        from troposphere.iotsitewise import AccessPolicyIdentity as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AccessPolicyResource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-accesspolicyresource.html
    Properties:
        - Name: Project
        - Name: Portal
    
    """
    
    Project_: Optional['Project'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-accesspolicyresource.html#cfn-iotsitewise-accesspolicy-accesspolicyresource-project""", alias="Project")
    Portal_: Optional['Portal'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-accesspolicyresource.html#cfn-iotsitewise-accesspolicy-accesspolicyresource-portal""", alias="Portal")
    


    @property
    def tropo_type(self) -> troposphere.iotsitewise.AccessPolicyResource:
        from troposphere.iotsitewise import AccessPolicyResource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IamRole(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-iamrole.html
    Properties:
        - Name: arn
    
    """
    
    arn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-iamrole.html#cfn-iotsitewise-accesspolicy-iamrole-arn""", alias="arn")
    


    @property
    def tropo_type(self) -> troposphere.iotsitewise.IamRole:
        from troposphere.iotsitewise import IamRole as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IamUser(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-iamuser.html
    Properties:
        - Name: arn
    
    """
    
    arn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-iamuser.html#cfn-iotsitewise-accesspolicy-iamuser-arn""", alias="arn")
    


    @property
    def tropo_type(self) -> troposphere.iotsitewise.IamUser:
        from troposphere.iotsitewise import IamUser as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Portal(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-portal.html
    Properties:
        - Name: id
    
    """
    
    id_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-portal.html#cfn-iotsitewise-accesspolicy-portal-id""", alias="id")
    


    @property
    def tropo_type(self) -> troposphere.iotsitewise.Portal:
        from troposphere.iotsitewise import Portal as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Project(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-project.html
    Properties:
        - Name: id
    
    """
    
    id_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-project.html#cfn-iotsitewise-accesspolicy-project-id""", alias="id")
    


    @property
    def tropo_type(self) -> troposphere.iotsitewise.Project:
        from troposphere.iotsitewise import Project as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class User(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-user.html
    Properties:
        - Name: id
    
    """
    
    id_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-user.html#cfn-iotsitewise-accesspolicy-user-id""", alias="id")
    


    @property
    def tropo_type(self) -> troposphere.iotsitewise.User:
        from troposphere.iotsitewise import User as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AssetHierarchy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-asset-assethierarchy.html
    Properties:
        - Name: LogicalId
        - Name: ChildAssetId
    
    """
    
    LogicalId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-asset-assethierarchy.html#cfn-iotsitewise-asset-assethierarchy-logicalid""", alias="LogicalId")
    ChildAssetId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-asset-assethierarchy.html#cfn-iotsitewise-asset-assethierarchy-childassetid""", alias="ChildAssetId")
    


    @property
    def tropo_type(self) -> troposphere.iotsitewise.AssetHierarchy:
        from troposphere.iotsitewise import AssetHierarchy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AssetProperty(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-asset-assetproperty.html
    Properties:
        - Name: LogicalId
        - Name: Alias
        - Name: Unit
        - Name: NotificationState
    
    """
    
    LogicalId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-asset-assetproperty.html#cfn-iotsitewise-asset-assetproperty-logicalid""", alias="LogicalId")
    Alias_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-asset-assetproperty.html#cfn-iotsitewise-asset-assetproperty-alias""", alias="Alias")
    Unit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-asset-assetproperty.html#cfn-iotsitewise-asset-assetproperty-unit""", alias="Unit")
    NotificationState_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-asset-assetproperty.html#cfn-iotsitewise-asset-assetproperty-notificationstate""", alias="NotificationState")
    


    @property
    def tropo_type(self) -> troposphere.iotsitewise.AssetProperty:
        from troposphere.iotsitewise import AssetProperty as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AssetModelCompositeModel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel.html
    Properties:
        - Name: Type
        - Name: Description
        - Name: CompositeModelProperties
        - Name: Name
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel.html#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-type""", alias="Type")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel.html#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-description""", alias="Description")
    CompositeModelProperties_: Optional[List['AssetModelProperty']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel.html#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-compositemodelproperties""", alias="CompositeModelProperties")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel.html#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.iotsitewise.AssetModelCompositeModel:
        from troposphere.iotsitewise import AssetModelCompositeModel as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AssetModelHierarchy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelhierarchy.html
    Properties:
        - Name: LogicalId
        - Name: ChildAssetModelId
        - Name: Name
    
    """
    
    LogicalId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelhierarchy.html#cfn-iotsitewise-assetmodel-assetmodelhierarchy-logicalid""", alias="LogicalId")
    ChildAssetModelId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelhierarchy.html#cfn-iotsitewise-assetmodel-assetmodelhierarchy-childassetmodelid""", alias="ChildAssetModelId")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelhierarchy.html#cfn-iotsitewise-assetmodel-assetmodelhierarchy-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.iotsitewise.AssetModelHierarchy:
        from troposphere.iotsitewise import AssetModelHierarchy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AssetModelProperty(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelproperty.html
    Properties:
        - Name: Type
        - Name: LogicalId
        - Name: DataTypeSpec
        - Name: DataType
        - Name: Unit
        - Name: Name
    
    """
    
    Type_: 'PropertyType' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelproperty.html#cfn-iotsitewise-assetmodel-assetmodelproperty-type""", alias="Type")
    LogicalId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelproperty.html#cfn-iotsitewise-assetmodel-assetmodelproperty-logicalid""", alias="LogicalId")
    DataTypeSpec_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelproperty.html#cfn-iotsitewise-assetmodel-assetmodelproperty-datatypespec""", alias="DataTypeSpec")
    DataType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelproperty.html#cfn-iotsitewise-assetmodel-assetmodelproperty-datatype""", alias="DataType")
    Unit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelproperty.html#cfn-iotsitewise-assetmodel-assetmodelproperty-unit""", alias="Unit")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelproperty.html#cfn-iotsitewise-assetmodel-assetmodelproperty-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.iotsitewise.AssetModelProperty:
        from troposphere.iotsitewise import AssetModelProperty as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Attribute(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-attribute.html
    Properties:
        - Name: DefaultValue
    
    """
    
    DefaultValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-attribute.html#cfn-iotsitewise-assetmodel-attribute-defaultvalue""", alias="DefaultValue")
    


    @property
    def tropo_type(self) -> troposphere.iotsitewise.Attribute:
        from troposphere.iotsitewise import Attribute as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ExpressionVariable(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-expressionvariable.html
    Properties:
        - Name: Value
        - Name: Name
    
    """
    
    Value_: 'VariableValue' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-expressionvariable.html#cfn-iotsitewise-assetmodel-expressionvariable-value""", alias="Value")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-expressionvariable.html#cfn-iotsitewise-assetmodel-expressionvariable-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.iotsitewise.ExpressionVariable:
        from troposphere.iotsitewise import ExpressionVariable as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Metric(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-metric.html
    Properties:
        - Name: Variables
        - Name: Window
        - Name: Expression
    
    """
    
    Variables_: List['ExpressionVariable'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-metric.html#cfn-iotsitewise-assetmodel-metric-variables""", alias="Variables")
    Window_: 'MetricWindow' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-metric.html#cfn-iotsitewise-assetmodel-metric-window""", alias="Window")
    Expression_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-metric.html#cfn-iotsitewise-assetmodel-metric-expression""", alias="Expression")
    


    @property
    def tropo_type(self) -> troposphere.iotsitewise.Metric:
        from troposphere.iotsitewise import Metric as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetricWindow(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-metricwindow.html
    Properties:
        - Name: Tumbling
    
    """
    
    Tumbling_: Optional['TumblingWindow'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-metricwindow.html#cfn-iotsitewise-assetmodel-metricwindow-tumbling""", alias="Tumbling")
    


    @property
    def tropo_type(self) -> troposphere.iotsitewise.MetricWindow:
        from troposphere.iotsitewise import MetricWindow as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PropertyType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-propertytype.html
    Properties:
        - Name: TypeName
        - Name: Attribute
        - Name: Metric
        - Name: Transform
    
    """
    
    TypeName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-propertytype.html#cfn-iotsitewise-assetmodel-propertytype-typename""", alias="TypeName")
    Attribute_: Optional['Attribute'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-propertytype.html#cfn-iotsitewise-assetmodel-propertytype-attribute""", alias="Attribute")
    Metric_: Optional['Metric'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-propertytype.html#cfn-iotsitewise-assetmodel-propertytype-metric""", alias="Metric")
    Transform_: Optional['Transform'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-propertytype.html#cfn-iotsitewise-assetmodel-propertytype-transform""", alias="Transform")
    


    @property
    def tropo_type(self) -> troposphere.iotsitewise.PropertyType:
        from troposphere.iotsitewise import PropertyType as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Transform(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-transform.html
    Properties:
        - Name: Variables
        - Name: Expression
    
    """
    
    Variables_: List['ExpressionVariable'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-transform.html#cfn-iotsitewise-assetmodel-transform-variables""", alias="Variables")
    Expression_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-transform.html#cfn-iotsitewise-assetmodel-transform-expression""", alias="Expression")
    


    @property
    def tropo_type(self) -> troposphere.iotsitewise.Transform:
        from troposphere.iotsitewise import Transform as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TumblingWindow(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-tumblingwindow.html
    Properties:
        - Name: Interval
        - Name: Offset
    
    """
    
    Interval_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-tumblingwindow.html#cfn-iotsitewise-assetmodel-tumblingwindow-interval""", alias="Interval")
    Offset_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-tumblingwindow.html#cfn-iotsitewise-assetmodel-tumblingwindow-offset""", alias="Offset")
    


    @property
    def tropo_type(self) -> troposphere.iotsitewise.TumblingWindow:
        from troposphere.iotsitewise import TumblingWindow as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VariableValue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-variablevalue.html
    Properties:
        - Name: PropertyLogicalId
        - Name: HierarchyLogicalId
    
    """
    
    PropertyLogicalId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-variablevalue.html#cfn-iotsitewise-assetmodel-variablevalue-propertylogicalid""", alias="PropertyLogicalId")
    HierarchyLogicalId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-variablevalue.html#cfn-iotsitewise-assetmodel-variablevalue-hierarchylogicalid""", alias="HierarchyLogicalId")
    


    @property
    def tropo_type(self) -> troposphere.iotsitewise.VariableValue:
        from troposphere.iotsitewise import VariableValue as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GatewayCapabilitySummary(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-gatewaycapabilitysummary.html
    Properties:
        - Name: CapabilityNamespace
        - Name: CapabilityConfiguration
    
    """
    
    CapabilityNamespace_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-gatewaycapabilitysummary.html#cfn-iotsitewise-gateway-gatewaycapabilitysummary-capabilitynamespace""", alias="CapabilityNamespace")
    CapabilityConfiguration_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-gatewaycapabilitysummary.html#cfn-iotsitewise-gateway-gatewaycapabilitysummary-capabilityconfiguration""", alias="CapabilityConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.iotsitewise.GatewayCapabilitySummary:
        from troposphere.iotsitewise import GatewayCapabilitySummary as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GatewayPlatform(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-gatewayplatform.html
    Properties:
        - Name: GreengrassV2
        - Name: Greengrass
    
    """
    
    GreengrassV2_: Optional['GreengrassV2'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-gatewayplatform.html#cfn-iotsitewise-gateway-gatewayplatform-greengrassv2""", alias="GreengrassV2")
    Greengrass_: Optional['Greengrass'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-gatewayplatform.html#cfn-iotsitewise-gateway-gatewayplatform-greengrass""", alias="Greengrass")
    


    @property
    def tropo_type(self) -> troposphere.iotsitewise.GatewayPlatform:
        from troposphere.iotsitewise import GatewayPlatform as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Greengrass(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-greengrass.html
    Properties:
        - Name: GroupArn
    
    """
    
    GroupArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-greengrass.html#cfn-iotsitewise-gateway-greengrass-grouparn""", alias="GroupArn")
    


    @property
    def tropo_type(self) -> troposphere.iotsitewise.Greengrass:
        from troposphere.iotsitewise import Greengrass as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GreengrassV2(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-greengrassv2.html
    Properties:
        - Name: CoreDeviceThingName
    
    """
    
    CoreDeviceThingName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-greengrassv2.html#cfn-iotsitewise-gateway-greengrassv2-coredevicethingname""", alias="CoreDeviceThingName")
    


    @property
    def tropo_type(self) -> troposphere.iotsitewise.GreengrassV2:
        from troposphere.iotsitewise import GreengrassV2 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Alarms(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-portal-alarms.html
    Properties:
        - Name: NotificationLambdaArn
        - Name: AlarmRoleArn
    
    """
    
    NotificationLambdaArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-portal-alarms.html#cfn-iotsitewise-portal-alarms-notificationlambdaarn""", alias="NotificationLambdaArn")
    AlarmRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-portal-alarms.html#cfn-iotsitewise-portal-alarms-alarmrolearn""", alias="AlarmRoleArn")
    


    @property
    def tropo_type(self) -> troposphere.iotsitewise.Alarms:
        from troposphere.iotsitewise import Alarms as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class AccessPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html
    Properties:
        - Name: AccessPolicyResource
        - Name: AccessPolicyIdentity
        - Name: AccessPolicyPermission
    Attributes:
        - Name: AccessPolicyArn
        - Name: AccessPolicyId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AccessPolicyResource_: 'AccessPolicyResource' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html#cfn-iotsitewise-accesspolicy-accesspolicyresource""", alias="AccessPolicyResource")
    AccessPolicyIdentity_: 'AccessPolicyIdentity' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html#cfn-iotsitewise-accesspolicy-accesspolicyidentity""", alias="AccessPolicyIdentity")
    AccessPolicyPermission_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html#cfn-iotsitewise-accesspolicy-accesspolicypermission""", alias="AccessPolicyPermission")
    

    @property
    def tropo_type(self) -> troposphere.iotsitewise.AccessPolicy:
        from troposphere.iotsitewise import AccessPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotsitewise import AccessPolicy as TropoT
        return resource_to_troposphere(self, TropoT)


class Asset(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html
    Properties:
        - Name: AssetModelId
        - Name: AssetDescription
        - Name: AssetProperties
        - Name: AssetName
        - Name: Tags
        - Name: AssetHierarchies
    Attributes:
        - Name: AssetArn
        - Name: AssetId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AssetModelId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assetmodelid""", alias="AssetModelId")
    AssetDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assetdescription""", alias="AssetDescription")
    AssetProperties_: Optional[List['AssetProperty']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assetproperties""", alias="AssetProperties")
    AssetName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assetname""", alias="AssetName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-tags""", alias="Tags")
    AssetHierarchies_: Optional[List['AssetHierarchy']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assethierarchies""", alias="AssetHierarchies")
    

    @property
    def tropo_type(self) -> troposphere.iotsitewise.Asset:
        from troposphere.iotsitewise import Asset as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotsitewise import Asset as TropoT
        return resource_to_troposphere(self, TropoT)


class AssetModel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html
    Properties:
        - Name: AssetModelDescription
        - Name: AssetModelCompositeModels
        - Name: AssetModelName
        - Name: AssetModelHierarchies
        - Name: AssetModelProperties
        - Name: Tags
    Attributes:
        - Name: AssetModelId
        - Name: AssetModelArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AssetModelDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html#cfn-iotsitewise-assetmodel-assetmodeldescription""", alias="AssetModelDescription")
    AssetModelCompositeModels_: Optional[List['AssetModelCompositeModel']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html#cfn-iotsitewise-assetmodel-assetmodelcompositemodels""", alias="AssetModelCompositeModels")
    AssetModelName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html#cfn-iotsitewise-assetmodel-assetmodelname""", alias="AssetModelName")
    AssetModelHierarchies_: Optional[List['AssetModelHierarchy']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html#cfn-iotsitewise-assetmodel-assetmodelhierarchies""", alias="AssetModelHierarchies")
    AssetModelProperties_: Optional[List['AssetModelProperty']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html#cfn-iotsitewise-assetmodel-assetmodelproperties""", alias="AssetModelProperties")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html#cfn-iotsitewise-assetmodel-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iotsitewise.AssetModel:
        from troposphere.iotsitewise import AssetModel as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotsitewise import AssetModel as TropoT
        return resource_to_troposphere(self, TropoT)


class Dashboard(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.html
    Properties:
        - Name: DashboardName
        - Name: DashboardDefinition
        - Name: ProjectId
        - Name: DashboardDescription
        - Name: Tags
    Attributes:
        - Name: DashboardId
        - Name: DashboardArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DashboardName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.html#cfn-iotsitewise-dashboard-dashboardname""", alias="DashboardName")
    DashboardDefinition_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.html#cfn-iotsitewise-dashboard-dashboarddefinition""", alias="DashboardDefinition")
    ProjectId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.html#cfn-iotsitewise-dashboard-projectid""", alias="ProjectId")
    DashboardDescription_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.html#cfn-iotsitewise-dashboard-dashboarddescription""", alias="DashboardDescription")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.html#cfn-iotsitewise-dashboard-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iotsitewise.Dashboard:
        from troposphere.iotsitewise import Dashboard as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotsitewise import Dashboard as TropoT
        return resource_to_troposphere(self, TropoT)


class Gateway(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html
    Properties:
        - Name: GatewayCapabilitySummaries
        - Name: GatewayName
        - Name: GatewayPlatform
        - Name: Tags
    Attributes:
        - Name: GatewayId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    GatewayCapabilitySummaries_: Optional[List['GatewayCapabilitySummary']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html#cfn-iotsitewise-gateway-gatewaycapabilitysummaries""", alias="GatewayCapabilitySummaries")
    GatewayName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html#cfn-iotsitewise-gateway-gatewayname""", alias="GatewayName")
    GatewayPlatform_: 'GatewayPlatform' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html#cfn-iotsitewise-gateway-gatewayplatform""", alias="GatewayPlatform")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html#cfn-iotsitewise-gateway-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iotsitewise.Gateway:
        from troposphere.iotsitewise import Gateway as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotsitewise import Gateway as TropoT
        return resource_to_troposphere(self, TropoT)


class Portal(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html
    Properties:
        - Name: PortalName
        - Name: PortalAuthMode
        - Name: NotificationSenderEmail
        - Name: Alarms
        - Name: PortalContactEmail
        - Name: RoleArn
        - Name: Tags
        - Name: PortalDescription
    Attributes:
        - Name: PortalArn
        - Name: PortalStartUrl
        - Name: PortalId
        - Name: PortalClientId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PortalName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-portalname""", alias="PortalName")
    PortalAuthMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-portalauthmode""", alias="PortalAuthMode")
    NotificationSenderEmail_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-notificationsenderemail""", alias="NotificationSenderEmail")
    Alarms_: Optional['Alarms'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-alarms""", alias="Alarms")
    PortalContactEmail_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-portalcontactemail""", alias="PortalContactEmail")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-rolearn""", alias="RoleArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-tags""", alias="Tags")
    PortalDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-portaldescription""", alias="PortalDescription")
    

    @property
    def tropo_type(self) -> troposphere.iotsitewise.Portal:
        from troposphere.iotsitewise import Portal as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotsitewise import Portal as TropoT
        return resource_to_troposphere(self, TropoT)


class Project(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-project.html
    Properties:
        - Name: AssetIds
        - Name: ProjectName
        - Name: PortalId
        - Name: ProjectDescription
        - Name: Tags
    Attributes:
        - Name: ProjectArn
        - Name: ProjectId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AssetIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-project.html#cfn-iotsitewise-project-assetids""", alias="AssetIds")
    ProjectName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-project.html#cfn-iotsitewise-project-projectname""", alias="ProjectName")
    PortalId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-project.html#cfn-iotsitewise-project-portalid""", alias="PortalId")
    ProjectDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-project.html#cfn-iotsitewise-project-projectdescription""", alias="ProjectDescription")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-project.html#cfn-iotsitewise-project-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iotsitewise.Project:
        from troposphere.iotsitewise import Project as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotsitewise import Project as TropoT
        return resource_to_troposphere(self, TropoT)

