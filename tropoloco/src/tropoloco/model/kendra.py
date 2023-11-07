from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AccessControlListConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-accesscontrollistconfiguration.html
    Properties:
        - Name: KeyPath
    
    """
    
    KeyPath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-accesscontrollistconfiguration.html#cfn-kendra-datasource-accesscontrollistconfiguration-keypath""", alias="KeyPath")
    


    @property
    def tropo_type(self) -> troposphere.kendra.AccessControlListConfiguration:
        from troposphere.kendra import AccessControlListConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AclConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-aclconfiguration.html
    Properties:
        - Name: AllowedGroupsColumnName
    
    """
    
    AllowedGroupsColumnName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-aclconfiguration.html#cfn-kendra-datasource-aclconfiguration-allowedgroupscolumnname""", alias="AllowedGroupsColumnName")
    


    @property
    def tropo_type(self) -> troposphere.kendra.AclConfiguration:
        from troposphere.kendra import AclConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ColumnConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-columnconfiguration.html
    Properties:
        - Name: ChangeDetectingColumns
        - Name: DocumentTitleColumnName
        - Name: DocumentIdColumnName
        - Name: DocumentDataColumnName
        - Name: FieldMappings
    
    """
    
    ChangeDetectingColumns_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-columnconfiguration.html#cfn-kendra-datasource-columnconfiguration-changedetectingcolumns""", alias="ChangeDetectingColumns")
    DocumentTitleColumnName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-columnconfiguration.html#cfn-kendra-datasource-columnconfiguration-documenttitlecolumnname""", alias="DocumentTitleColumnName")
    DocumentIdColumnName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-columnconfiguration.html#cfn-kendra-datasource-columnconfiguration-documentidcolumnname""", alias="DocumentIdColumnName")
    DocumentDataColumnName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-columnconfiguration.html#cfn-kendra-datasource-columnconfiguration-documentdatacolumnname""", alias="DocumentDataColumnName")
    FieldMappings_: Optional[List['DataSourceToIndexFieldMapping']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-columnconfiguration.html#cfn-kendra-datasource-columnconfiguration-fieldmappings""", alias="FieldMappings")
    


    @property
    def tropo_type(self) -> troposphere.kendra.ColumnConfiguration:
        from troposphere.kendra import ColumnConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConfluenceAttachmentConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmentconfiguration.html
    Properties:
        - Name: AttachmentFieldMappings
        - Name: CrawlAttachments
    
    """
    
    AttachmentFieldMappings_: Optional[List['ConfluenceAttachmentToIndexFieldMapping']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmentconfiguration.html#cfn-kendra-datasource-confluenceattachmentconfiguration-attachmentfieldmappings""", alias="AttachmentFieldMappings")
    CrawlAttachments_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmentconfiguration.html#cfn-kendra-datasource-confluenceattachmentconfiguration-crawlattachments""", alias="CrawlAttachments")
    


    @property
    def tropo_type(self) -> troposphere.kendra.ConfluenceAttachmentConfiguration:
        from troposphere.kendra import ConfluenceAttachmentConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConfluenceAttachmentToIndexFieldMapping(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmenttoindexfieldmapping.html
    Properties:
        - Name: DateFieldFormat
        - Name: IndexFieldName
        - Name: DataSourceFieldName
    
    """
    
    DateFieldFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmenttoindexfieldmapping.html#cfn-kendra-datasource-confluenceattachmenttoindexfieldmapping-datefieldformat""", alias="DateFieldFormat")
    IndexFieldName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmenttoindexfieldmapping.html#cfn-kendra-datasource-confluenceattachmenttoindexfieldmapping-indexfieldname""", alias="IndexFieldName")
    DataSourceFieldName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmenttoindexfieldmapping.html#cfn-kendra-datasource-confluenceattachmenttoindexfieldmapping-datasourcefieldname""", alias="DataSourceFieldName")
    


    @property
    def tropo_type(self) -> troposphere.kendra.ConfluenceAttachmentToIndexFieldMapping:
        from troposphere.kendra import ConfluenceAttachmentToIndexFieldMapping as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConfluenceBlogConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceblogconfiguration.html
    Properties:
        - Name: BlogFieldMappings
    
    """
    
    BlogFieldMappings_: Optional[List['ConfluenceBlogToIndexFieldMapping']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceblogconfiguration.html#cfn-kendra-datasource-confluenceblogconfiguration-blogfieldmappings""", alias="BlogFieldMappings")
    


    @property
    def tropo_type(self) -> troposphere.kendra.ConfluenceBlogConfiguration:
        from troposphere.kendra import ConfluenceBlogConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConfluenceBlogToIndexFieldMapping(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceblogtoindexfieldmapping.html
    Properties:
        - Name: DateFieldFormat
        - Name: IndexFieldName
        - Name: DataSourceFieldName
    
    """
    
    DateFieldFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceblogtoindexfieldmapping.html#cfn-kendra-datasource-confluenceblogtoindexfieldmapping-datefieldformat""", alias="DateFieldFormat")
    IndexFieldName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceblogtoindexfieldmapping.html#cfn-kendra-datasource-confluenceblogtoindexfieldmapping-indexfieldname""", alias="IndexFieldName")
    DataSourceFieldName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceblogtoindexfieldmapping.html#cfn-kendra-datasource-confluenceblogtoindexfieldmapping-datasourcefieldname""", alias="DataSourceFieldName")
    


    @property
    def tropo_type(self) -> troposphere.kendra.ConfluenceBlogToIndexFieldMapping:
        from troposphere.kendra import ConfluenceBlogToIndexFieldMapping as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConfluenceConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html
    Properties:
        - Name: SecretArn
        - Name: AttachmentConfiguration
        - Name: ServerUrl
        - Name: PageConfiguration
        - Name: BlogConfiguration
        - Name: Version
        - Name: VpcConfiguration
        - Name: InclusionPatterns
        - Name: ExclusionPatterns
        - Name: SpaceConfiguration
    
    """
    
    SecretArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html#cfn-kendra-datasource-confluenceconfiguration-secretarn""", alias="SecretArn")
    AttachmentConfiguration_: Optional['ConfluenceAttachmentConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html#cfn-kendra-datasource-confluenceconfiguration-attachmentconfiguration""", alias="AttachmentConfiguration")
    ServerUrl_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html#cfn-kendra-datasource-confluenceconfiguration-serverurl""", alias="ServerUrl")
    PageConfiguration_: Optional['ConfluencePageConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html#cfn-kendra-datasource-confluenceconfiguration-pageconfiguration""", alias="PageConfiguration")
    BlogConfiguration_: Optional['ConfluenceBlogConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html#cfn-kendra-datasource-confluenceconfiguration-blogconfiguration""", alias="BlogConfiguration")
    Version_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html#cfn-kendra-datasource-confluenceconfiguration-version""", alias="Version")
    VpcConfiguration_: Optional['DataSourceVpcConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html#cfn-kendra-datasource-confluenceconfiguration-vpcconfiguration""", alias="VpcConfiguration")
    InclusionPatterns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html#cfn-kendra-datasource-confluenceconfiguration-inclusionpatterns""", alias="InclusionPatterns")
    ExclusionPatterns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html#cfn-kendra-datasource-confluenceconfiguration-exclusionpatterns""", alias="ExclusionPatterns")
    SpaceConfiguration_: Optional['ConfluenceSpaceConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html#cfn-kendra-datasource-confluenceconfiguration-spaceconfiguration""", alias="SpaceConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.kendra.ConfluenceConfiguration:
        from troposphere.kendra import ConfluenceConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConfluencePageConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencepageconfiguration.html
    Properties:
        - Name: PageFieldMappings
    
    """
    
    PageFieldMappings_: Optional[List['ConfluencePageToIndexFieldMapping']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencepageconfiguration.html#cfn-kendra-datasource-confluencepageconfiguration-pagefieldmappings""", alias="PageFieldMappings")
    


    @property
    def tropo_type(self) -> troposphere.kendra.ConfluencePageConfiguration:
        from troposphere.kendra import ConfluencePageConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConfluencePageToIndexFieldMapping(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencepagetoindexfieldmapping.html
    Properties:
        - Name: DateFieldFormat
        - Name: IndexFieldName
        - Name: DataSourceFieldName
    
    """
    
    DateFieldFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencepagetoindexfieldmapping.html#cfn-kendra-datasource-confluencepagetoindexfieldmapping-datefieldformat""", alias="DateFieldFormat")
    IndexFieldName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencepagetoindexfieldmapping.html#cfn-kendra-datasource-confluencepagetoindexfieldmapping-indexfieldname""", alias="IndexFieldName")
    DataSourceFieldName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencepagetoindexfieldmapping.html#cfn-kendra-datasource-confluencepagetoindexfieldmapping-datasourcefieldname""", alias="DataSourceFieldName")
    


    @property
    def tropo_type(self) -> troposphere.kendra.ConfluencePageToIndexFieldMapping:
        from troposphere.kendra import ConfluencePageToIndexFieldMapping as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConfluenceSpaceConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespaceconfiguration.html
    Properties:
        - Name: ExcludeSpaces
        - Name: SpaceFieldMappings
        - Name: CrawlPersonalSpaces
        - Name: CrawlArchivedSpaces
        - Name: IncludeSpaces
    
    """
    
    ExcludeSpaces_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespaceconfiguration.html#cfn-kendra-datasource-confluencespaceconfiguration-excludespaces""", alias="ExcludeSpaces")
    SpaceFieldMappings_: Optional[List['ConfluenceSpaceToIndexFieldMapping']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespaceconfiguration.html#cfn-kendra-datasource-confluencespaceconfiguration-spacefieldmappings""", alias="SpaceFieldMappings")
    CrawlPersonalSpaces_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespaceconfiguration.html#cfn-kendra-datasource-confluencespaceconfiguration-crawlpersonalspaces""", alias="CrawlPersonalSpaces")
    CrawlArchivedSpaces_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespaceconfiguration.html#cfn-kendra-datasource-confluencespaceconfiguration-crawlarchivedspaces""", alias="CrawlArchivedSpaces")
    IncludeSpaces_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespaceconfiguration.html#cfn-kendra-datasource-confluencespaceconfiguration-includespaces""", alias="IncludeSpaces")
    


    @property
    def tropo_type(self) -> troposphere.kendra.ConfluenceSpaceConfiguration:
        from troposphere.kendra import ConfluenceSpaceConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConfluenceSpaceToIndexFieldMapping(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespacetoindexfieldmapping.html
    Properties:
        - Name: DateFieldFormat
        - Name: IndexFieldName
        - Name: DataSourceFieldName
    
    """
    
    DateFieldFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespacetoindexfieldmapping.html#cfn-kendra-datasource-confluencespacetoindexfieldmapping-datefieldformat""", alias="DateFieldFormat")
    IndexFieldName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespacetoindexfieldmapping.html#cfn-kendra-datasource-confluencespacetoindexfieldmapping-indexfieldname""", alias="IndexFieldName")
    DataSourceFieldName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespacetoindexfieldmapping.html#cfn-kendra-datasource-confluencespacetoindexfieldmapping-datasourcefieldname""", alias="DataSourceFieldName")
    


    @property
    def tropo_type(self) -> troposphere.kendra.ConfluenceSpaceToIndexFieldMapping:
        from troposphere.kendra import ConfluenceSpaceToIndexFieldMapping as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConnectionConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-connectionconfiguration.html
    Properties:
        - Name: SecretArn
        - Name: TableName
        - Name: DatabasePort
        - Name: DatabaseHost
        - Name: DatabaseName
    
    """
    
    SecretArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-connectionconfiguration.html#cfn-kendra-datasource-connectionconfiguration-secretarn""", alias="SecretArn")
    TableName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-connectionconfiguration.html#cfn-kendra-datasource-connectionconfiguration-tablename""", alias="TableName")
    DatabasePort_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-connectionconfiguration.html#cfn-kendra-datasource-connectionconfiguration-databaseport""", alias="DatabasePort")
    DatabaseHost_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-connectionconfiguration.html#cfn-kendra-datasource-connectionconfiguration-databasehost""", alias="DatabaseHost")
    DatabaseName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-connectionconfiguration.html#cfn-kendra-datasource-connectionconfiguration-databasename""", alias="DatabaseName")
    


    @property
    def tropo_type(self) -> troposphere.kendra.ConnectionConfiguration:
        from troposphere.kendra import ConnectionConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomDocumentEnrichmentConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-customdocumentenrichmentconfiguration.html
    Properties:
        - Name: InlineConfigurations
        - Name: PreExtractionHookConfiguration
        - Name: PostExtractionHookConfiguration
        - Name: RoleArn
    
    """
    
    InlineConfigurations_: Optional[List['InlineCustomDocumentEnrichmentConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-customdocumentenrichmentconfiguration.html#cfn-kendra-datasource-customdocumentenrichmentconfiguration-inlineconfigurations""", alias="InlineConfigurations")
    PreExtractionHookConfiguration_: Optional['HookConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-customdocumentenrichmentconfiguration.html#cfn-kendra-datasource-customdocumentenrichmentconfiguration-preextractionhookconfiguration""", alias="PreExtractionHookConfiguration")
    PostExtractionHookConfiguration_: Optional['HookConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-customdocumentenrichmentconfiguration.html#cfn-kendra-datasource-customdocumentenrichmentconfiguration-postextractionhookconfiguration""", alias="PostExtractionHookConfiguration")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-customdocumentenrichmentconfiguration.html#cfn-kendra-datasource-customdocumentenrichmentconfiguration-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.kendra.CustomDocumentEnrichmentConfiguration:
        from troposphere.kendra import CustomDocumentEnrichmentConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataSourceConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html
    Properties:
        - Name: GoogleDriveConfiguration
        - Name: WebCrawlerConfiguration
        - Name: S3Configuration
        - Name: SalesforceConfiguration
        - Name: DatabaseConfiguration
        - Name: SharePointConfiguration
        - Name: ConfluenceConfiguration
        - Name: WorkDocsConfiguration
        - Name: OneDriveConfiguration
        - Name: ServiceNowConfiguration
    
    """
    
    GoogleDriveConfiguration_: Optional['GoogleDriveConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html#cfn-kendra-datasource-datasourceconfiguration-googledriveconfiguration""", alias="GoogleDriveConfiguration")
    WebCrawlerConfiguration_: Optional['WebCrawlerConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html#cfn-kendra-datasource-datasourceconfiguration-webcrawlerconfiguration""", alias="WebCrawlerConfiguration")
    S3Configuration_: Optional['S3DataSourceConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html#cfn-kendra-datasource-datasourceconfiguration-s3configuration""", alias="S3Configuration")
    SalesforceConfiguration_: Optional['SalesforceConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html#cfn-kendra-datasource-datasourceconfiguration-salesforceconfiguration""", alias="SalesforceConfiguration")
    DatabaseConfiguration_: Optional['DatabaseConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html#cfn-kendra-datasource-datasourceconfiguration-databaseconfiguration""", alias="DatabaseConfiguration")
    SharePointConfiguration_: Optional['SharePointConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html#cfn-kendra-datasource-datasourceconfiguration-sharepointconfiguration""", alias="SharePointConfiguration")
    ConfluenceConfiguration_: Optional['ConfluenceConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html#cfn-kendra-datasource-datasourceconfiguration-confluenceconfiguration""", alias="ConfluenceConfiguration")
    WorkDocsConfiguration_: Optional['WorkDocsConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html#cfn-kendra-datasource-datasourceconfiguration-workdocsconfiguration""", alias="WorkDocsConfiguration")
    OneDriveConfiguration_: Optional['OneDriveConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html#cfn-kendra-datasource-datasourceconfiguration-onedriveconfiguration""", alias="OneDriveConfiguration")
    ServiceNowConfiguration_: Optional['ServiceNowConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html#cfn-kendra-datasource-datasourceconfiguration-servicenowconfiguration""", alias="ServiceNowConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.kendra.DataSourceConfiguration:
        from troposphere.kendra import DataSourceConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataSourceToIndexFieldMapping(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcetoindexfieldmapping.html
    Properties:
        - Name: DateFieldFormat
        - Name: IndexFieldName
        - Name: DataSourceFieldName
    
    """
    
    DateFieldFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcetoindexfieldmapping.html#cfn-kendra-datasource-datasourcetoindexfieldmapping-datefieldformat""", alias="DateFieldFormat")
    IndexFieldName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcetoindexfieldmapping.html#cfn-kendra-datasource-datasourcetoindexfieldmapping-indexfieldname""", alias="IndexFieldName")
    DataSourceFieldName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcetoindexfieldmapping.html#cfn-kendra-datasource-datasourcetoindexfieldmapping-datasourcefieldname""", alias="DataSourceFieldName")
    


    @property
    def tropo_type(self) -> troposphere.kendra.DataSourceToIndexFieldMapping:
        from troposphere.kendra import DataSourceToIndexFieldMapping as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataSourceVpcConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcevpcconfiguration.html
    Properties:
        - Name: SubnetIds
        - Name: SecurityGroupIds
    
    """
    
    SubnetIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcevpcconfiguration.html#cfn-kendra-datasource-datasourcevpcconfiguration-subnetids""", alias="SubnetIds")
    SecurityGroupIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcevpcconfiguration.html#cfn-kendra-datasource-datasourcevpcconfiguration-securitygroupids""", alias="SecurityGroupIds")
    


    @property
    def tropo_type(self) -> troposphere.kendra.DataSourceVpcConfiguration:
        from troposphere.kendra import DataSourceVpcConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DatabaseConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-databaseconfiguration.html
    Properties:
        - Name: SqlConfiguration
        - Name: DatabaseEngineType
        - Name: ConnectionConfiguration
        - Name: ColumnConfiguration
        - Name: VpcConfiguration
        - Name: AclConfiguration
    
    """
    
    SqlConfiguration_: Optional['SqlConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-databaseconfiguration.html#cfn-kendra-datasource-databaseconfiguration-sqlconfiguration""", alias="SqlConfiguration")
    DatabaseEngineType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-databaseconfiguration.html#cfn-kendra-datasource-databaseconfiguration-databaseenginetype""", alias="DatabaseEngineType")
    ConnectionConfiguration_: 'ConnectionConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-databaseconfiguration.html#cfn-kendra-datasource-databaseconfiguration-connectionconfiguration""", alias="ConnectionConfiguration")
    ColumnConfiguration_: 'ColumnConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-databaseconfiguration.html#cfn-kendra-datasource-databaseconfiguration-columnconfiguration""", alias="ColumnConfiguration")
    VpcConfiguration_: Optional['DataSourceVpcConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-databaseconfiguration.html#cfn-kendra-datasource-databaseconfiguration-vpcconfiguration""", alias="VpcConfiguration")
    AclConfiguration_: Optional['AclConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-databaseconfiguration.html#cfn-kendra-datasource-databaseconfiguration-aclconfiguration""", alias="AclConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.kendra.DatabaseConfiguration:
        from troposphere.kendra import DatabaseConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DocumentAttributeCondition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentattributecondition.html
    Properties:
        - Name: Operator
        - Name: ConditionDocumentAttributeKey
        - Name: ConditionOnValue
    
    """
    
    Operator_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentattributecondition.html#cfn-kendra-datasource-documentattributecondition-operator""", alias="Operator")
    ConditionDocumentAttributeKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentattributecondition.html#cfn-kendra-datasource-documentattributecondition-conditiondocumentattributekey""", alias="ConditionDocumentAttributeKey")
    ConditionOnValue_: Optional['DocumentAttributeValue'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentattributecondition.html#cfn-kendra-datasource-documentattributecondition-conditiononvalue""", alias="ConditionOnValue")
    


    @property
    def tropo_type(self) -> troposphere.kendra.DocumentAttributeCondition:
        from troposphere.kendra import DocumentAttributeCondition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DocumentAttributeTarget(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentattributetarget.html
    Properties:
        - Name: TargetDocumentAttributeKey
        - Name: TargetDocumentAttributeValueDeletion
        - Name: TargetDocumentAttributeValue
    
    """
    
    TargetDocumentAttributeKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentattributetarget.html#cfn-kendra-datasource-documentattributetarget-targetdocumentattributekey""", alias="TargetDocumentAttributeKey")
    TargetDocumentAttributeValueDeletion_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentattributetarget.html#cfn-kendra-datasource-documentattributetarget-targetdocumentattributevaluedeletion""", alias="TargetDocumentAttributeValueDeletion")
    TargetDocumentAttributeValue_: Optional['DocumentAttributeValue'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentattributetarget.html#cfn-kendra-datasource-documentattributetarget-targetdocumentattributevalue""", alias="TargetDocumentAttributeValue")
    


    @property
    def tropo_type(self) -> troposphere.kendra.DocumentAttributeTarget:
        from troposphere.kendra import DocumentAttributeTarget as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DocumentAttributeValue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentattributevalue.html
    Properties:
        - Name: DateValue
        - Name: LongValue
        - Name: StringValue
        - Name: StringListValue
    
    """
    
    DateValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentattributevalue.html#cfn-kendra-datasource-documentattributevalue-datevalue""", alias="DateValue")
    LongValue_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentattributevalue.html#cfn-kendra-datasource-documentattributevalue-longvalue""", alias="LongValue")
    StringValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentattributevalue.html#cfn-kendra-datasource-documentattributevalue-stringvalue""", alias="StringValue")
    StringListValue_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentattributevalue.html#cfn-kendra-datasource-documentattributevalue-stringlistvalue""", alias="StringListValue")
    


    @property
    def tropo_type(self) -> troposphere.kendra.DocumentAttributeValue:
        from troposphere.kendra import DocumentAttributeValue as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DocumentsMetadataConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentsmetadataconfiguration.html
    Properties:
        - Name: S3Prefix
    
    """
    
    S3Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentsmetadataconfiguration.html#cfn-kendra-datasource-documentsmetadataconfiguration-s3prefix""", alias="S3Prefix")
    


    @property
    def tropo_type(self) -> troposphere.kendra.DocumentsMetadataConfiguration:
        from troposphere.kendra import DocumentsMetadataConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GoogleDriveConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-googledriveconfiguration.html
    Properties:
        - Name: SecretArn
        - Name: ExcludeSharedDrives
        - Name: ExcludeUserAccounts
        - Name: InclusionPatterns
        - Name: ExcludeMimeTypes
        - Name: FieldMappings
        - Name: ExclusionPatterns
    
    """
    
    SecretArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-googledriveconfiguration.html#cfn-kendra-datasource-googledriveconfiguration-secretarn""", alias="SecretArn")
    ExcludeSharedDrives_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-googledriveconfiguration.html#cfn-kendra-datasource-googledriveconfiguration-excludeshareddrives""", alias="ExcludeSharedDrives")
    ExcludeUserAccounts_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-googledriveconfiguration.html#cfn-kendra-datasource-googledriveconfiguration-excludeuseraccounts""", alias="ExcludeUserAccounts")
    InclusionPatterns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-googledriveconfiguration.html#cfn-kendra-datasource-googledriveconfiguration-inclusionpatterns""", alias="InclusionPatterns")
    ExcludeMimeTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-googledriveconfiguration.html#cfn-kendra-datasource-googledriveconfiguration-excludemimetypes""", alias="ExcludeMimeTypes")
    FieldMappings_: Optional[List['DataSourceToIndexFieldMapping']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-googledriveconfiguration.html#cfn-kendra-datasource-googledriveconfiguration-fieldmappings""", alias="FieldMappings")
    ExclusionPatterns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-googledriveconfiguration.html#cfn-kendra-datasource-googledriveconfiguration-exclusionpatterns""", alias="ExclusionPatterns")
    


    @property
    def tropo_type(self) -> troposphere.kendra.GoogleDriveConfiguration:
        from troposphere.kendra import GoogleDriveConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HookConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-hookconfiguration.html
    Properties:
        - Name: S3Bucket
        - Name: LambdaArn
        - Name: InvocationCondition
    
    """
    
    S3Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-hookconfiguration.html#cfn-kendra-datasource-hookconfiguration-s3bucket""", alias="S3Bucket")
    LambdaArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-hookconfiguration.html#cfn-kendra-datasource-hookconfiguration-lambdaarn""", alias="LambdaArn")
    InvocationCondition_: Optional['DocumentAttributeCondition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-hookconfiguration.html#cfn-kendra-datasource-hookconfiguration-invocationcondition""", alias="InvocationCondition")
    


    @property
    def tropo_type(self) -> troposphere.kendra.HookConfiguration:
        from troposphere.kendra import HookConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InlineCustomDocumentEnrichmentConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-inlinecustomdocumentenrichmentconfiguration.html
    Properties:
        - Name: Condition
        - Name: Target
        - Name: DocumentContentDeletion
    
    """
    
    Condition_: Optional['DocumentAttributeCondition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-inlinecustomdocumentenrichmentconfiguration.html#cfn-kendra-datasource-inlinecustomdocumentenrichmentconfiguration-condition""", alias="Condition")
    Target_: Optional['DocumentAttributeTarget'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-inlinecustomdocumentenrichmentconfiguration.html#cfn-kendra-datasource-inlinecustomdocumentenrichmentconfiguration-target""", alias="Target")
    DocumentContentDeletion_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-inlinecustomdocumentenrichmentconfiguration.html#cfn-kendra-datasource-inlinecustomdocumentenrichmentconfiguration-documentcontentdeletion""", alias="DocumentContentDeletion")
    


    @property
    def tropo_type(self) -> troposphere.kendra.InlineCustomDocumentEnrichmentConfiguration:
        from troposphere.kendra import InlineCustomDocumentEnrichmentConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OneDriveConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveconfiguration.html
    Properties:
        - Name: TenantDomain
        - Name: SecretArn
        - Name: DisableLocalGroups
        - Name: OneDriveUsers
        - Name: InclusionPatterns
        - Name: FieldMappings
        - Name: ExclusionPatterns
    
    """
    
    TenantDomain_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveconfiguration.html#cfn-kendra-datasource-onedriveconfiguration-tenantdomain""", alias="TenantDomain")
    SecretArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveconfiguration.html#cfn-kendra-datasource-onedriveconfiguration-secretarn""", alias="SecretArn")
    DisableLocalGroups_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveconfiguration.html#cfn-kendra-datasource-onedriveconfiguration-disablelocalgroups""", alias="DisableLocalGroups")
    OneDriveUsers_: 'OneDriveUsers' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveconfiguration.html#cfn-kendra-datasource-onedriveconfiguration-onedriveusers""", alias="OneDriveUsers")
    InclusionPatterns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveconfiguration.html#cfn-kendra-datasource-onedriveconfiguration-inclusionpatterns""", alias="InclusionPatterns")
    FieldMappings_: Optional[List['DataSourceToIndexFieldMapping']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveconfiguration.html#cfn-kendra-datasource-onedriveconfiguration-fieldmappings""", alias="FieldMappings")
    ExclusionPatterns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveconfiguration.html#cfn-kendra-datasource-onedriveconfiguration-exclusionpatterns""", alias="ExclusionPatterns")
    


    @property
    def tropo_type(self) -> troposphere.kendra.OneDriveConfiguration:
        from troposphere.kendra import OneDriveConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OneDriveUsers(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveusers.html
    Properties:
        - Name: OneDriveUserList
        - Name: OneDriveUserS3Path
    
    """
    
    OneDriveUserList_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveusers.html#cfn-kendra-datasource-onedriveusers-onedriveuserlist""", alias="OneDriveUserList")
    OneDriveUserS3Path_: Optional['S3Path'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveusers.html#cfn-kendra-datasource-onedriveusers-onedriveusers3path""", alias="OneDriveUserS3Path")
    


    @property
    def tropo_type(self) -> troposphere.kendra.OneDriveUsers:
        from troposphere.kendra import OneDriveUsers as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProxyConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-proxyconfiguration.html
    Properties:
        - Name: Port
        - Name: Host
        - Name: Credentials
    
    """
    
    Port_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-proxyconfiguration.html#cfn-kendra-datasource-proxyconfiguration-port""", alias="Port")
    Host_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-proxyconfiguration.html#cfn-kendra-datasource-proxyconfiguration-host""", alias="Host")
    Credentials_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-proxyconfiguration.html#cfn-kendra-datasource-proxyconfiguration-credentials""", alias="Credentials")
    


    @property
    def tropo_type(self) -> troposphere.kendra.ProxyConfiguration:
        from troposphere.kendra import ProxyConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3DataSourceConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3datasourceconfiguration.html
    Properties:
        - Name: BucketName
        - Name: InclusionPatterns
        - Name: InclusionPrefixes
        - Name: AccessControlListConfiguration
        - Name: ExclusionPatterns
        - Name: DocumentsMetadataConfiguration
    
    """
    
    BucketName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3datasourceconfiguration.html#cfn-kendra-datasource-s3datasourceconfiguration-bucketname""", alias="BucketName")
    InclusionPatterns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3datasourceconfiguration.html#cfn-kendra-datasource-s3datasourceconfiguration-inclusionpatterns""", alias="InclusionPatterns")
    InclusionPrefixes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3datasourceconfiguration.html#cfn-kendra-datasource-s3datasourceconfiguration-inclusionprefixes""", alias="InclusionPrefixes")
    AccessControlListConfiguration_: Optional['AccessControlListConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3datasourceconfiguration.html#cfn-kendra-datasource-s3datasourceconfiguration-accesscontrollistconfiguration""", alias="AccessControlListConfiguration")
    ExclusionPatterns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3datasourceconfiguration.html#cfn-kendra-datasource-s3datasourceconfiguration-exclusionpatterns""", alias="ExclusionPatterns")
    DocumentsMetadataConfiguration_: Optional['DocumentsMetadataConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3datasourceconfiguration.html#cfn-kendra-datasource-s3datasourceconfiguration-documentsmetadataconfiguration""", alias="DocumentsMetadataConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.kendra.S3DataSourceConfiguration:
        from troposphere.kendra import S3DataSourceConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Path(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3path.html
    Properties:
        - Name: Bucket
        - Name: Key
    
    """
    
    Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3path.html#cfn-kendra-datasource-s3path-bucket""", alias="Bucket")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3path.html#cfn-kendra-datasource-s3path-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.kendra.S3Path:
        from troposphere.kendra import S3Path as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SalesforceChatterFeedConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcechatterfeedconfiguration.html
    Properties:
        - Name: DocumentTitleFieldName
        - Name: IncludeFilterTypes
        - Name: FieldMappings
        - Name: DocumentDataFieldName
    
    """
    
    DocumentTitleFieldName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcechatterfeedconfiguration.html#cfn-kendra-datasource-salesforcechatterfeedconfiguration-documenttitlefieldname""", alias="DocumentTitleFieldName")
    IncludeFilterTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcechatterfeedconfiguration.html#cfn-kendra-datasource-salesforcechatterfeedconfiguration-includefiltertypes""", alias="IncludeFilterTypes")
    FieldMappings_: Optional[List['DataSourceToIndexFieldMapping']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcechatterfeedconfiguration.html#cfn-kendra-datasource-salesforcechatterfeedconfiguration-fieldmappings""", alias="FieldMappings")
    DocumentDataFieldName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcechatterfeedconfiguration.html#cfn-kendra-datasource-salesforcechatterfeedconfiguration-documentdatafieldname""", alias="DocumentDataFieldName")
    


    @property
    def tropo_type(self) -> troposphere.kendra.SalesforceChatterFeedConfiguration:
        from troposphere.kendra import SalesforceChatterFeedConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SalesforceConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html
    Properties:
        - Name: SecretArn
        - Name: ServerUrl
        - Name: IncludeAttachmentFilePatterns
        - Name: StandardObjectConfigurations
        - Name: StandardObjectAttachmentConfiguration
        - Name: ExcludeAttachmentFilePatterns
        - Name: CrawlAttachments
        - Name: ChatterFeedConfiguration
        - Name: KnowledgeArticleConfiguration
    
    """
    
    SecretArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html#cfn-kendra-datasource-salesforceconfiguration-secretarn""", alias="SecretArn")
    ServerUrl_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html#cfn-kendra-datasource-salesforceconfiguration-serverurl""", alias="ServerUrl")
    IncludeAttachmentFilePatterns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html#cfn-kendra-datasource-salesforceconfiguration-includeattachmentfilepatterns""", alias="IncludeAttachmentFilePatterns")
    StandardObjectConfigurations_: Optional[List['SalesforceStandardObjectConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html#cfn-kendra-datasource-salesforceconfiguration-standardobjectconfigurations""", alias="StandardObjectConfigurations")
    StandardObjectAttachmentConfiguration_: Optional['SalesforceStandardObjectAttachmentConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html#cfn-kendra-datasource-salesforceconfiguration-standardobjectattachmentconfiguration""", alias="StandardObjectAttachmentConfiguration")
    ExcludeAttachmentFilePatterns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html#cfn-kendra-datasource-salesforceconfiguration-excludeattachmentfilepatterns""", alias="ExcludeAttachmentFilePatterns")
    CrawlAttachments_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html#cfn-kendra-datasource-salesforceconfiguration-crawlattachments""", alias="CrawlAttachments")
    ChatterFeedConfiguration_: Optional['SalesforceChatterFeedConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html#cfn-kendra-datasource-salesforceconfiguration-chatterfeedconfiguration""", alias="ChatterFeedConfiguration")
    KnowledgeArticleConfiguration_: Optional['SalesforceKnowledgeArticleConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html#cfn-kendra-datasource-salesforceconfiguration-knowledgearticleconfiguration""", alias="KnowledgeArticleConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.kendra.SalesforceConfiguration:
        from troposphere.kendra import SalesforceConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SalesforceCustomKnowledgeArticleTypeConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration.html
    Properties:
        - Name: DocumentTitleFieldName
        - Name: FieldMappings
        - Name: Name
        - Name: DocumentDataFieldName
    
    """
    
    DocumentTitleFieldName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration.html#cfn-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration-documenttitlefieldname""", alias="DocumentTitleFieldName")
    FieldMappings_: Optional[List['DataSourceToIndexFieldMapping']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration.html#cfn-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration-fieldmappings""", alias="FieldMappings")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration.html#cfn-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration-name""", alias="Name")
    DocumentDataFieldName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration.html#cfn-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration-documentdatafieldname""", alias="DocumentDataFieldName")
    


    @property
    def tropo_type(self) -> troposphere.kendra.SalesforceCustomKnowledgeArticleTypeConfiguration:
        from troposphere.kendra import SalesforceCustomKnowledgeArticleTypeConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SalesforceKnowledgeArticleConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceknowledgearticleconfiguration.html
    Properties:
        - Name: IncludedStates
        - Name: StandardKnowledgeArticleTypeConfiguration
        - Name: CustomKnowledgeArticleTypeConfigurations
    
    """
    
    IncludedStates_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceknowledgearticleconfiguration.html#cfn-kendra-datasource-salesforceknowledgearticleconfiguration-includedstates""", alias="IncludedStates")
    StandardKnowledgeArticleTypeConfiguration_: Optional['SalesforceStandardKnowledgeArticleTypeConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceknowledgearticleconfiguration.html#cfn-kendra-datasource-salesforceknowledgearticleconfiguration-standardknowledgearticletypeconfiguration""", alias="StandardKnowledgeArticleTypeConfiguration")
    CustomKnowledgeArticleTypeConfigurations_: Optional[List['SalesforceCustomKnowledgeArticleTypeConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceknowledgearticleconfiguration.html#cfn-kendra-datasource-salesforceknowledgearticleconfiguration-customknowledgearticletypeconfigurations""", alias="CustomKnowledgeArticleTypeConfigurations")
    


    @property
    def tropo_type(self) -> troposphere.kendra.SalesforceKnowledgeArticleConfiguration:
        from troposphere.kendra import SalesforceKnowledgeArticleConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SalesforceStandardKnowledgeArticleTypeConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration.html
    Properties:
        - Name: DocumentTitleFieldName
        - Name: FieldMappings
        - Name: DocumentDataFieldName
    
    """
    
    DocumentTitleFieldName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration.html#cfn-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration-documenttitlefieldname""", alias="DocumentTitleFieldName")
    FieldMappings_: Optional[List['DataSourceToIndexFieldMapping']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration.html#cfn-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration-fieldmappings""", alias="FieldMappings")
    DocumentDataFieldName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration.html#cfn-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration-documentdatafieldname""", alias="DocumentDataFieldName")
    


    @property
    def tropo_type(self) -> troposphere.kendra.SalesforceStandardKnowledgeArticleTypeConfiguration:
        from troposphere.kendra import SalesforceStandardKnowledgeArticleTypeConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SalesforceStandardObjectAttachmentConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectattachmentconfiguration.html
    Properties:
        - Name: DocumentTitleFieldName
        - Name: FieldMappings
    
    """
    
    DocumentTitleFieldName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectattachmentconfiguration.html#cfn-kendra-datasource-salesforcestandardobjectattachmentconfiguration-documenttitlefieldname""", alias="DocumentTitleFieldName")
    FieldMappings_: Optional[List['DataSourceToIndexFieldMapping']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectattachmentconfiguration.html#cfn-kendra-datasource-salesforcestandardobjectattachmentconfiguration-fieldmappings""", alias="FieldMappings")
    


    @property
    def tropo_type(self) -> troposphere.kendra.SalesforceStandardObjectAttachmentConfiguration:
        from troposphere.kendra import SalesforceStandardObjectAttachmentConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SalesforceStandardObjectConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectconfiguration.html
    Properties:
        - Name: DocumentTitleFieldName
        - Name: FieldMappings
        - Name: Name
        - Name: DocumentDataFieldName
    
    """
    
    DocumentTitleFieldName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectconfiguration.html#cfn-kendra-datasource-salesforcestandardobjectconfiguration-documenttitlefieldname""", alias="DocumentTitleFieldName")
    FieldMappings_: Optional[List['DataSourceToIndexFieldMapping']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectconfiguration.html#cfn-kendra-datasource-salesforcestandardobjectconfiguration-fieldmappings""", alias="FieldMappings")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectconfiguration.html#cfn-kendra-datasource-salesforcestandardobjectconfiguration-name""", alias="Name")
    DocumentDataFieldName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectconfiguration.html#cfn-kendra-datasource-salesforcestandardobjectconfiguration-documentdatafieldname""", alias="DocumentDataFieldName")
    


    @property
    def tropo_type(self) -> troposphere.kendra.SalesforceStandardObjectConfiguration:
        from troposphere.kendra import SalesforceStandardObjectConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ServiceNowConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowconfiguration.html
    Properties:
        - Name: SecretArn
        - Name: HostUrl
        - Name: ServiceCatalogConfiguration
        - Name: ServiceNowBuildVersion
        - Name: KnowledgeArticleConfiguration
        - Name: AuthenticationType
    
    """
    
    SecretArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowconfiguration.html#cfn-kendra-datasource-servicenowconfiguration-secretarn""", alias="SecretArn")
    HostUrl_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowconfiguration.html#cfn-kendra-datasource-servicenowconfiguration-hosturl""", alias="HostUrl")
    ServiceCatalogConfiguration_: Optional['ServiceNowServiceCatalogConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowconfiguration.html#cfn-kendra-datasource-servicenowconfiguration-servicecatalogconfiguration""", alias="ServiceCatalogConfiguration")
    ServiceNowBuildVersion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowconfiguration.html#cfn-kendra-datasource-servicenowconfiguration-servicenowbuildversion""", alias="ServiceNowBuildVersion")
    KnowledgeArticleConfiguration_: Optional['ServiceNowKnowledgeArticleConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowconfiguration.html#cfn-kendra-datasource-servicenowconfiguration-knowledgearticleconfiguration""", alias="KnowledgeArticleConfiguration")
    AuthenticationType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowconfiguration.html#cfn-kendra-datasource-servicenowconfiguration-authenticationtype""", alias="AuthenticationType")
    


    @property
    def tropo_type(self) -> troposphere.kendra.ServiceNowConfiguration:
        from troposphere.kendra import ServiceNowConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ServiceNowKnowledgeArticleConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowknowledgearticleconfiguration.html
    Properties:
        - Name: DocumentTitleFieldName
        - Name: IncludeAttachmentFilePatterns
        - Name: ExcludeAttachmentFilePatterns
        - Name: FilterQuery
        - Name: CrawlAttachments
        - Name: FieldMappings
        - Name: DocumentDataFieldName
    
    """
    
    DocumentTitleFieldName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowknowledgearticleconfiguration.html#cfn-kendra-datasource-servicenowknowledgearticleconfiguration-documenttitlefieldname""", alias="DocumentTitleFieldName")
    IncludeAttachmentFilePatterns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowknowledgearticleconfiguration.html#cfn-kendra-datasource-servicenowknowledgearticleconfiguration-includeattachmentfilepatterns""", alias="IncludeAttachmentFilePatterns")
    ExcludeAttachmentFilePatterns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowknowledgearticleconfiguration.html#cfn-kendra-datasource-servicenowknowledgearticleconfiguration-excludeattachmentfilepatterns""", alias="ExcludeAttachmentFilePatterns")
    FilterQuery_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowknowledgearticleconfiguration.html#cfn-kendra-datasource-servicenowknowledgearticleconfiguration-filterquery""", alias="FilterQuery")
    CrawlAttachments_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowknowledgearticleconfiguration.html#cfn-kendra-datasource-servicenowknowledgearticleconfiguration-crawlattachments""", alias="CrawlAttachments")
    FieldMappings_: Optional[List['DataSourceToIndexFieldMapping']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowknowledgearticleconfiguration.html#cfn-kendra-datasource-servicenowknowledgearticleconfiguration-fieldmappings""", alias="FieldMappings")
    DocumentDataFieldName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowknowledgearticleconfiguration.html#cfn-kendra-datasource-servicenowknowledgearticleconfiguration-documentdatafieldname""", alias="DocumentDataFieldName")
    


    @property
    def tropo_type(self) -> troposphere.kendra.ServiceNowKnowledgeArticleConfiguration:
        from troposphere.kendra import ServiceNowKnowledgeArticleConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ServiceNowServiceCatalogConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowservicecatalogconfiguration.html
    Properties:
        - Name: DocumentTitleFieldName
        - Name: IncludeAttachmentFilePatterns
        - Name: ExcludeAttachmentFilePatterns
        - Name: CrawlAttachments
        - Name: FieldMappings
        - Name: DocumentDataFieldName
    
    """
    
    DocumentTitleFieldName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowservicecatalogconfiguration.html#cfn-kendra-datasource-servicenowservicecatalogconfiguration-documenttitlefieldname""", alias="DocumentTitleFieldName")
    IncludeAttachmentFilePatterns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowservicecatalogconfiguration.html#cfn-kendra-datasource-servicenowservicecatalogconfiguration-includeattachmentfilepatterns""", alias="IncludeAttachmentFilePatterns")
    ExcludeAttachmentFilePatterns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowservicecatalogconfiguration.html#cfn-kendra-datasource-servicenowservicecatalogconfiguration-excludeattachmentfilepatterns""", alias="ExcludeAttachmentFilePatterns")
    CrawlAttachments_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowservicecatalogconfiguration.html#cfn-kendra-datasource-servicenowservicecatalogconfiguration-crawlattachments""", alias="CrawlAttachments")
    FieldMappings_: Optional[List['DataSourceToIndexFieldMapping']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowservicecatalogconfiguration.html#cfn-kendra-datasource-servicenowservicecatalogconfiguration-fieldmappings""", alias="FieldMappings")
    DocumentDataFieldName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowservicecatalogconfiguration.html#cfn-kendra-datasource-servicenowservicecatalogconfiguration-documentdatafieldname""", alias="DocumentDataFieldName")
    


    @property
    def tropo_type(self) -> troposphere.kendra.ServiceNowServiceCatalogConfiguration:
        from troposphere.kendra import ServiceNowServiceCatalogConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SharePointConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html
    Properties:
        - Name: SecretArn
        - Name: DocumentTitleFieldName
        - Name: SslCertificateS3Path
        - Name: DisableLocalGroups
        - Name: CrawlAttachments
        - Name: InclusionPatterns
        - Name: VpcConfiguration
        - Name: Urls
        - Name: UseChangeLog
        - Name: FieldMappings
        - Name: ExclusionPatterns
        - Name: SharePointVersion
    
    """
    
    SecretArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-secretarn""", alias="SecretArn")
    DocumentTitleFieldName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-documenttitlefieldname""", alias="DocumentTitleFieldName")
    SslCertificateS3Path_: Optional['S3Path'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-sslcertificates3path""", alias="SslCertificateS3Path")
    DisableLocalGroups_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-disablelocalgroups""", alias="DisableLocalGroups")
    CrawlAttachments_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-crawlattachments""", alias="CrawlAttachments")
    InclusionPatterns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-inclusionpatterns""", alias="InclusionPatterns")
    VpcConfiguration_: Optional['DataSourceVpcConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-vpcconfiguration""", alias="VpcConfiguration")
    Urls_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-urls""", alias="Urls")
    UseChangeLog_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-usechangelog""", alias="UseChangeLog")
    FieldMappings_: Optional[List['DataSourceToIndexFieldMapping']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-fieldmappings""", alias="FieldMappings")
    ExclusionPatterns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-exclusionpatterns""", alias="ExclusionPatterns")
    SharePointVersion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-sharepointversion""", alias="SharePointVersion")
    


    @property
    def tropo_type(self) -> troposphere.kendra.SharePointConfiguration:
        from troposphere.kendra import SharePointConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SqlConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sqlconfiguration.html
    Properties:
        - Name: QueryIdentifiersEnclosingOption
    
    """
    
    QueryIdentifiersEnclosingOption_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sqlconfiguration.html#cfn-kendra-datasource-sqlconfiguration-queryidentifiersenclosingoption""", alias="QueryIdentifiersEnclosingOption")
    


    @property
    def tropo_type(self) -> troposphere.kendra.SqlConfiguration:
        from troposphere.kendra import SqlConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WebCrawlerAuthenticationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerauthenticationconfiguration.html
    Properties:
        - Name: BasicAuthentication
    
    """
    
    BasicAuthentication_: Optional[List['WebCrawlerBasicAuthentication']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerauthenticationconfiguration.html#cfn-kendra-datasource-webcrawlerauthenticationconfiguration-basicauthentication""", alias="BasicAuthentication")
    


    @property
    def tropo_type(self) -> troposphere.kendra.WebCrawlerAuthenticationConfiguration:
        from troposphere.kendra import WebCrawlerAuthenticationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WebCrawlerBasicAuthentication(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerbasicauthentication.html
    Properties:
        - Name: Port
        - Name: Host
        - Name: Credentials
    
    """
    
    Port_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerbasicauthentication.html#cfn-kendra-datasource-webcrawlerbasicauthentication-port""", alias="Port")
    Host_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerbasicauthentication.html#cfn-kendra-datasource-webcrawlerbasicauthentication-host""", alias="Host")
    Credentials_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerbasicauthentication.html#cfn-kendra-datasource-webcrawlerbasicauthentication-credentials""", alias="Credentials")
    


    @property
    def tropo_type(self) -> troposphere.kendra.WebCrawlerBasicAuthentication:
        from troposphere.kendra import WebCrawlerBasicAuthentication as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WebCrawlerConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html
    Properties:
        - Name: AuthenticationConfiguration
        - Name: MaxLinksPerPage
        - Name: ProxyConfiguration
        - Name: UrlExclusionPatterns
        - Name: MaxUrlsPerMinuteCrawlRate
        - Name: UrlInclusionPatterns
        - Name: Urls
        - Name: MaxContentSizePerPageInMegaBytes
        - Name: CrawlDepth
    
    """
    
    AuthenticationConfiguration_: Optional['WebCrawlerAuthenticationConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html#cfn-kendra-datasource-webcrawlerconfiguration-authenticationconfiguration""", alias="AuthenticationConfiguration")
    MaxLinksPerPage_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html#cfn-kendra-datasource-webcrawlerconfiguration-maxlinksperpage""", alias="MaxLinksPerPage")
    ProxyConfiguration_: Optional['ProxyConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html#cfn-kendra-datasource-webcrawlerconfiguration-proxyconfiguration""", alias="ProxyConfiguration")
    UrlExclusionPatterns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html#cfn-kendra-datasource-webcrawlerconfiguration-urlexclusionpatterns""", alias="UrlExclusionPatterns")
    MaxUrlsPerMinuteCrawlRate_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html#cfn-kendra-datasource-webcrawlerconfiguration-maxurlsperminutecrawlrate""", alias="MaxUrlsPerMinuteCrawlRate")
    UrlInclusionPatterns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html#cfn-kendra-datasource-webcrawlerconfiguration-urlinclusionpatterns""", alias="UrlInclusionPatterns")
    Urls_: 'WebCrawlerUrls' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html#cfn-kendra-datasource-webcrawlerconfiguration-urls""", alias="Urls")
    MaxContentSizePerPageInMegaBytes_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html#cfn-kendra-datasource-webcrawlerconfiguration-maxcontentsizeperpageinmegabytes""", alias="MaxContentSizePerPageInMegaBytes")
    CrawlDepth_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html#cfn-kendra-datasource-webcrawlerconfiguration-crawldepth""", alias="CrawlDepth")
    


    @property
    def tropo_type(self) -> troposphere.kendra.WebCrawlerConfiguration:
        from troposphere.kendra import WebCrawlerConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WebCrawlerSeedUrlConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerseedurlconfiguration.html
    Properties:
        - Name: WebCrawlerMode
        - Name: SeedUrls
    
    """
    
    WebCrawlerMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerseedurlconfiguration.html#cfn-kendra-datasource-webcrawlerseedurlconfiguration-webcrawlermode""", alias="WebCrawlerMode")
    SeedUrls_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerseedurlconfiguration.html#cfn-kendra-datasource-webcrawlerseedurlconfiguration-seedurls""", alias="SeedUrls")
    


    @property
    def tropo_type(self) -> troposphere.kendra.WebCrawlerSeedUrlConfiguration:
        from troposphere.kendra import WebCrawlerSeedUrlConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WebCrawlerSiteMapsConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlersitemapsconfiguration.html
    Properties:
        - Name: SiteMaps
    
    """
    
    SiteMaps_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlersitemapsconfiguration.html#cfn-kendra-datasource-webcrawlersitemapsconfiguration-sitemaps""", alias="SiteMaps")
    


    @property
    def tropo_type(self) -> troposphere.kendra.WebCrawlerSiteMapsConfiguration:
        from troposphere.kendra import WebCrawlerSiteMapsConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WebCrawlerUrls(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerurls.html
    Properties:
        - Name: SiteMapsConfiguration
        - Name: SeedUrlConfiguration
    
    """
    
    SiteMapsConfiguration_: Optional['WebCrawlerSiteMapsConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerurls.html#cfn-kendra-datasource-webcrawlerurls-sitemapsconfiguration""", alias="SiteMapsConfiguration")
    SeedUrlConfiguration_: Optional['WebCrawlerSeedUrlConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerurls.html#cfn-kendra-datasource-webcrawlerurls-seedurlconfiguration""", alias="SeedUrlConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.kendra.WebCrawlerUrls:
        from troposphere.kendra import WebCrawlerUrls as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WorkDocsConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-workdocsconfiguration.html
    Properties:
        - Name: CrawlComments
        - Name: OrganizationId
        - Name: InclusionPatterns
        - Name: UseChangeLog
        - Name: FieldMappings
        - Name: ExclusionPatterns
    
    """
    
    CrawlComments_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-workdocsconfiguration.html#cfn-kendra-datasource-workdocsconfiguration-crawlcomments""", alias="CrawlComments")
    OrganizationId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-workdocsconfiguration.html#cfn-kendra-datasource-workdocsconfiguration-organizationid""", alias="OrganizationId")
    InclusionPatterns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-workdocsconfiguration.html#cfn-kendra-datasource-workdocsconfiguration-inclusionpatterns""", alias="InclusionPatterns")
    UseChangeLog_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-workdocsconfiguration.html#cfn-kendra-datasource-workdocsconfiguration-usechangelog""", alias="UseChangeLog")
    FieldMappings_: Optional[List['DataSourceToIndexFieldMapping']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-workdocsconfiguration.html#cfn-kendra-datasource-workdocsconfiguration-fieldmappings""", alias="FieldMappings")
    ExclusionPatterns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-workdocsconfiguration.html#cfn-kendra-datasource-workdocsconfiguration-exclusionpatterns""", alias="ExclusionPatterns")
    


    @property
    def tropo_type(self) -> troposphere.kendra.WorkDocsConfiguration:
        from troposphere.kendra import WorkDocsConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Path(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-faq-s3path.html
    Properties:
        - Name: Bucket
        - Name: Key
    
    """
    
    Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-faq-s3path.html#cfn-kendra-faq-s3path-bucket""", alias="Bucket")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-faq-s3path.html#cfn-kendra-faq-s3path-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.kendra.S3Path:
        from troposphere.kendra import S3Path as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CapacityUnitsConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-capacityunitsconfiguration.html
    Properties:
        - Name: QueryCapacityUnits
        - Name: StorageCapacityUnits
    
    """
    
    QueryCapacityUnits_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-capacityunitsconfiguration.html#cfn-kendra-index-capacityunitsconfiguration-querycapacityunits""", alias="QueryCapacityUnits")
    StorageCapacityUnits_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-capacityunitsconfiguration.html#cfn-kendra-index-capacityunitsconfiguration-storagecapacityunits""", alias="StorageCapacityUnits")
    


    @property
    def tropo_type(self) -> troposphere.kendra.CapacityUnitsConfiguration:
        from troposphere.kendra import CapacityUnitsConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DocumentMetadataConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-documentmetadataconfiguration.html
    Properties:
        - Name: Relevance
        - Name: Type
        - Name: Search
        - Name: Name
    
    """
    
    Relevance_: Optional['Relevance'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-documentmetadataconfiguration.html#cfn-kendra-index-documentmetadataconfiguration-relevance""", alias="Relevance")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-documentmetadataconfiguration.html#cfn-kendra-index-documentmetadataconfiguration-type""", alias="Type")
    Search_: Optional['Search'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-documentmetadataconfiguration.html#cfn-kendra-index-documentmetadataconfiguration-search""", alias="Search")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-documentmetadataconfiguration.html#cfn-kendra-index-documentmetadataconfiguration-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.kendra.DocumentMetadataConfiguration:
        from troposphere.kendra import DocumentMetadataConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class JsonTokenTypeConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jsontokentypeconfiguration.html
    Properties:
        - Name: GroupAttributeField
        - Name: UserNameAttributeField
    
    """
    
    GroupAttributeField_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jsontokentypeconfiguration.html#cfn-kendra-index-jsontokentypeconfiguration-groupattributefield""", alias="GroupAttributeField")
    UserNameAttributeField_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jsontokentypeconfiguration.html#cfn-kendra-index-jsontokentypeconfiguration-usernameattributefield""", alias="UserNameAttributeField")
    


    @property
    def tropo_type(self) -> troposphere.kendra.JsonTokenTypeConfiguration:
        from troposphere.kendra import JsonTokenTypeConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class JwtTokenTypeConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jwttokentypeconfiguration.html
    Properties:
        - Name: ClaimRegex
        - Name: Issuer
        - Name: KeyLocation
        - Name: SecretManagerArn
        - Name: GroupAttributeField
        - Name: URL
        - Name: UserNameAttributeField
    
    """
    
    ClaimRegex_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jwttokentypeconfiguration.html#cfn-kendra-index-jwttokentypeconfiguration-claimregex""", alias="ClaimRegex")
    Issuer_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jwttokentypeconfiguration.html#cfn-kendra-index-jwttokentypeconfiguration-issuer""", alias="Issuer")
    KeyLocation_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jwttokentypeconfiguration.html#cfn-kendra-index-jwttokentypeconfiguration-keylocation""", alias="KeyLocation")
    SecretManagerArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jwttokentypeconfiguration.html#cfn-kendra-index-jwttokentypeconfiguration-secretmanagerarn""", alias="SecretManagerArn")
    GroupAttributeField_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jwttokentypeconfiguration.html#cfn-kendra-index-jwttokentypeconfiguration-groupattributefield""", alias="GroupAttributeField")
    URL_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jwttokentypeconfiguration.html#cfn-kendra-index-jwttokentypeconfiguration-url""", alias="URL")
    UserNameAttributeField_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jwttokentypeconfiguration.html#cfn-kendra-index-jwttokentypeconfiguration-usernameattributefield""", alias="UserNameAttributeField")
    


    @property
    def tropo_type(self) -> troposphere.kendra.JwtTokenTypeConfiguration:
        from troposphere.kendra import JwtTokenTypeConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Relevance(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-relevance.html
    Properties:
        - Name: Importance
        - Name: RankOrder
        - Name: ValueImportanceItems
        - Name: Freshness
        - Name: Duration
    
    """
    
    Importance_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-relevance.html#cfn-kendra-index-relevance-importance""", alias="Importance")
    RankOrder_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-relevance.html#cfn-kendra-index-relevance-rankorder""", alias="RankOrder")
    ValueImportanceItems_: Optional[List['ValueImportanceItem']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-relevance.html#cfn-kendra-index-relevance-valueimportanceitems""", alias="ValueImportanceItems")
    Freshness_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-relevance.html#cfn-kendra-index-relevance-freshness""", alias="Freshness")
    Duration_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-relevance.html#cfn-kendra-index-relevance-duration""", alias="Duration")
    


    @property
    def tropo_type(self) -> troposphere.kendra.Relevance:
        from troposphere.kendra import Relevance as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Search(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-search.html
    Properties:
        - Name: Displayable
        - Name: Sortable
        - Name: Facetable
        - Name: Searchable
    
    """
    
    Displayable_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-search.html#cfn-kendra-index-search-displayable""", alias="Displayable")
    Sortable_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-search.html#cfn-kendra-index-search-sortable""", alias="Sortable")
    Facetable_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-search.html#cfn-kendra-index-search-facetable""", alias="Facetable")
    Searchable_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-search.html#cfn-kendra-index-search-searchable""", alias="Searchable")
    


    @property
    def tropo_type(self) -> troposphere.kendra.Search:
        from troposphere.kendra import Search as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ServerSideEncryptionConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-serversideencryptionconfiguration.html
    Properties:
        - Name: KmsKeyId
    
    """
    
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-serversideencryptionconfiguration.html#cfn-kendra-index-serversideencryptionconfiguration-kmskeyid""", alias="KmsKeyId")
    


    @property
    def tropo_type(self) -> troposphere.kendra.ServerSideEncryptionConfiguration:
        from troposphere.kendra import ServerSideEncryptionConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class UserTokenConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-usertokenconfiguration.html
    Properties:
        - Name: JwtTokenTypeConfiguration
        - Name: JsonTokenTypeConfiguration
    
    """
    
    JwtTokenTypeConfiguration_: Optional['JwtTokenTypeConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-usertokenconfiguration.html#cfn-kendra-index-usertokenconfiguration-jwttokentypeconfiguration""", alias="JwtTokenTypeConfiguration")
    JsonTokenTypeConfiguration_: Optional['JsonTokenTypeConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-usertokenconfiguration.html#cfn-kendra-index-usertokenconfiguration-jsontokentypeconfiguration""", alias="JsonTokenTypeConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.kendra.UserTokenConfiguration:
        from troposphere.kendra import UserTokenConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ValueImportanceItem(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-valueimportanceitem.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-valueimportanceitem.html#cfn-kendra-index-valueimportanceitem-value""", alias="Value")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-valueimportanceitem.html#cfn-kendra-index-valueimportanceitem-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.kendra.ValueImportanceItem:
        from troposphere.kendra import ValueImportanceItem as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class DataSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html
    Properties:
        - Name: CustomDocumentEnrichmentConfiguration
        - Name: IndexId
        - Name: LanguageCode
        - Name: Type
        - Name: Description
        - Name: Schedule
        - Name: DataSourceConfiguration
        - Name: RoleArn
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CustomDocumentEnrichmentConfiguration_: Optional['CustomDocumentEnrichmentConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-customdocumentenrichmentconfiguration""", alias="CustomDocumentEnrichmentConfiguration")
    IndexId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-indexid""", alias="IndexId")
    LanguageCode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-languagecode""", alias="LanguageCode")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-type""", alias="Type")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-description""", alias="Description")
    Schedule_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-schedule""", alias="Schedule")
    DataSourceConfiguration_: Optional['DataSourceConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-datasourceconfiguration""", alias="DataSourceConfiguration")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-rolearn""", alias="RoleArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.kendra.DataSource:
        from troposphere.kendra import DataSource as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.kendra import DataSource as TropoT
        return resource_to_troposphere(self, TropoT)


class Faq(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html
    Properties:
        - Name: IndexId
        - Name: Description
        - Name: S3Path
        - Name: FileFormat
        - Name: RoleArn
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    IndexId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-indexid""", alias="IndexId")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-description""", alias="Description")
    S3Path_: 'S3Path' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-s3path""", alias="S3Path")
    FileFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-fileformat""", alias="FileFormat")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-rolearn""", alias="RoleArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.kendra.Faq:
        from troposphere.kendra import Faq as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.kendra import Faq as TropoT
        return resource_to_troposphere(self, TropoT)


class Index(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html
    Properties:
        - Name: Description
        - Name: UserContextPolicy
        - Name: CapacityUnits
        - Name: ServerSideEncryptionConfiguration
        - Name: DocumentMetadataConfigurations
        - Name: Tags
        - Name: RoleArn
        - Name: Edition
        - Name: Name
        - Name: UserTokenConfigurations
    Attributes:
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-description""", alias="Description")
    UserContextPolicy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-usercontextpolicy""", alias="UserContextPolicy")
    CapacityUnits_: Optional['CapacityUnitsConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-capacityunits""", alias="CapacityUnits")
    ServerSideEncryptionConfiguration_: Optional['ServerSideEncryptionConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-serversideencryptionconfiguration""", alias="ServerSideEncryptionConfiguration")
    DocumentMetadataConfigurations_: Optional[List['DocumentMetadataConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-documentmetadataconfigurations""", alias="DocumentMetadataConfigurations")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-tags""", alias="Tags")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-rolearn""", alias="RoleArn")
    Edition_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-edition""", alias="Edition")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-name""", alias="Name")
    UserTokenConfigurations_: Optional[List['UserTokenConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-usertokenconfigurations""", alias="UserTokenConfigurations")
    

    @property
    def tropo_type(self) -> troposphere.kendra.Index:
        from troposphere.kendra import Index as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.kendra import Index as TropoT
        return resource_to_troposphere(self, TropoT)

