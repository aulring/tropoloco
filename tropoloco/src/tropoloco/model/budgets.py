from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AutoAdjustData(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-autoadjustdata.html
    Properties:
        - Name: AutoAdjustType
        - Name: HistoricalOptions
    
    """
    
    AutoAdjustType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-autoadjustdata.html#cfn-budgets-budget-autoadjustdata-autoadjusttype""", alias="AutoAdjustType")
    HistoricalOptions_: Optional['HistoricalOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-autoadjustdata.html#cfn-budgets-budget-autoadjustdata-historicaloptions""", alias="HistoricalOptions")
    


    @property
    def tropo_type(self) -> troposphere.budgets.AutoAdjustData:
        from troposphere.budgets import AutoAdjustData as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BudgetData(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html
    Properties:
        - Name: BudgetLimit
        - Name: TimePeriod
        - Name: AutoAdjustData
        - Name: TimeUnit
        - Name: PlannedBudgetLimits
        - Name: CostFilters
        - Name: BudgetName
        - Name: CostTypes
        - Name: BudgetType
    
    """
    
    BudgetLimit_: Optional['Spend'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-budgetlimit""", alias="BudgetLimit")
    TimePeriod_: Optional['TimePeriod'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-timeperiod""", alias="TimePeriod")
    AutoAdjustData_: Optional['AutoAdjustData'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-autoadjustdata""", alias="AutoAdjustData")
    TimeUnit_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-timeunit""", alias="TimeUnit")
    PlannedBudgetLimits_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-plannedbudgetlimits""", alias="PlannedBudgetLimits")
    CostFilters_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-costfilters""", alias="CostFilters")
    BudgetName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-budgetname""", alias="BudgetName")
    CostTypes_: Optional['CostTypes'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-costtypes""", alias="CostTypes")
    BudgetType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-budgettype""", alias="BudgetType")
    


    @property
    def tropo_type(self) -> troposphere.budgets.BudgetData:
        from troposphere.budgets import BudgetData as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CostTypes(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html
    Properties:
        - Name: IncludeSupport
        - Name: IncludeOtherSubscription
        - Name: IncludeTax
        - Name: IncludeSubscription
        - Name: UseBlended
        - Name: IncludeUpfront
        - Name: IncludeDiscount
        - Name: IncludeCredit
        - Name: IncludeRecurring
        - Name: UseAmortized
        - Name: IncludeRefund
    
    """
    
    IncludeSupport_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includesupport""", alias="IncludeSupport")
    IncludeOtherSubscription_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includeothersubscription""", alias="IncludeOtherSubscription")
    IncludeTax_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includetax""", alias="IncludeTax")
    IncludeSubscription_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includesubscription""", alias="IncludeSubscription")
    UseBlended_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-useblended""", alias="UseBlended")
    IncludeUpfront_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includeupfront""", alias="IncludeUpfront")
    IncludeDiscount_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includediscount""", alias="IncludeDiscount")
    IncludeCredit_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includecredit""", alias="IncludeCredit")
    IncludeRecurring_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includerecurring""", alias="IncludeRecurring")
    UseAmortized_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-useamortized""", alias="UseAmortized")
    IncludeRefund_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includerefund""", alias="IncludeRefund")
    


    @property
    def tropo_type(self) -> troposphere.budgets.CostTypes:
        from troposphere.budgets import CostTypes as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HistoricalOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-historicaloptions.html
    Properties:
        - Name: BudgetAdjustmentPeriod
    
    """
    
    BudgetAdjustmentPeriod_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-historicaloptions.html#cfn-budgets-budget-historicaloptions-budgetadjustmentperiod""", alias="BudgetAdjustmentPeriod")
    


    @property
    def tropo_type(self) -> troposphere.budgets.HistoricalOptions:
        from troposphere.budgets import HistoricalOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Notification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notification.html
    Properties:
        - Name: ComparisonOperator
        - Name: NotificationType
        - Name: Threshold
        - Name: ThresholdType
    
    """
    
    ComparisonOperator_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notification.html#cfn-budgets-budget-notification-comparisonoperator""", alias="ComparisonOperator")
    NotificationType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notification.html#cfn-budgets-budget-notification-notificationtype""", alias="NotificationType")
    Threshold_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notification.html#cfn-budgets-budget-notification-threshold""", alias="Threshold")
    ThresholdType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notification.html#cfn-budgets-budget-notification-thresholdtype""", alias="ThresholdType")
    


    @property
    def tropo_type(self) -> troposphere.budgets.Notification:
        from troposphere.budgets import Notification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NotificationWithSubscribers(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notificationwithsubscribers.html
    Properties:
        - Name: Subscribers
        - Name: Notification
    
    """
    
    Subscribers_: List['Subscriber'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notificationwithsubscribers.html#cfn-budgets-budget-notificationwithsubscribers-subscribers""", alias="Subscribers")
    Notification_: 'Notification' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notificationwithsubscribers.html#cfn-budgets-budget-notificationwithsubscribers-notification""", alias="Notification")
    


    @property
    def tropo_type(self) -> troposphere.budgets.NotificationWithSubscribers:
        from troposphere.budgets import NotificationWithSubscribers as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Spend(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-spend.html
    Properties:
        - Name: Amount
        - Name: Unit
    
    """
    
    Amount_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-spend.html#cfn-budgets-budget-spend-amount""", alias="Amount")
    Unit_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-spend.html#cfn-budgets-budget-spend-unit""", alias="Unit")
    


    @property
    def tropo_type(self) -> troposphere.budgets.Spend:
        from troposphere.budgets import Spend as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Subscriber(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-subscriber.html
    Properties:
        - Name: SubscriptionType
        - Name: Address
    
    """
    
    SubscriptionType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-subscriber.html#cfn-budgets-budget-subscriber-subscriptiontype""", alias="SubscriptionType")
    Address_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-subscriber.html#cfn-budgets-budget-subscriber-address""", alias="Address")
    


    @property
    def tropo_type(self) -> troposphere.budgets.Subscriber:
        from troposphere.budgets import Subscriber as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TimePeriod(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-timeperiod.html
    Properties:
        - Name: Start
        - Name: End
    
    """
    
    Start_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-timeperiod.html#cfn-budgets-budget-timeperiod-start""", alias="Start")
    End_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-timeperiod.html#cfn-budgets-budget-timeperiod-end""", alias="End")
    


    @property
    def tropo_type(self) -> troposphere.budgets.TimePeriod:
        from troposphere.budgets import TimePeriod as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ActionThreshold(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-actionthreshold.html
    Properties:
        - Name: Type
        - Name: Value
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-actionthreshold.html#cfn-budgets-budgetsaction-actionthreshold-type""", alias="Type")
    Value_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-actionthreshold.html#cfn-budgets-budgetsaction-actionthreshold-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.budgets.ActionThreshold:
        from troposphere.budgets import ActionThreshold as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Definition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-definition.html
    Properties:
        - Name: SsmActionDefinition
        - Name: IamActionDefinition
        - Name: ScpActionDefinition
    
    """
    
    SsmActionDefinition_: Optional['SsmActionDefinition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-definition.html#cfn-budgets-budgetsaction-definition-ssmactiondefinition""", alias="SsmActionDefinition")
    IamActionDefinition_: Optional['IamActionDefinition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-definition.html#cfn-budgets-budgetsaction-definition-iamactiondefinition""", alias="IamActionDefinition")
    ScpActionDefinition_: Optional['ScpActionDefinition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-definition.html#cfn-budgets-budgetsaction-definition-scpactiondefinition""", alias="ScpActionDefinition")
    


    @property
    def tropo_type(self) -> troposphere.budgets.Definition:
        from troposphere.budgets import Definition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IamActionDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-iamactiondefinition.html
    Properties:
        - Name: PolicyArn
        - Name: Groups
        - Name: Roles
        - Name: Users
    
    """
    
    PolicyArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-iamactiondefinition.html#cfn-budgets-budgetsaction-iamactiondefinition-policyarn""", alias="PolicyArn")
    Groups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-iamactiondefinition.html#cfn-budgets-budgetsaction-iamactiondefinition-groups""", alias="Groups")
    Roles_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-iamactiondefinition.html#cfn-budgets-budgetsaction-iamactiondefinition-roles""", alias="Roles")
    Users_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-iamactiondefinition.html#cfn-budgets-budgetsaction-iamactiondefinition-users""", alias="Users")
    


    @property
    def tropo_type(self) -> troposphere.budgets.IamActionDefinition:
        from troposphere.budgets import IamActionDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ScpActionDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-scpactiondefinition.html
    Properties:
        - Name: TargetIds
        - Name: PolicyId
    
    """
    
    TargetIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-scpactiondefinition.html#cfn-budgets-budgetsaction-scpactiondefinition-targetids""", alias="TargetIds")
    PolicyId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-scpactiondefinition.html#cfn-budgets-budgetsaction-scpactiondefinition-policyid""", alias="PolicyId")
    


    @property
    def tropo_type(self) -> troposphere.budgets.ScpActionDefinition:
        from troposphere.budgets import ScpActionDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SsmActionDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-ssmactiondefinition.html
    Properties:
        - Name: Region
        - Name: InstanceIds
        - Name: Subtype
    
    """
    
    Region_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-ssmactiondefinition.html#cfn-budgets-budgetsaction-ssmactiondefinition-region""", alias="Region")
    InstanceIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-ssmactiondefinition.html#cfn-budgets-budgetsaction-ssmactiondefinition-instanceids""", alias="InstanceIds")
    Subtype_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-ssmactiondefinition.html#cfn-budgets-budgetsaction-ssmactiondefinition-subtype""", alias="Subtype")
    


    @property
    def tropo_type(self) -> troposphere.budgets.SsmActionDefinition:
        from troposphere.budgets import SsmActionDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Subscriber(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-subscriber.html
    Properties:
        - Name: Type
        - Name: Address
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-subscriber.html#cfn-budgets-budgetsaction-subscriber-type""", alias="Type")
    Address_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-subscriber.html#cfn-budgets-budgetsaction-subscriber-address""", alias="Address")
    


    @property
    def tropo_type(self) -> troposphere.budgets.Subscriber:
        from troposphere.budgets import Subscriber as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Budget(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budget.html
    Properties:
        - Name: NotificationsWithSubscribers
        - Name: Budget
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    NotificationsWithSubscribers_: Optional[List['NotificationWithSubscribers']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budget.html#cfn-budgets-budget-notificationswithsubscribers""", alias="NotificationsWithSubscribers")
    Budget_: 'BudgetData' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budget.html#cfn-budgets-budget-budget""", alias="Budget")
    

    @property
    def tropo_type(self) -> troposphere.budgets.Budget:
        from troposphere.budgets import Budget as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.budgets import Budget as TropoT
        return resource_to_troposphere(self, TropoT)


class BudgetsAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html
    Properties:
        - Name: ExecutionRoleArn
        - Name: ActionType
        - Name: NotificationType
        - Name: ActionThreshold
        - Name: Definition
        - Name: ApprovalModel
        - Name: Subscribers
        - Name: BudgetName
    Attributes:
        - Name: ActionId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ExecutionRoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-executionrolearn""", alias="ExecutionRoleArn")
    ActionType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-actiontype""", alias="ActionType")
    NotificationType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-notificationtype""", alias="NotificationType")
    ActionThreshold_: 'ActionThreshold' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-actionthreshold""", alias="ActionThreshold")
    Definition_: 'Definition' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-definition""", alias="Definition")
    ApprovalModel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-approvalmodel""", alias="ApprovalModel")
    Subscribers_: List['Subscriber'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-subscribers""", alias="Subscribers")
    BudgetName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-budgetname""", alias="BudgetName")
    

    @property
    def tropo_type(self) -> troposphere.budgets.BudgetsAction:
        from troposphere.budgets import BudgetsAction as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.budgets import BudgetsAction as TropoT
        return resource_to_troposphere(self, TropoT)

