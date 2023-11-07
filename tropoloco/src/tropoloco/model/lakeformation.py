from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class ColumnWildcard(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datacellsfilter-columnwildcard.html
    Properties:
        - Name: ExcludedColumnNames
    
    """
    
    ExcludedColumnNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datacellsfilter-columnwildcard.html#cfn-lakeformation-datacellsfilter-columnwildcard-excludedcolumnnames""", alias="ExcludedColumnNames")
    


    @property
    def tropo_type(self) -> troposphere.lakeformation.ColumnWildcard:
        from troposphere.lakeformation import ColumnWildcard as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RowFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datacellsfilter-rowfilter.html
    Properties:
        - Name: AllRowsWildcard
        - Name: FilterExpression
    
    """
    
    AllRowsWildcard_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datacellsfilter-rowfilter.html#cfn-lakeformation-datacellsfilter-rowfilter-allrowswildcard""", alias="AllRowsWildcard")
    FilterExpression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datacellsfilter-rowfilter.html#cfn-lakeformation-datacellsfilter-rowfilter-filterexpression""", alias="FilterExpression")
    


    @property
    def tropo_type(self) -> troposphere.lakeformation.RowFilter:
        from troposphere.lakeformation import RowFilter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataLakePrincipal(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-admins.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.lakeformation.Admins:
        from troposphere.lakeformation import Admins as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CreateDatabaseDefaultPermissions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-createdatabasedefaultpermissions.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.lakeformation.List:
        from troposphere.lakeformation import List as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CreateTableDefaultPermissions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-createtabledefaultpermissions.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.lakeformation.List:
        from troposphere.lakeformation import List as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataLakePrincipal(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-datalakeprincipal.html
    Properties:
        - Name: DataLakePrincipalIdentifier
    
    """
    
    DataLakePrincipalIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-datalakeprincipal.html#cfn-lakeformation-datalakesettings-datalakeprincipal-datalakeprincipalidentifier""", alias="DataLakePrincipalIdentifier")
    


    @property
    def tropo_type(self) -> troposphere.lakeformation.DataLakePrincipal:
        from troposphere.lakeformation import DataLakePrincipal as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ExternalDataFilteringAllowList(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-externaldatafilteringallowlist.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.lakeformation.List:
        from troposphere.lakeformation import List as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PrincipalPermissions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-principalpermissions.html
    Properties:
        - Name: Permissions
        - Name: Principal
    
    """
    
    Permissions_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-principalpermissions.html#cfn-lakeformation-datalakesettings-principalpermissions-permissions""", alias="Permissions")
    Principal_: 'DataLakePrincipal' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-principalpermissions.html#cfn-lakeformation-datalakesettings-principalpermissions-principal""", alias="Principal")
    


    @property
    def tropo_type(self) -> troposphere.lakeformation.PrincipalPermissions:
        from troposphere.lakeformation import PrincipalPermissions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ColumnWildcard(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-columnwildcard.html
    Properties:
        - Name: ExcludedColumnNames
    
    """
    
    ExcludedColumnNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-columnwildcard.html#cfn-lakeformation-permissions-columnwildcard-excludedcolumnnames""", alias="ExcludedColumnNames")
    


    @property
    def tropo_type(self) -> troposphere.lakeformation.ColumnWildcard:
        from troposphere.lakeformation import ColumnWildcard as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataLakePrincipal(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalakeprincipal.html
    Properties:
        - Name: DataLakePrincipalIdentifier
    
    """
    
    DataLakePrincipalIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalakeprincipal.html#cfn-lakeformation-permissions-datalakeprincipal-datalakeprincipalidentifier""", alias="DataLakePrincipalIdentifier")
    


    @property
    def tropo_type(self) -> troposphere.lakeformation.DataLakePrincipal:
        from troposphere.lakeformation import DataLakePrincipal as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataLocationResource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html
    Properties:
        - Name: S3Resource
        - Name: CatalogId
    
    """
    
    S3Resource_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html#cfn-lakeformation-permissions-datalocationresource-s3resource""", alias="S3Resource")
    CatalogId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html#cfn-lakeformation-permissions-datalocationresource-catalogid""", alias="CatalogId")
    


    @property
    def tropo_type(self) -> troposphere.lakeformation.DataLocationResource:
        from troposphere.lakeformation import DataLocationResource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DatabaseResource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-databaseresource.html
    Properties:
        - Name: CatalogId
        - Name: Name
    
    """
    
    CatalogId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-databaseresource.html#cfn-lakeformation-permissions-databaseresource-catalogid""", alias="CatalogId")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-databaseresource.html#cfn-lakeformation-permissions-databaseresource-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.lakeformation.DatabaseResource:
        from troposphere.lakeformation import DatabaseResource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TagAssociationResource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html
    Properties:
        - Name: TableResource
        - Name: DatabaseResource
        - Name: DataLocationResource
        - Name: TableWithColumnsResource
    
    """
    
    TableResource_: Optional['TableResource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-tableresource""", alias="TableResource")
    DatabaseResource_: Optional['DatabaseResource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-databaseresource""", alias="DatabaseResource")
    DataLocationResource_: Optional['DataLocationResource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-datalocationresource""", alias="DataLocationResource")
    TableWithColumnsResource_: Optional['TableWithColumnsResource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-tablewithcolumnsresource""", alias="TableWithColumnsResource")
    


    @property
    def tropo_type(self) -> troposphere.lakeformation.TagAssociationResource:
        from troposphere.lakeformation import TagAssociationResource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TableResource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html
    Properties:
        - Name: DatabaseName
        - Name: CatalogId
        - Name: TableWildcard
        - Name: Name
    
    """
    
    DatabaseName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-databasename""", alias="DatabaseName")
    CatalogId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-catalogid""", alias="CatalogId")
    TableWildcard_: Optional['TableWildcard'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-tablewildcard""", alias="TableWildcard")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.lakeformation.TableResource:
        from troposphere.lakeformation import TableResource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TableWildcard(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewildcard.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.lakeformation.TableWildcard:
        from troposphere.lakeformation import TableWildcard as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TableWithColumnsResource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html
    Properties:
        - Name: ColumnNames
        - Name: DatabaseName
        - Name: CatalogId
        - Name: Name
        - Name: ColumnWildcard
    
    """
    
    ColumnNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-columnnames""", alias="ColumnNames")
    DatabaseName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-databasename""", alias="DatabaseName")
    CatalogId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-catalogid""", alias="CatalogId")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-name""", alias="Name")
    ColumnWildcard_: Optional['ColumnWildcard'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-columnwildcard""", alias="ColumnWildcard")
    


    @property
    def tropo_type(self) -> troposphere.lakeformation.TagAssociationTableWithColumnsResource:
        from troposphere.lakeformation import TagAssociationTableWithColumnsResource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ColumnWildcard(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-columnwildcard.html
    Properties:
        - Name: ExcludedColumnNames
    
    """
    
    ExcludedColumnNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-columnwildcard.html#cfn-lakeformation-principalpermissions-columnwildcard-excludedcolumnnames""", alias="ExcludedColumnNames")
    


    @property
    def tropo_type(self) -> troposphere.lakeformation.ColumnWildcard:
        from troposphere.lakeformation import ColumnWildcard as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataCellsFilterResource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datacellsfilterresource.html
    Properties:
        - Name: TableName
        - Name: DatabaseName
        - Name: TableCatalogId
        - Name: Name
    
    """
    
    TableName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datacellsfilterresource.html#cfn-lakeformation-principalpermissions-datacellsfilterresource-tablename""", alias="TableName")
    DatabaseName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datacellsfilterresource.html#cfn-lakeformation-principalpermissions-datacellsfilterresource-databasename""", alias="DatabaseName")
    TableCatalogId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datacellsfilterresource.html#cfn-lakeformation-principalpermissions-datacellsfilterresource-tablecatalogid""", alias="TableCatalogId")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datacellsfilterresource.html#cfn-lakeformation-principalpermissions-datacellsfilterresource-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.lakeformation.DataCellsFilterResource:
        from troposphere.lakeformation import DataCellsFilterResource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataLakePrincipal(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datalakeprincipal.html
    Properties:
        - Name: DataLakePrincipalIdentifier
    
    """
    
    DataLakePrincipalIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datalakeprincipal.html#cfn-lakeformation-principalpermissions-datalakeprincipal-datalakeprincipalidentifier""", alias="DataLakePrincipalIdentifier")
    


    @property
    def tropo_type(self) -> troposphere.lakeformation.DataLakePrincipal:
        from troposphere.lakeformation import DataLakePrincipal as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataLocationResource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datalocationresource.html
    Properties:
        - Name: ResourceArn
        - Name: CatalogId
    
    """
    
    ResourceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datalocationresource.html#cfn-lakeformation-principalpermissions-datalocationresource-resourcearn""", alias="ResourceArn")
    CatalogId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datalocationresource.html#cfn-lakeformation-principalpermissions-datalocationresource-catalogid""", alias="CatalogId")
    


    @property
    def tropo_type(self) -> troposphere.lakeformation.DataLocationResource:
        from troposphere.lakeformation import DataLocationResource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DatabaseResource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-databaseresource.html
    Properties:
        - Name: CatalogId
        - Name: Name
    
    """
    
    CatalogId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-databaseresource.html#cfn-lakeformation-principalpermissions-databaseresource-catalogid""", alias="CatalogId")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-databaseresource.html#cfn-lakeformation-principalpermissions-databaseresource-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.lakeformation.DatabaseResource:
        from troposphere.lakeformation import DatabaseResource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LFTag(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftag.html
    Properties:
        - Name: TagKey
        - Name: TagValues
    
    """
    
    TagKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftag.html#cfn-lakeformation-principalpermissions-lftag-tagkey""", alias="TagKey")
    TagValues_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftag.html#cfn-lakeformation-principalpermissions-lftag-tagvalues""", alias="TagValues")
    


    @property
    def tropo_type(self) -> troposphere.lakeformation.LFTag:
        from troposphere.lakeformation import LFTag as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LFTagKeyResource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagkeyresource.html
    Properties:
        - Name: TagKey
        - Name: CatalogId
        - Name: TagValues
    
    """
    
    TagKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagkeyresource.html#cfn-lakeformation-principalpermissions-lftagkeyresource-tagkey""", alias="TagKey")
    CatalogId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagkeyresource.html#cfn-lakeformation-principalpermissions-lftagkeyresource-catalogid""", alias="CatalogId")
    TagValues_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagkeyresource.html#cfn-lakeformation-principalpermissions-lftagkeyresource-tagvalues""", alias="TagValues")
    


    @property
    def tropo_type(self) -> troposphere.lakeformation.LFTagKeyResource:
        from troposphere.lakeformation import LFTagKeyResource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LFTagPolicyResource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagpolicyresource.html
    Properties:
        - Name: Expression
        - Name: ResourceType
        - Name: CatalogId
    
    """
    
    Expression_: List['LFTag'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagpolicyresource.html#cfn-lakeformation-principalpermissions-lftagpolicyresource-expression""", alias="Expression")
    ResourceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagpolicyresource.html#cfn-lakeformation-principalpermissions-lftagpolicyresource-resourcetype""", alias="ResourceType")
    CatalogId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagpolicyresource.html#cfn-lakeformation-principalpermissions-lftagpolicyresource-catalogid""", alias="CatalogId")
    


    @property
    def tropo_type(self) -> troposphere.lakeformation.LFTagPolicyResource:
        from troposphere.lakeformation import LFTagPolicyResource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TagAssociationResource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html
    Properties:
        - Name: LFTag
        - Name: Table
        - Name: DataCellsFilter
        - Name: TableWithColumns
        - Name: LFTagPolicy
        - Name: Database
        - Name: DataLocation
        - Name: Catalog
    
    """
    
    LFTag_: Optional['LFTagKeyResource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html#cfn-lakeformation-principalpermissions-resource-lftag""", alias="LFTag")
    Table_: Optional['TableResource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html#cfn-lakeformation-principalpermissions-resource-table""", alias="Table")
    DataCellsFilter_: Optional['DataCellsFilterResource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html#cfn-lakeformation-principalpermissions-resource-datacellsfilter""", alias="DataCellsFilter")
    TableWithColumns_: Optional['TableWithColumnsResource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html#cfn-lakeformation-principalpermissions-resource-tablewithcolumns""", alias="TableWithColumns")
    LFTagPolicy_: Optional['LFTagPolicyResource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html#cfn-lakeformation-principalpermissions-resource-lftagpolicy""", alias="LFTagPolicy")
    Database_: Optional['DatabaseResource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html#cfn-lakeformation-principalpermissions-resource-database""", alias="Database")
    DataLocation_: Optional['DataLocationResource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html#cfn-lakeformation-principalpermissions-resource-datalocation""", alias="DataLocation")
    Catalog_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html#cfn-lakeformation-principalpermissions-resource-catalog""", alias="Catalog")
    


    @property
    def tropo_type(self) -> troposphere.lakeformation.TagAssociationResource:
        from troposphere.lakeformation import TagAssociationResource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TableResource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tableresource.html
    Properties:
        - Name: DatabaseName
        - Name: CatalogId
        - Name: TableWildcard
        - Name: Name
    
    """
    
    DatabaseName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tableresource.html#cfn-lakeformation-principalpermissions-tableresource-databasename""", alias="DatabaseName")
    CatalogId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tableresource.html#cfn-lakeformation-principalpermissions-tableresource-catalogid""", alias="CatalogId")
    TableWildcard_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tableresource.html#cfn-lakeformation-principalpermissions-tableresource-tablewildcard""", alias="TableWildcard")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tableresource.html#cfn-lakeformation-principalpermissions-tableresource-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.lakeformation.TableResource:
        from troposphere.lakeformation import TableResource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TableWithColumnsResource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource.html
    Properties:
        - Name: ColumnNames
        - Name: DatabaseName
        - Name: CatalogId
        - Name: Name
        - Name: ColumnWildcard
    
    """
    
    ColumnNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource.html#cfn-lakeformation-principalpermissions-tablewithcolumnsresource-columnnames""", alias="ColumnNames")
    DatabaseName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource.html#cfn-lakeformation-principalpermissions-tablewithcolumnsresource-databasename""", alias="DatabaseName")
    CatalogId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource.html#cfn-lakeformation-principalpermissions-tablewithcolumnsresource-catalogid""", alias="CatalogId")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource.html#cfn-lakeformation-principalpermissions-tablewithcolumnsresource-name""", alias="Name")
    ColumnWildcard_: Optional['ColumnWildcard'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource.html#cfn-lakeformation-principalpermissions-tablewithcolumnsresource-columnwildcard""", alias="ColumnWildcard")
    


    @property
    def tropo_type(self) -> troposphere.lakeformation.TagAssociationTableWithColumnsResource:
        from troposphere.lakeformation import TagAssociationTableWithColumnsResource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DatabaseResource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-databaseresource.html
    Properties:
        - Name: CatalogId
        - Name: Name
    
    """
    
    CatalogId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-databaseresource.html#cfn-lakeformation-tagassociation-databaseresource-catalogid""", alias="CatalogId")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-databaseresource.html#cfn-lakeformation-tagassociation-databaseresource-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.lakeformation.DatabaseResource:
        from troposphere.lakeformation import DatabaseResource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LFTagPair(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-lftagpair.html
    Properties:
        - Name: TagKey
        - Name: CatalogId
        - Name: TagValues
    
    """
    
    TagKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-lftagpair.html#cfn-lakeformation-tagassociation-lftagpair-tagkey""", alias="TagKey")
    CatalogId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-lftagpair.html#cfn-lakeformation-tagassociation-lftagpair-catalogid""", alias="CatalogId")
    TagValues_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-lftagpair.html#cfn-lakeformation-tagassociation-lftagpair-tagvalues""", alias="TagValues")
    


    @property
    def tropo_type(self) -> troposphere.lakeformation.LFTagPair:
        from troposphere.lakeformation import LFTagPair as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TagAssociationResource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-resource.html
    Properties:
        - Name: Table
        - Name: TableWithColumns
        - Name: Database
        - Name: Catalog
    
    """
    
    Table_: Optional['TableResource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-resource.html#cfn-lakeformation-tagassociation-resource-table""", alias="Table")
    TableWithColumns_: Optional['TableWithColumnsResource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-resource.html#cfn-lakeformation-tagassociation-resource-tablewithcolumns""", alias="TableWithColumns")
    Database_: Optional['DatabaseResource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-resource.html#cfn-lakeformation-tagassociation-resource-database""", alias="Database")
    Catalog_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-resource.html#cfn-lakeformation-tagassociation-resource-catalog""", alias="Catalog")
    


    @property
    def tropo_type(self) -> troposphere.lakeformation.TagAssociationResource:
        from troposphere.lakeformation import TagAssociationResource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TableResource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tableresource.html
    Properties:
        - Name: DatabaseName
        - Name: CatalogId
        - Name: TableWildcard
        - Name: Name
    
    """
    
    DatabaseName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tableresource.html#cfn-lakeformation-tagassociation-tableresource-databasename""", alias="DatabaseName")
    CatalogId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tableresource.html#cfn-lakeformation-tagassociation-tableresource-catalogid""", alias="CatalogId")
    TableWildcard_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tableresource.html#cfn-lakeformation-tagassociation-tableresource-tablewildcard""", alias="TableWildcard")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tableresource.html#cfn-lakeformation-tagassociation-tableresource-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.lakeformation.TableResource:
        from troposphere.lakeformation import TableResource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TableWithColumnsResource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tablewithcolumnsresource.html
    Properties:
        - Name: ColumnNames
        - Name: DatabaseName
        - Name: CatalogId
        - Name: Name
    
    """
    
    ColumnNames_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tablewithcolumnsresource.html#cfn-lakeformation-tagassociation-tablewithcolumnsresource-columnnames""", alias="ColumnNames")
    DatabaseName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tablewithcolumnsresource.html#cfn-lakeformation-tagassociation-tablewithcolumnsresource-databasename""", alias="DatabaseName")
    CatalogId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tablewithcolumnsresource.html#cfn-lakeformation-tagassociation-tablewithcolumnsresource-catalogid""", alias="CatalogId")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tablewithcolumnsresource.html#cfn-lakeformation-tagassociation-tablewithcolumnsresource-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.lakeformation.TagAssociationTableWithColumnsResource:
        from troposphere.lakeformation import TagAssociationTableWithColumnsResource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class DataCellsFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html
    Properties:
        - Name: TableName
        - Name: ColumnNames
        - Name: RowFilter
        - Name: DatabaseName
        - Name: TableCatalogId
        - Name: Name
        - Name: ColumnWildcard
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TableName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-tablename""", alias="TableName")
    ColumnNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-columnnames""", alias="ColumnNames")
    RowFilter_: Optional['RowFilter'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-rowfilter""", alias="RowFilter")
    DatabaseName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-databasename""", alias="DatabaseName")
    TableCatalogId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-tablecatalogid""", alias="TableCatalogId")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-name""", alias="Name")
    ColumnWildcard_: Optional['ColumnWildcard'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-columnwildcard""", alias="ColumnWildcard")
    

    @property
    def tropo_type(self) -> troposphere.lakeformation.DataCellsFilter:
        from troposphere.lakeformation import DataCellsFilter as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.lakeformation import DataCellsFilter as TropoT
        return resource_to_troposphere(self, TropoT)


class DataLakeSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html
    Properties:
        - Name: AllowExternalDataFiltering
        - Name: ExternalDataFilteringAllowList
        - Name: CreateTableDefaultPermissions
        - Name: MutationType
        - Name: Parameters
        - Name: AllowFullTableExternalDataAccess
        - Name: Admins
        - Name: CreateDatabaseDefaultPermissions
        - Name: AuthorizedSessionTagValueList
        - Name: TrustedResourceOwners
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AllowExternalDataFiltering_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-allowexternaldatafiltering""", alias="AllowExternalDataFiltering")
    ExternalDataFilteringAllowList_: Optional['List'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-externaldatafilteringallowlist""", alias="ExternalDataFilteringAllowList")
    CreateTableDefaultPermissions_: Optional['List'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-createtabledefaultpermissions""", alias="CreateTableDefaultPermissions")
    MutationType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-mutationtype""", alias="MutationType")
    Parameters_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-parameters""", alias="Parameters")
    AllowFullTableExternalDataAccess_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-allowfulltableexternaldataaccess""", alias="AllowFullTableExternalDataAccess")
    Admins_: Optional[List['DataLakePrincipal']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-admins""", alias="Admins")
    CreateDatabaseDefaultPermissions_: Optional['List'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-createdatabasedefaultpermissions""", alias="CreateDatabaseDefaultPermissions")
    AuthorizedSessionTagValueList_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-authorizedsessiontagvaluelist""", alias="AuthorizedSessionTagValueList")
    TrustedResourceOwners_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-trustedresourceowners""", alias="TrustedResourceOwners")
    

    @property
    def tropo_type(self) -> troposphere.lakeformation.DataLakeSettings:
        from troposphere.lakeformation import DataLakeSettings as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.lakeformation import DataLakeSettings as TropoT
        return resource_to_troposphere(self, TropoT)


class Permissions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html
    Properties:
        - Name: DataLakePrincipal
        - Name: Resource
        - Name: Permissions
        - Name: PermissionsWithGrantOption
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DataLakePrincipal_: 'DataLakePrincipal' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-datalakeprincipal""", alias="DataLakePrincipal")
    Resource_: 'TagAssociationResource' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-resource""", alias="Resource")
    Permissions_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-permissions""", alias="Permissions")
    PermissionsWithGrantOption_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-permissionswithgrantoption""", alias="PermissionsWithGrantOption")
    

    @property
    def tropo_type(self) -> troposphere.lakeformation.Permissions:
        from troposphere.lakeformation import Permissions as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.lakeformation import Permissions as TropoT
        return resource_to_troposphere(self, TropoT)


class PrincipalPermissions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html
    Properties:
        - Name: Resource
        - Name: Permissions
        - Name: Catalog
        - Name: Principal
        - Name: PermissionsWithGrantOption
    Attributes:
        - Name: ResourceIdentifier
        - Name: PrincipalIdentifier
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Resource_: 'TagAssociationResource' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html#cfn-lakeformation-principalpermissions-resource""", alias="Resource")
    Permissions_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html#cfn-lakeformation-principalpermissions-permissions""", alias="Permissions")
    Catalog_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html#cfn-lakeformation-principalpermissions-catalog""", alias="Catalog")
    Principal_: 'DataLakePrincipal' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html#cfn-lakeformation-principalpermissions-principal""", alias="Principal")
    PermissionsWithGrantOption_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html#cfn-lakeformation-principalpermissions-permissionswithgrantoption""", alias="PermissionsWithGrantOption")
    

    @property
    def tropo_type(self) -> troposphere.lakeformation.PrincipalPermissions:
        from troposphere.lakeformation import PrincipalPermissions as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.lakeformation import PrincipalPermissions as TropoT
        return resource_to_troposphere(self, TropoT)


