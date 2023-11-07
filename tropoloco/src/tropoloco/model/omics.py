from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class ReferenceItem(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-referenceitem.html
    Properties:
        - Name: ReferenceArn
    
    """
    
    ReferenceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-referenceitem.html#cfn-omics-annotationstore-referenceitem-referencearn""", alias="ReferenceArn")
    


    @property
    def tropo_type(self) -> troposphere.omics.ReferenceItem:
        from troposphere.omics import ReferenceItem as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SseConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-sseconfig.html
    Properties:
        - Name: Type
        - Name: KeyArn
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-sseconfig.html#cfn-omics-annotationstore-sseconfig-type""", alias="Type")
    KeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-sseconfig.html#cfn-omics-annotationstore-sseconfig-keyarn""", alias="KeyArn")
    


    @property
    def tropo_type(self) -> troposphere.omics.SseConfig:
        from troposphere.omics import SseConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StoreOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-storeoptions.html
    Properties:
        - Name: TsvStoreOptions
    
    """
    
    TsvStoreOptions_: 'TsvStoreOptions' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-storeoptions.html#cfn-omics-annotationstore-storeoptions-tsvstoreoptions""", alias="TsvStoreOptions")
    


    @property
    def tropo_type(self) -> troposphere.omics.StoreOptions:
        from troposphere.omics import StoreOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TsvStoreOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-tsvstoreoptions.html
    Properties:
        - Name: Schema
        - Name: FormatToHeader
        - Name: AnnotationType
    
    """
    
    Schema_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-tsvstoreoptions.html#cfn-omics-annotationstore-tsvstoreoptions-schema""", alias="Schema")
    FormatToHeader_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-tsvstoreoptions.html#cfn-omics-annotationstore-tsvstoreoptions-formattoheader""", alias="FormatToHeader")
    AnnotationType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-tsvstoreoptions.html#cfn-omics-annotationstore-tsvstoreoptions-annotationtype""", alias="AnnotationType")
    


    @property
    def tropo_type(self) -> troposphere.omics.TsvStoreOptions:
        from troposphere.omics import TsvStoreOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SseConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-referencestore-sseconfig.html
    Properties:
        - Name: Type
        - Name: KeyArn
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-referencestore-sseconfig.html#cfn-omics-referencestore-sseconfig-type""", alias="Type")
    KeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-referencestore-sseconfig.html#cfn-omics-referencestore-sseconfig-keyarn""", alias="KeyArn")
    


    @property
    def tropo_type(self) -> troposphere.omics.SseConfig:
        from troposphere.omics import SseConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SseConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-sequencestore-sseconfig.html
    Properties:
        - Name: Type
        - Name: KeyArn
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-sequencestore-sseconfig.html#cfn-omics-sequencestore-sseconfig-type""", alias="Type")
    KeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-sequencestore-sseconfig.html#cfn-omics-sequencestore-sseconfig-keyarn""", alias="KeyArn")
    


    @property
    def tropo_type(self) -> troposphere.omics.SseConfig:
        from troposphere.omics import SseConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReferenceItem(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-variantstore-referenceitem.html
    Properties:
        - Name: ReferenceArn
    
    """
    
    ReferenceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-variantstore-referenceitem.html#cfn-omics-variantstore-referenceitem-referencearn""", alias="ReferenceArn")
    


    @property
    def tropo_type(self) -> troposphere.omics.ReferenceItem:
        from troposphere.omics import ReferenceItem as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SseConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-variantstore-sseconfig.html
    Properties:
        - Name: Type
        - Name: KeyArn
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-variantstore-sseconfig.html#cfn-omics-variantstore-sseconfig-type""", alias="Type")
    KeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-variantstore-sseconfig.html#cfn-omics-variantstore-sseconfig-keyarn""", alias="KeyArn")
    


    @property
    def tropo_type(self) -> troposphere.omics.SseConfig:
        from troposphere.omics import SseConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WorkflowParameter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflow-workflowparameter.html
    Properties:
        - Name: Description
        - Name: Optional
    
    """
    
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflow-workflowparameter.html#cfn-omics-workflow-workflowparameter-description""", alias="Description")
    Optional_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflow-workflowparameter.html#cfn-omics-workflow-workflowparameter-optional""", alias="Optional")
    


    @property
    def tropo_type(self) -> troposphere.omics.WorkflowParameter:
        from troposphere.omics import WorkflowParameter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class AnnotationStore(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-annotationstore.html
    Properties:
        - Name: StoreFormat
        - Name: Description
        - Name: Reference
        - Name: SseConfig
        - Name: StoreOptions
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Status
        - Name: CreationTime
        - Name: UpdateTime
        - Name: Id
        - Name: StoreSizeBytes
        - Name: StatusMessage
        - Name: StoreArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    StoreFormat_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-annotationstore.html#cfn-omics-annotationstore-storeformat""", alias="StoreFormat")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-annotationstore.html#cfn-omics-annotationstore-description""", alias="Description")
    Reference_: Optional['ReferenceItem'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-annotationstore.html#cfn-omics-annotationstore-reference""", alias="Reference")
    SseConfig_: Optional['SseConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-annotationstore.html#cfn-omics-annotationstore-sseconfig""", alias="SseConfig")
    StoreOptions_: Optional['StoreOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-annotationstore.html#cfn-omics-annotationstore-storeoptions""", alias="StoreOptions")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-annotationstore.html#cfn-omics-annotationstore-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-annotationstore.html#cfn-omics-annotationstore-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.omics.AnnotationStore:
        from troposphere.omics import AnnotationStore as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.omics import AnnotationStore as TropoT
        return resource_to_troposphere(self, TropoT)


class ReferenceStore(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-referencestore.html
    Properties:
        - Name: Description
        - Name: SseConfig
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: ReferenceStoreId
        - Name: CreationTime
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-referencestore.html#cfn-omics-referencestore-description""", alias="Description")
    SseConfig_: Optional['SseConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-referencestore.html#cfn-omics-referencestore-sseconfig""", alias="SseConfig")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-referencestore.html#cfn-omics-referencestore-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-referencestore.html#cfn-omics-referencestore-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.omics.ReferenceStore:
        from troposphere.omics import ReferenceStore as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.omics import ReferenceStore as TropoT
        return resource_to_troposphere(self, TropoT)


class RunGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-rungroup.html
    Properties:
        - Name: MaxDuration
        - Name: MaxGpus
        - Name: MaxRuns
        - Name: MaxCpus
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: CreationTime
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MaxDuration_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-rungroup.html#cfn-omics-rungroup-maxduration""", alias="MaxDuration")
    MaxGpus_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-rungroup.html#cfn-omics-rungroup-maxgpus""", alias="MaxGpus")
    MaxRuns_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-rungroup.html#cfn-omics-rungroup-maxruns""", alias="MaxRuns")
    MaxCpus_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-rungroup.html#cfn-omics-rungroup-maxcpus""", alias="MaxCpus")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-rungroup.html#cfn-omics-rungroup-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-rungroup.html#cfn-omics-rungroup-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.omics.RunGroup:
        from troposphere.omics import RunGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.omics import RunGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class SequenceStore(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-sequencestore.html
    Properties:
        - Name: Description
        - Name: FallbackLocation
        - Name: SseConfig
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: SequenceStoreId
        - Name: CreationTime
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-sequencestore.html#cfn-omics-sequencestore-description""", alias="Description")
    FallbackLocation_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-sequencestore.html#cfn-omics-sequencestore-fallbacklocation""", alias="FallbackLocation")
    SseConfig_: Optional['SseConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-sequencestore.html#cfn-omics-sequencestore-sseconfig""", alias="SseConfig")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-sequencestore.html#cfn-omics-sequencestore-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-sequencestore.html#cfn-omics-sequencestore-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.omics.SequenceStore:
        from troposphere.omics import SequenceStore as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.omics import SequenceStore as TropoT
        return resource_to_troposphere(self, TropoT)


class VariantStore(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-variantstore.html
    Properties:
        - Name: Description
        - Name: Reference
        - Name: SseConfig
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Status
        - Name: CreationTime
        - Name: UpdateTime
        - Name: Id
        - Name: StoreSizeBytes
        - Name: StatusMessage
        - Name: StoreArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-variantstore.html#cfn-omics-variantstore-description""", alias="Description")
    Reference_: 'ReferenceItem' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-variantstore.html#cfn-omics-variantstore-reference""", alias="Reference")
    SseConfig_: Optional['SseConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-variantstore.html#cfn-omics-variantstore-sseconfig""", alias="SseConfig")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-variantstore.html#cfn-omics-variantstore-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-variantstore.html#cfn-omics-variantstore-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.omics.VariantStore:
        from troposphere.omics import VariantStore as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.omics import VariantStore as TropoT
        return resource_to_troposphere(self, TropoT)


class Workflow(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html
    Properties:
        - Name: ParameterTemplate
        - Name: Description
        - Name: StorageCapacity
        - Name: Accelerators
        - Name: DefinitionUri
        - Name: Main
        - Name: Engine
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Status
        - Name: Type
        - Name: CreationTime
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ParameterTemplate_: Optional[Dict[str, 'WorkflowParameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-parametertemplate""", alias="ParameterTemplate")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-description""", alias="Description")
    StorageCapacity_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-storagecapacity""", alias="StorageCapacity")
    Accelerators_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-accelerators""", alias="Accelerators")
    DefinitionUri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-definitionuri""", alias="DefinitionUri")
    Main_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-main""", alias="Main")
    Engine_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-engine""", alias="Engine")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.omics.Workflow:
        from troposphere.omics import Workflow as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.omics import Workflow as TropoT
        return resource_to_troposphere(self, TropoT)

