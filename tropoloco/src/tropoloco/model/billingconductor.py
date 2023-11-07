from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AccountGrouping(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-billinggroup-accountgrouping.html
    Properties:
        - Name: LinkedAccountIds
        - Name: AutoAssociate
    
    """
    
    LinkedAccountIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-billinggroup-accountgrouping.html#cfn-billingconductor-billinggroup-accountgrouping-linkedaccountids""", alias="LinkedAccountIds")
    AutoAssociate_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-billinggroup-accountgrouping.html#cfn-billingconductor-billinggroup-accountgrouping-autoassociate""", alias="AutoAssociate")
    


    @property
    def tropo_type(self) -> troposphere.billingconductor.AccountGrouping:
        from troposphere.billingconductor import AccountGrouping as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ComputationPreference(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-billinggroup-computationpreference.html
    Properties:
        - Name: PricingPlanArn
    
    """
    
    PricingPlanArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-billinggroup-computationpreference.html#cfn-billingconductor-billinggroup-computationpreference-pricingplanarn""", alias="PricingPlanArn")
    


    @property
    def tropo_type(self) -> troposphere.billingconductor.ComputationPreference:
        from troposphere.billingconductor import ComputationPreference as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BillingPeriodRange(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-billingperiodrange.html
    Properties:
        - Name: ExclusiveEndBillingPeriod
        - Name: InclusiveStartBillingPeriod
    
    """
    
    ExclusiveEndBillingPeriod_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-billingperiodrange.html#cfn-billingconductor-customlineitem-billingperiodrange-exclusiveendbillingperiod""", alias="ExclusiveEndBillingPeriod")
    InclusiveStartBillingPeriod_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-billingperiodrange.html#cfn-billingconductor-customlineitem-billingperiodrange-inclusivestartbillingperiod""", alias="InclusiveStartBillingPeriod")
    


    @property
    def tropo_type(self) -> troposphere.billingconductor.BillingPeriodRange:
        from troposphere.billingconductor import BillingPeriodRange as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomLineItemChargeDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-customlineitemchargedetails.html
    Properties:
        - Name: LineItemFilters
        - Name: Type
        - Name: Percentage
        - Name: Flat
    
    """
    
    LineItemFilters_: Optional[List['LineItemFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-customlineitemchargedetails.html#cfn-billingconductor-customlineitem-customlineitemchargedetails-lineitemfilters""", alias="LineItemFilters")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-customlineitemchargedetails.html#cfn-billingconductor-customlineitem-customlineitemchargedetails-type""", alias="Type")
    Percentage_: Optional['CustomLineItemPercentageChargeDetails'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-customlineitemchargedetails.html#cfn-billingconductor-customlineitem-customlineitemchargedetails-percentage""", alias="Percentage")
    Flat_: Optional['CustomLineItemFlatChargeDetails'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-customlineitemchargedetails.html#cfn-billingconductor-customlineitem-customlineitemchargedetails-flat""", alias="Flat")
    


    @property
    def tropo_type(self) -> troposphere.billingconductor.CustomLineItemChargeDetails:
        from troposphere.billingconductor import CustomLineItemChargeDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomLineItemFlatChargeDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-customlineitemflatchargedetails.html
    Properties:
        - Name: ChargeValue
    
    """
    
    ChargeValue_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-customlineitemflatchargedetails.html#cfn-billingconductor-customlineitem-customlineitemflatchargedetails-chargevalue""", alias="ChargeValue")
    


    @property
    def tropo_type(self) -> troposphere.billingconductor.CustomLineItemFlatChargeDetails:
        from troposphere.billingconductor import CustomLineItemFlatChargeDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomLineItemPercentageChargeDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-customlineitempercentagechargedetails.html
    Properties:
        - Name: ChildAssociatedResources
        - Name: PercentageValue
    
    """
    
    ChildAssociatedResources_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-customlineitempercentagechargedetails.html#cfn-billingconductor-customlineitem-customlineitempercentagechargedetails-childassociatedresources""", alias="ChildAssociatedResources")
    PercentageValue_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-customlineitempercentagechargedetails.html#cfn-billingconductor-customlineitem-customlineitempercentagechargedetails-percentagevalue""", alias="PercentageValue")
    


    @property
    def tropo_type(self) -> troposphere.billingconductor.CustomLineItemPercentageChargeDetails:
        from troposphere.billingconductor import CustomLineItemPercentageChargeDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LineItemFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-lineitemfilter.html
    Properties:
        - Name: MatchOption
        - Name: Attribute
        - Name: Values
    
    """
    
    MatchOption_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-lineitemfilter.html#cfn-billingconductor-customlineitem-lineitemfilter-matchoption""", alias="MatchOption")
    Attribute_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-lineitemfilter.html#cfn-billingconductor-customlineitem-lineitemfilter-attribute""", alias="Attribute")
    Values_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-lineitemfilter.html#cfn-billingconductor-customlineitem-lineitemfilter-values""", alias="Values")
    


    @property
    def tropo_type(self) -> troposphere.billingconductor.LineItemFilter:
        from troposphere.billingconductor import LineItemFilter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FreeTier(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-pricingrule-freetier.html
    Properties:
        - Name: Activated
    
    """
    
    Activated_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-pricingrule-freetier.html#cfn-billingconductor-pricingrule-freetier-activated""", alias="Activated")
    


    @property
    def tropo_type(self) -> troposphere.billingconductor.FreeTier:
        from troposphere.billingconductor import FreeTier as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Tiering(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-pricingrule-tiering.html
    Properties:
        - Name: FreeTier
    
    """
    
    FreeTier_: Optional['FreeTier'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-pricingrule-tiering.html#cfn-billingconductor-pricingrule-tiering-freetier""", alias="FreeTier")
    


    @property
    def tropo_type(self) -> troposphere.billingconductor.Tiering:
        from troposphere.billingconductor import Tiering as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class BillingGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-billinggroup.html
    Properties:
        - Name: Description
        - Name: PrimaryAccountId
        - Name: ComputationPreference
        - Name: AccountGrouping
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Status
        - Name: Size
        - Name: StatusReason
        - Name: CreationTime
        - Name: LastModifiedTime
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-billinggroup.html#cfn-billingconductor-billinggroup-description""", alias="Description")
    PrimaryAccountId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-billinggroup.html#cfn-billingconductor-billinggroup-primaryaccountid""", alias="PrimaryAccountId")
    ComputationPreference_: 'ComputationPreference' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-billinggroup.html#cfn-billingconductor-billinggroup-computationpreference""", alias="ComputationPreference")
    AccountGrouping_: 'AccountGrouping' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-billinggroup.html#cfn-billingconductor-billinggroup-accountgrouping""", alias="AccountGrouping")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-billinggroup.html#cfn-billingconductor-billinggroup-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-billinggroup.html#cfn-billingconductor-billinggroup-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.billingconductor.BillingGroup:
        from troposphere.billingconductor import BillingGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.billingconductor import BillingGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class CustomLineItem(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-customlineitem.html
    Properties:
        - Name: BillingPeriodRange
        - Name: Description
        - Name: BillingGroupArn
        - Name: CustomLineItemChargeDetails
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: CurrencyCode
        - Name: ProductCode
        - Name: CreationTime
        - Name: LastModifiedTime
        - Name: Arn
        - Name: AssociationSize
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    BillingPeriodRange_: Optional['BillingPeriodRange'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-customlineitem.html#cfn-billingconductor-customlineitem-billingperiodrange""", alias="BillingPeriodRange")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-customlineitem.html#cfn-billingconductor-customlineitem-description""", alias="Description")
    BillingGroupArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-customlineitem.html#cfn-billingconductor-customlineitem-billinggrouparn""", alias="BillingGroupArn")
    CustomLineItemChargeDetails_: Optional['CustomLineItemChargeDetails'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-customlineitem.html#cfn-billingconductor-customlineitem-customlineitemchargedetails""", alias="CustomLineItemChargeDetails")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-customlineitem.html#cfn-billingconductor-customlineitem-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-customlineitem.html#cfn-billingconductor-customlineitem-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.billingconductor.CustomLineItem:
        from troposphere.billingconductor import CustomLineItem as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.billingconductor import CustomLineItem as TropoT
        return resource_to_troposphere(self, TropoT)


class PricingPlan(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingplan.html
    Properties:
        - Name: Description
        - Name: PricingRuleArns
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Size
        - Name: CreationTime
        - Name: LastModifiedTime
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingplan.html#cfn-billingconductor-pricingplan-description""", alias="Description")
    PricingRuleArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingplan.html#cfn-billingconductor-pricingplan-pricingrulearns""", alias="PricingRuleArns")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingplan.html#cfn-billingconductor-pricingplan-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingplan.html#cfn-billingconductor-pricingplan-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.billingconductor.PricingPlan:
        from troposphere.billingconductor import PricingPlan as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.billingconductor import PricingPlan as TropoT
        return resource_to_troposphere(self, TropoT)


class PricingRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html
    Properties:
        - Name: Type
        - Name: Description
        - Name: Scope
        - Name: Service
        - Name: ModifierPercentage
        - Name: Operation
        - Name: Tiering
        - Name: BillingEntity
        - Name: UsageType
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: CreationTime
        - Name: LastModifiedTime
        - Name: AssociatedPricingPlanCount
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-type""", alias="Type")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-description""", alias="Description")
    Scope_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-scope""", alias="Scope")
    Service_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-service""", alias="Service")
    ModifierPercentage_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-modifierpercentage""", alias="ModifierPercentage")
    Operation_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-operation""", alias="Operation")
    Tiering_: Optional['Tiering'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-tiering""", alias="Tiering")
    BillingEntity_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-billingentity""", alias="BillingEntity")
    UsageType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-usagetype""", alias="UsageType")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.billingconductor.PricingRule:
        from troposphere.billingconductor import PricingRule as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.billingconductor import PricingRule as TropoT
        return resource_to_troposphere(self, TropoT)