class Resource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html
    Properties:
        - Name: ResourceArn
        - Name: WithFederation
        - Name: UseServiceLinkedRole
        - Name: RoleArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ResourceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-resourcearn""", alias="ResourceArn")
    WithFederation_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-withfederation""", alias="WithFederation")
    UseServiceLinkedRole_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-useservicelinkedrole""", alias="UseServiceLinkedRole")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-rolearn""", alias="RoleArn")
    

    @property
    def tropo_type(self) -> troposphere.lakeformation.Resource:
        from troposphere.lakeformation import Resource as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.lakeformation import Resource as TropoT
        return resource_to_troposphere(self, TropoT)


class Tag(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tag.html
    Properties:
        - Name: TagKey
        - Name: CatalogId
        - Name: TagValues
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TagKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tag.html#cfn-lakeformation-tag-tagkey""", alias="TagKey")
    CatalogId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tag.html#cfn-lakeformation-tag-catalogid""", alias="CatalogId")
    TagValues_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tag.html#cfn-lakeformation-tag-tagvalues""", alias="TagValues")
    

    @property
    def tropo_type(self) -> troposphere.lakeformation.Tag:
        from troposphere.lakeformation import Tag as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.lakeformation import Tag as TropoT
        return resource_to_troposphere(self, TropoT)


class TagAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tagassociation.html
    Properties:
        - Name: LFTags
        - Name: Resource
    Attributes:
        - Name: ResourceIdentifier
        - Name: TagsIdentifier
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    LFTags_: List['LFTagPair'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tagassociation.html#cfn-lakeformation-tagassociation-lftags""", alias="LFTags")
    Resource_: 'TagAssociationResource' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tagassociation.html#cfn-lakeformation-tagassociation-resource""", alias="Resource")
    

    @property
    def tropo_type(self) -> troposphere.lakeformation.TagAssociation:
        from troposphere.lakeformation import TagAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.lakeformation import TagAssociation as TropoT
        return resource_to_troposphere(self, TropoT)

