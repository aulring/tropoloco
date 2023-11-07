from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################


class VpcConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codetest-persistentconfiguration-vpcconfig.html
    Properties:
        - Name: Subnets
        - Name: SecurityGroupIds

    """

    Subnets_: Optional[List[str]] = Field(
        None,
        description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codetest-persistentconfiguration-vpcconfig.html#cfn-codetest-persistentconfiguration-vpcconfig-subnets""",
        alias="Subnets",
    )
    SecurityGroupIds_: Optional[List[str]] = Field(
        None,
        description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codetest-persistentconfiguration-vpcconfig.html#cfn-codetest-persistentconfiguration-vpcconfig-securitygroupids""",
        alias="SecurityGroupIds",
    )

    @property
    def tropo_type(self) -> troposphere.codetest.VpcConfig:
        from troposphere.codetest import VpcConfig as TropoT

        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)


######################################################################
# AWS Resource
######################################################################


class PersistentConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codetest-persistentconfiguration.html
    Properties:
        - Name: Version
        - Name: VpcConfig
        - Name: Name
        - Name: ResultsRoleArn
    Attributes:
        - Name: Name
    """

    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Version_: Optional[str] = Field(
        None,
        description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codetest-persistentconfiguration.html#cfn-codetest-persistentconfiguration-version""",
        alias="Version",
    )
    VpcConfig_: Optional["VpcConfig"] = Field(
        None,
        description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codetest-persistentconfiguration.html#cfn-codetest-persistentconfiguration-vpcconfig""",
        alias="VpcConfig",
    )
    Name_: Optional[str] = Field(
        None,
        description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codetest-persistentconfiguration.html#cfn-codetest-persistentconfiguration-name""",
        alias="Name",
    )
    ResultsRoleArn_: str = Field(
        description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codetest-persistentconfiguration.html#cfn-codetest-persistentconfiguration-resultsrolearn""",
        alias="ResultsRoleArn",
    )

    def to_troposphere(self):
        from troposphere.codetest import PersistentConfiguration as TropoT

        return resource_to_troposphere(self, TropoT)


class Series(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codetest-series.html
    Properties:
        - Name: RunDefinition
        - Name: State
        - Name: PersistentConfigurationId
        - Name: Name
    """

    title: str = Field(description="Title of cloudformation resource.", alias="title")
    RunDefinition_: Dict = Field(
        description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codetest-series.html#cfn-codetest-series-rundefinition""",
        alias="RunDefinition",
    )
    State_: str = Field(
        description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codetest-series.html#cfn-codetest-series-state""",
        alias="State",
    )
    PersistentConfigurationId_: str = Field(
        description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codetest-series.html#cfn-codetest-series-persistentconfigurationid""",
        alias="PersistentConfigurationId",
    )
    Name_: Optional[str] = Field(
        None,
        description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codetest-series.html#cfn-codetest-series-name""",
        alias="Name",
    )

    def to_troposphere(self):
        from troposphere.codetest import Series as TropoT

        return resource_to_troposphere(self, TropoT)
