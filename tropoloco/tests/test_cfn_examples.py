import json
import os

import yaml
import pytest


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

BAD_AWS_EXAMPLES = [
    "appflow_Flow.json", # missing required types
    "appmesh_VirtualRouter.yaml", #null set on non-nullable field MeshName
    "appmesh_VirtualRouter.json", #null set on non-nullable field MeshName
    "apprunner_Service.yaml", #Port 8080 is int instead of string.
    "cleanrooms_AnalysisTemplate.yaml", # can't tell it's a str issue
    "cleanrooms_AnalysisTemplate.json" # can't tell it's a str issue
    "cleanrooms_AnalysisTemplate.json" # can't tell it's a str issue
    "cleanrooms_AnalysisTemplate.json", # can't tell it's a str issue
    "cloudformation_HookDefaultVersion.yaml", #can't tell it's a str issue
    "cloudformation_HookDefaultVersion.json", #can't tell it's a str issue
    "cloudfront_Distribution.yaml", #missing required types
    "cloudfront_Distribution.json", #missing required types
    "cloudwatch_AnomalyDetector.yaml", #can't tell it's a str issue
    "cloudwatch_AnomalyDetector.json", #can't tell it's a str issue
    "dms_ReplicationTask.json", #can't tell it's a str issue
    "cloudwatch_AnomalyDetector.json", #can't tell it's a str issue
    "databrew_Recipe.yaml", #can't tell it's a str issue
    "detective_MemberInvitation.yaml", #can't tell it's a str issue
    "detective_OrganizationAdmin.yaml", #can't tell it's a str issue 
    "ec2_Host.yaml", #can't tell it's a str issue
    "ecr_ReplicationConfiguration.yaml", #TODO troposphere renamed a circular reference where property and resource had the same name
    #while understandable... it means pydantic can't parse the CFN if implementing the tropo type. We will need to implement a hack,
    "ecr_ReplicationConfiguration.json", #TODO troposphere renamed a circular reference where property and resource had the same name    
    "elasticloadbalancing_LoadBalancer.yaml", #TODO tropo doesn't implement this type... will have to hack
    "elasticloadbalancing_LoadBalancer.json", #TODO tropo doesn't implement this type... will have to hack
    "fsx_FileSystem.yaml", #missing required types
    "fsx_FileSystem.json", #missing required types
    "glue_Crawler.yaml", #missing/bad types
    "glue_Crawler.json", #missing/bad types
    "greengrass_LoggerDefinition.yaml", #tropo renamed the type
    "greengrass_LoggerDefinition.json", #tropo renamed the type
    "lakeformation_DataLakeSettings.yaml", #bug in tropo...ExternalDataFilteringAllowList must be empty list
    "lakeformation_DataLakeSettings.json", #bug in tropo...ExternalDataFilteringAllowList must be empty list
    "macie_FindingsFilter.yaml", #Troposphere typed this as a dict... when it's actually a map with specific keys #TODO raise compatability
    "macie_FindingsFilter.json", #Troposphere typed this as a dict... when it's actually a map with specific keys #TODO raise compatability
    "networkfirewall_RuleGroup.yaml", #Looks like a troposphere bug. It's throwing a type error, but the type conversion is correct
    "networkfirewall_RuleGroup.json", #Looks like a troposphere bug. It's throwing a type error, but the type conversion is correct
    "organizations_Policy.yaml", #inline json policy instead of yaml. TODO should maybe support inline policies
    "organizations_Policy.json", #inline json policy instead of json. TODO should maybe support inline policies
    "organizations_ResourcePolicy.yaml", #inline json policy instead of yaml.
    "organizations_ResourcePolicy.json", #inline json policy instead of json.
    "rds_OptionGroup.yaml", # I think this example is typed wrong... TODO double check this open
    "rds_OptionGroup.json", # I think this example is typed wrong... TODO double check this open
    "rekognition_StreamProcessor.yaml", # troposphere has import bug in validator
    "rekognition_StreamProcessor.json", # troposphere has import bug in validator
    "s3outposts_Bucket.yaml", # missing a required kwarg in the example
    "s3outposts_Bucket.json", # missing a required kwarg in the example
    "s3outposts_Endpoint.yaml", # Keys Misnamed "ID" instead of "Id"
    "s3outposts_Endpoint.json", # Keys Misnamed "ID" instead of "Id"
    "ssm_Document.yaml", # Inline JSON type
    "ssm_Document.json", # Inline JSON type
    "ssm_MaintenanceWindowTask.yaml", #TODO need to implement JSON type
    "ssm_MaintenanceWindowTask.json", #TODO need to implement JSON type
    "ssmincidents_ResponsePlan.yaml", #Example typed wrong
    "ssmincidents_ResponsePlan.json", # Example typed wrong
    "securityhub_AutomationRule.yaml", # AWS Type errors. Small and fixable. 
    "securityhub_AutomationRule.json", # AWS Type errors. Small and fixable. 
    "synthetics_Canary.yaml", # Yaml type issue with int
]


def load_yaml_file(filename):
    with open(os.path.join(BASE_DIR, 'aws_cfn_examples', filename), 'r') as file:
        return yaml.safe_load(file)

def load_json_file(filename):
    with open(os.path.join(BASE_DIR, 'aws_cfn_examples', filename), 'r') as file:
        return json.load(file)

def should_skip_test(filename):
    with open(os.path.join(BASE_DIR, 'aws_cfn_examples', filename), 'r') as file:
        contents =  file.read()
    if "Fn::" in contents:
        return True
    if "Ref:" in contents or '"Ref":' in contents:
        return True
    if filename in BAD_AWS_EXAMPLES:
        return True
    if "cleanrooms" in filename:
        print("cleanrooms not supported yet")
        return True
    return False




@pytest.mark.skipif(should_skip_test("aps_Workspace.yaml"), reason="Skipping Test for compatability reason")
def test_aps_Workspace_yaml():
    data = load_yaml_file("aps_Workspace.yaml")

    from tropoloco.model.aps import Workspace as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("aps_Workspace.json"), reason="Skipping Test for compatability reason")
def test_aps_Workspace_json():
    data = load_json_file("aps_Workspace.json")

    from tropoloco.model.aps import Workspace as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("accessanalyzer_Analyzer.yaml"), reason="Skipping Test for compatability reason")
def test_accessanalyzer_Analyzer_yaml():
    data = load_yaml_file("accessanalyzer_Analyzer.yaml")

    from tropoloco.model.accessanalyzer import Analyzer as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("accessanalyzer_Analyzer.json"), reason="Skipping Test for compatability reason")
def test_accessanalyzer_Analyzer_json():
    data = load_json_file("accessanalyzer_Analyzer.json")

    from tropoloco.model.accessanalyzer import Analyzer as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("amazonmq_Broker.yaml"), reason="Skipping Test for compatability reason")
def test_amazonmq_Broker_yaml():
    data = load_yaml_file("amazonmq_Broker.yaml")

    from tropoloco.model.amazonmq import Broker as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("amazonmq_Broker.json"), reason="Skipping Test for compatability reason")
def test_amazonmq_Broker_json():
    data = load_json_file("amazonmq_Broker.json")

    from tropoloco.model.amazonmq import Broker as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("amazonmq_Configuration.yaml"), reason="Skipping Test for compatability reason")
def test_amazonmq_Configuration_yaml():
    data = load_yaml_file("amazonmq_Configuration.yaml")

    from tropoloco.model.amazonmq import Configuration as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("amazonmq_Configuration.json"), reason="Skipping Test for compatability reason")
def test_amazonmq_Configuration_json():
    data = load_json_file("amazonmq_Configuration.json")

    from tropoloco.model.amazonmq import Configuration as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("amazonmq_ConfigurationAssociation.yaml"), reason="Skipping Test for compatability reason")
def test_amazonmq_ConfigurationAssociation_yaml():
    data = load_yaml_file("amazonmq_ConfigurationAssociation.yaml")

    from tropoloco.model.amazonmq import ConfigurationAssociation as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("amazonmq_ConfigurationAssociation.json"), reason="Skipping Test for compatability reason")
def test_amazonmq_ConfigurationAssociation_json():
    data = load_json_file("amazonmq_ConfigurationAssociation.json")

    from tropoloco.model.amazonmq import ConfigurationAssociation as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("apigateway_ClientCertificate.yaml"), reason="Skipping Test for compatability reason")
def test_apigateway_ClientCertificate_yaml():
    data = load_yaml_file("apigateway_ClientCertificate.yaml")

    from tropoloco.model.apigateway import ClientCertificate as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("apigateway_ClientCertificate.json"), reason="Skipping Test for compatability reason")
def test_apigateway_ClientCertificate_json():
    data = load_json_file("apigateway_ClientCertificate.json")

    from tropoloco.model.apigateway import ClientCertificate as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("apigatewayv2_Api.yaml"), reason="Skipping Test for compatability reason")
def test_apigatewayv2_Api_yaml():
    data = load_yaml_file("apigatewayv2_Api.yaml")

    from tropoloco.model.apigatewayv2 import Api as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("apigatewayv2_Api.json"), reason="Skipping Test for compatability reason")
def test_apigatewayv2_Api_json():
    data = load_json_file("apigatewayv2_Api.json")

    from tropoloco.model.apigatewayv2 import Api as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("apigatewayv2_DomainName.yaml"), reason="Skipping Test for compatability reason")
def test_apigatewayv2_DomainName_yaml():
    data = load_yaml_file("apigatewayv2_DomainName.yaml")

    from tropoloco.model.apigatewayv2 import DomainName as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("apigatewayv2_DomainName.json"), reason="Skipping Test for compatability reason")
def test_apigatewayv2_DomainName_json():
    data = load_json_file("apigatewayv2_DomainName.json")

    from tropoloco.model.apigatewayv2 import DomainName as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("appflow_Flow.yaml"), reason="Skipping Test for compatability reason")
def test_appflow_Flow_yaml():
    data = load_yaml_file("appflow_Flow.yaml")

    from tropoloco.model.appflow import Flow as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("appflow_Flow.json"), reason="Skipping Test for compatability reason")
def test_appflow_Flow_json():
    data = load_json_file("appflow_Flow.json")

    from tropoloco.model.appflow import Flow as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("appmesh_Mesh.yaml"), reason="Skipping Test for compatability reason")
def test_appmesh_Mesh_yaml():
    data = load_yaml_file("appmesh_Mesh.yaml")

    from tropoloco.model.appmesh import Mesh as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("appmesh_Mesh.json"), reason="Skipping Test for compatability reason")
def test_appmesh_Mesh_json():
    data = load_json_file("appmesh_Mesh.json")

    from tropoloco.model.appmesh import Mesh as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("appmesh_VirtualRouter.yaml"), reason="Skipping Test for compatability reason")
def test_appmesh_VirtualRouter_yaml():
    data = load_yaml_file("appmesh_VirtualRouter.yaml")

    from tropoloco.model.appmesh import VirtualRouter as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("appmesh_VirtualRouter.json"), reason="Skipping Test for compatability reason")
def test_appmesh_VirtualRouter_json():
    data = load_json_file("appmesh_VirtualRouter.json")

    from tropoloco.model.appmesh import VirtualRouter as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("apprunner_AutoScalingConfiguration.yaml"), reason="Skipping Test for compatability reason")
def test_apprunner_AutoScalingConfiguration_yaml():
    data = load_yaml_file("apprunner_AutoScalingConfiguration.yaml")

    from tropoloco.model.apprunner import AutoScalingConfiguration as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("apprunner_AutoScalingConfiguration.json"), reason="Skipping Test for compatability reason")
def test_apprunner_AutoScalingConfiguration_json():
    data = load_json_file("apprunner_AutoScalingConfiguration.json")

    from tropoloco.model.apprunner import AutoScalingConfiguration as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("apprunner_ObservabilityConfiguration.yaml"), reason="Skipping Test for compatability reason")
def test_apprunner_ObservabilityConfiguration_yaml():
    data = load_yaml_file("apprunner_ObservabilityConfiguration.yaml")

    from tropoloco.model.apprunner import ObservabilityConfiguration as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("apprunner_ObservabilityConfiguration.json"), reason="Skipping Test for compatability reason")
def test_apprunner_ObservabilityConfiguration_json():
    data = load_json_file("apprunner_ObservabilityConfiguration.json")

    from tropoloco.model.apprunner import ObservabilityConfiguration as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("apprunner_Service.yaml"), reason="Skipping Test for compatability reason")
def test_apprunner_Service_yaml():
    data = load_yaml_file("apprunner_Service.yaml")

    from tropoloco.model.apprunner import Service as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("apprunner_Service.json"), reason="Skipping Test for compatability reason")
def test_apprunner_Service_json():
    data = load_json_file("apprunner_Service.json")

    from tropoloco.model.apprunner import Service as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("apprunner_VpcConnector.yaml"), reason="Skipping Test for compatability reason")
def test_apprunner_VpcConnector_yaml():
    data = load_yaml_file("apprunner_VpcConnector.yaml")

    from tropoloco.model.apprunner import VpcConnector as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("apprunner_VpcConnector.json"), reason="Skipping Test for compatability reason")
def test_apprunner_VpcConnector_json():
    data = load_json_file("apprunner_VpcConnector.json")

    from tropoloco.model.apprunner import VpcConnector as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("apprunner_VpcIngressConnection.yaml"), reason="Skipping Test for compatability reason")
def test_apprunner_VpcIngressConnection_yaml():
    data = load_yaml_file("apprunner_VpcIngressConnection.yaml")

    from tropoloco.model.apprunner import VpcIngressConnection as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("apprunner_VpcIngressConnection.json"), reason="Skipping Test for compatability reason")
def test_apprunner_VpcIngressConnection_json():
    data = load_json_file("apprunner_VpcIngressConnection.json")

    from tropoloco.model.apprunner import VpcIngressConnection as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("appsync_DataSource.yaml"), reason="Skipping Test for compatability reason")
def test_appsync_DataSource_yaml():
    data = load_yaml_file("appsync_DataSource.yaml")

    from tropoloco.model.appsync import DataSource as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("appsync_DataSource.json"), reason="Skipping Test for compatability reason")
def test_appsync_DataSource_json():
    data = load_json_file("appsync_DataSource.json")

    from tropoloco.model.appsync import DataSource as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("applicationautoscaling_ScalableTarget.yaml"), reason="Skipping Test for compatability reason")
def test_applicationautoscaling_ScalableTarget_yaml():
    data = load_yaml_file("applicationautoscaling_ScalableTarget.yaml")

    from tropoloco.model.applicationautoscaling import ScalableTarget as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("applicationautoscaling_ScalableTarget.json"), reason="Skipping Test for compatability reason")
def test_applicationautoscaling_ScalableTarget_json():
    data = load_json_file("applicationautoscaling_ScalableTarget.json")

    from tropoloco.model.applicationautoscaling import ScalableTarget as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("applicationautoscaling_ScalingPolicy.yaml"), reason="Skipping Test for compatability reason")
def test_applicationautoscaling_ScalingPolicy_yaml():
    data = load_yaml_file("applicationautoscaling_ScalingPolicy.yaml")

    from tropoloco.model.applicationautoscaling import ScalingPolicy as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("applicationautoscaling_ScalingPolicy.json"), reason="Skipping Test for compatability reason")
def test_applicationautoscaling_ScalingPolicy_json():
    data = load_json_file("applicationautoscaling_ScalingPolicy.json")

    from tropoloco.model.applicationautoscaling import ScalingPolicy as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("applicationinsights_Application.yaml"), reason="Skipping Test for compatability reason")
def test_applicationinsights_Application_yaml():
    data = load_yaml_file("applicationinsights_Application.yaml")

    from tropoloco.model.applicationinsights import Application as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("applicationinsights_Application.json"), reason="Skipping Test for compatability reason")
def test_applicationinsights_Application_json():
    data = load_json_file("applicationinsights_Application.json")

    from tropoloco.model.applicationinsights import Application as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("athena_DataCatalog.yaml"), reason="Skipping Test for compatability reason")
def test_athena_DataCatalog_yaml():
    data = load_yaml_file("athena_DataCatalog.yaml")

    from tropoloco.model.athena import DataCatalog as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("athena_DataCatalog.json"), reason="Skipping Test for compatability reason")
def test_athena_DataCatalog_json():
    data = load_json_file("athena_DataCatalog.json")

    from tropoloco.model.athena import DataCatalog as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("athena_NamedQuery.yaml"), reason="Skipping Test for compatability reason")
def test_athena_NamedQuery_yaml():
    data = load_yaml_file("athena_NamedQuery.yaml")

    from tropoloco.model.athena import NamedQuery as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("athena_NamedQuery.json"), reason="Skipping Test for compatability reason")
def test_athena_NamedQuery_json():
    data = load_json_file("athena_NamedQuery.json")

    from tropoloco.model.athena import NamedQuery as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("athena_WorkGroup.yaml"), reason="Skipping Test for compatability reason")
def test_athena_WorkGroup_yaml():
    data = load_yaml_file("athena_WorkGroup.yaml")

    from tropoloco.model.athena import WorkGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("athena_WorkGroup.json"), reason="Skipping Test for compatability reason")
def test_athena_WorkGroup_json():
    data = load_json_file("athena_WorkGroup.json")

    from tropoloco.model.athena import WorkGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("batch_ComputeEnvironment.yaml"), reason="Skipping Test for compatability reason")
def test_batch_ComputeEnvironment_yaml():
    data = load_yaml_file("batch_ComputeEnvironment.yaml")

    from tropoloco.model.batch import ComputeEnvironment as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("batch_ComputeEnvironment.json"), reason="Skipping Test for compatability reason")
def test_batch_ComputeEnvironment_json():
    data = load_json_file("batch_ComputeEnvironment.json")

    from tropoloco.model.batch import ComputeEnvironment as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("batch_JobDefinition.yaml"), reason="Skipping Test for compatability reason")
def test_batch_JobDefinition_yaml():
    data = load_yaml_file("batch_JobDefinition.yaml")

    from tropoloco.model.batch import JobDefinition as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("batch_JobDefinition.json"), reason="Skipping Test for compatability reason")
def test_batch_JobDefinition_json():
    data = load_json_file("batch_JobDefinition.json")

    from tropoloco.model.batch import JobDefinition as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("batch_JobQueue.yaml"), reason="Skipping Test for compatability reason")
def test_batch_JobQueue_yaml():
    data = load_yaml_file("batch_JobQueue.yaml")

    from tropoloco.model.batch import JobQueue as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("batch_JobQueue.json"), reason="Skipping Test for compatability reason")
def test_batch_JobQueue_json():
    data = load_json_file("batch_JobQueue.json")

    from tropoloco.model.batch import JobQueue as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ce_AnomalySubscription.yaml"), reason="Skipping Test for compatability reason")
def test_ce_AnomalySubscription_yaml():
    data = load_yaml_file("ce_AnomalySubscription.yaml")

    from tropoloco.model.ce import AnomalySubscription as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ce_AnomalySubscription.json"), reason="Skipping Test for compatability reason")
def test_ce_AnomalySubscription_json():
    data = load_json_file("ce_AnomalySubscription.json")

    from tropoloco.model.ce import AnomalySubscription as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("cassandra_Keyspace.yaml"), reason="Skipping Test for compatability reason")
def test_cassandra_Keyspace_yaml():
    data = load_yaml_file("cassandra_Keyspace.yaml")

    from tropoloco.model.cassandra import Keyspace as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("cassandra_Keyspace.json"), reason="Skipping Test for compatability reason")
def test_cassandra_Keyspace_json():
    data = load_json_file("cassandra_Keyspace.json")

    from tropoloco.model.cassandra import Keyspace as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("cassandra_Table.yaml"), reason="Skipping Test for compatability reason")
def test_cassandra_Table_yaml():
    data = load_yaml_file("cassandra_Table.yaml")

    from tropoloco.model.cassandra import Table as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("cassandra_Table.json"), reason="Skipping Test for compatability reason")
def test_cassandra_Table_json():
    data = load_json_file("cassandra_Table.json")

    from tropoloco.model.cassandra import Table as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("certificatemanager_Certificate.yaml"), reason="Skipping Test for compatability reason")
def test_certificatemanager_Certificate_yaml():
    data = load_yaml_file("certificatemanager_Certificate.yaml")

    from tropoloco.model.certificatemanager import Certificate as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("certificatemanager_Certificate.json"), reason="Skipping Test for compatability reason")
def test_certificatemanager_Certificate_json():
    data = load_json_file("certificatemanager_Certificate.json")

    from tropoloco.model.certificatemanager import Certificate as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("cleanrooms_AnalysisTemplate.yaml"), reason="Skipping Test for compatability reason")
def test_cleanrooms_AnalysisTemplate_yaml():
    data = load_yaml_file("cleanrooms_AnalysisTemplate.yaml")

    from tropoloco.model.cleanrooms import AnalysisTemplate as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("cleanrooms_AnalysisTemplate.json"), reason="Skipping Test for compatability reason")
def test_cleanrooms_AnalysisTemplate_json():
    data = load_json_file("cleanrooms_AnalysisTemplate.json")

    from tropoloco.model.cleanrooms import AnalysisTemplate as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("cleanrooms_ConfiguredTableAssociation.yaml"), reason="Skipping Test for compatability reason")
def test_cleanrooms_ConfiguredTableAssociation_yaml():
    data = load_yaml_file("cleanrooms_ConfiguredTableAssociation.yaml")

    from tropoloco.model.cleanrooms import ConfiguredTableAssociation as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("cleanrooms_ConfiguredTableAssociation.json"), reason="Skipping Test for compatability reason")
def test_cleanrooms_ConfiguredTableAssociation_json():
    data = load_json_file("cleanrooms_ConfiguredTableAssociation.json")

    from tropoloco.model.cleanrooms import ConfiguredTableAssociation as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("cloudformation_HookDefaultVersion.yaml"), reason="Skipping Test for compatability reason")
def test_cloudformation_HookDefaultVersion_yaml():
    data = load_yaml_file("cloudformation_HookDefaultVersion.yaml")

    from tropoloco.model.cloudformation import HookDefaultVersion as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("cloudformation_HookDefaultVersion.json"), reason="Skipping Test for compatability reason")
def test_cloudformation_HookDefaultVersion_json():
    data = load_json_file("cloudformation_HookDefaultVersion.json")

    from tropoloco.model.cloudformation import HookDefaultVersion as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("cloudformation_HookTypeConfig.yaml"), reason="Skipping Test for compatability reason")
def test_cloudformation_HookTypeConfig_yaml():
    data = load_yaml_file("cloudformation_HookTypeConfig.yaml")

    from tropoloco.model.cloudformation import HookTypeConfig as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("cloudformation_HookTypeConfig.json"), reason="Skipping Test for compatability reason")
def test_cloudformation_HookTypeConfig_json():
    data = load_json_file("cloudformation_HookTypeConfig.json")

    from tropoloco.model.cloudformation import HookTypeConfig as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("cloudformation_ModuleVersion.yaml"), reason="Skipping Test for compatability reason")
def test_cloudformation_ModuleVersion_yaml():
    data = load_yaml_file("cloudformation_ModuleVersion.yaml")

    from tropoloco.model.cloudformation import ModuleVersion as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("cloudformation_ModuleVersion.json"), reason="Skipping Test for compatability reason")
def test_cloudformation_ModuleVersion_json():
    data = load_json_file("cloudformation_ModuleVersion.json")

    from tropoloco.model.cloudformation import ModuleVersion as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("cloudfront_CloudFrontOriginAccessIdentity.yaml"), reason="Skipping Test for compatability reason")
def test_cloudfront_CloudFrontOriginAccessIdentity_yaml():
    data = load_yaml_file("cloudfront_CloudFrontOriginAccessIdentity.yaml")

    from tropoloco.model.cloudfront import CloudFrontOriginAccessIdentity as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("cloudfront_CloudFrontOriginAccessIdentity.json"), reason="Skipping Test for compatability reason")
def test_cloudfront_CloudFrontOriginAccessIdentity_json():
    data = load_json_file("cloudfront_CloudFrontOriginAccessIdentity.json")

    from tropoloco.model.cloudfront import CloudFrontOriginAccessIdentity as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("cloudfront_Distribution.yaml"), reason="Skipping Test for compatability reason")
def test_cloudfront_Distribution_yaml():
    data = load_yaml_file("cloudfront_Distribution.yaml")

    from tropoloco.model.cloudfront import Distribution as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("cloudfront_Distribution.json"), reason="Skipping Test for compatability reason")
def test_cloudfront_Distribution_json():
    data = load_json_file("cloudfront_Distribution.json")

    from tropoloco.model.cloudfront import Distribution as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("cloudwatch_Alarm.yaml"), reason="Skipping Test for compatability reason")
def test_cloudwatch_Alarm_yaml():
    data = load_yaml_file("cloudwatch_Alarm.yaml")

    from tropoloco.model.cloudwatch import Alarm as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("cloudwatch_Alarm.json"), reason="Skipping Test for compatability reason")
def test_cloudwatch_Alarm_json():
    data = load_json_file("cloudwatch_Alarm.json")

    from tropoloco.model.cloudwatch import Alarm as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("cloudwatch_AnomalyDetector.yaml"), reason="Skipping Test for compatability reason")
def test_cloudwatch_AnomalyDetector_yaml():
    data = load_yaml_file("cloudwatch_AnomalyDetector.yaml")

    from tropoloco.model.cloudwatch import AnomalyDetector as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("cloudwatch_AnomalyDetector.json"), reason="Skipping Test for compatability reason")
def test_cloudwatch_AnomalyDetector_json():
    data = load_json_file("cloudwatch_AnomalyDetector.json")

    from tropoloco.model.cloudwatch import AnomalyDetector as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("cloudwatch_MetricStream.yaml"), reason="Skipping Test for compatability reason")
def test_cloudwatch_MetricStream_yaml():
    data = load_yaml_file("cloudwatch_MetricStream.yaml")

    from tropoloco.model.cloudwatch import MetricStream as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("cloudwatch_MetricStream.json"), reason="Skipping Test for compatability reason")
def test_cloudwatch_MetricStream_json():
    data = load_json_file("cloudwatch_MetricStream.json")

    from tropoloco.model.cloudwatch import MetricStream as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("codeartifact_Domain.yaml"), reason="Skipping Test for compatability reason")
def test_codeartifact_Domain_yaml():
    data = load_yaml_file("codeartifact_Domain.yaml")

    from tropoloco.model.codeartifact import Domain as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("codeartifact_Domain.json"), reason="Skipping Test for compatability reason")
def test_codeartifact_Domain_json():
    data = load_json_file("codeartifact_Domain.json")

    from tropoloco.model.codeartifact import Domain as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("codebuild_SourceCredential.yaml"), reason="Skipping Test for compatability reason")
def test_codebuild_SourceCredential_yaml():
    data = load_yaml_file("codebuild_SourceCredential.yaml")

    from tropoloco.model.codebuild import SourceCredential as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("codebuild_SourceCredential.json"), reason="Skipping Test for compatability reason")
def test_codebuild_SourceCredential_json():
    data = load_json_file("codebuild_SourceCredential.json")

    from tropoloco.model.codebuild import SourceCredential as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("codedeploy_Application.yaml"), reason="Skipping Test for compatability reason")
def test_codedeploy_Application_yaml():
    data = load_yaml_file("codedeploy_Application.yaml")

    from tropoloco.model.codedeploy import Application as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("codedeploy_Application.json"), reason="Skipping Test for compatability reason")
def test_codedeploy_Application_json():
    data = load_json_file("codedeploy_Application.json")

    from tropoloco.model.codedeploy import Application as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("codedeploy_DeploymentConfig.yaml"), reason="Skipping Test for compatability reason")
def test_codedeploy_DeploymentConfig_yaml():
    data = load_yaml_file("codedeploy_DeploymentConfig.yaml")

    from tropoloco.model.codedeploy import DeploymentConfig as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("codedeploy_DeploymentConfig.json"), reason="Skipping Test for compatability reason")
def test_codedeploy_DeploymentConfig_json():
    data = load_json_file("codedeploy_DeploymentConfig.json")

    from tropoloco.model.codedeploy import DeploymentConfig as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("codeguruprofiler_ProfilingGroup.yaml"), reason="Skipping Test for compatability reason")
def test_codeguruprofiler_ProfilingGroup_yaml():
    data = load_yaml_file("codeguruprofiler_ProfilingGroup.yaml")

    from tropoloco.model.codeguruprofiler import ProfilingGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("codeguruprofiler_ProfilingGroup.json"), reason="Skipping Test for compatability reason")
def test_codeguruprofiler_ProfilingGroup_json():
    data = load_json_file("codeguruprofiler_ProfilingGroup.json")

    from tropoloco.model.codeguruprofiler import ProfilingGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("codegurureviewer_RepositoryAssociation.yaml"), reason="Skipping Test for compatability reason")
def test_codegurureviewer_RepositoryAssociation_yaml():
    data = load_yaml_file("codegurureviewer_RepositoryAssociation.yaml")

    from tropoloco.model.codegurureviewer import RepositoryAssociation as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("codegurureviewer_RepositoryAssociation.json"), reason="Skipping Test for compatability reason")
def test_codegurureviewer_RepositoryAssociation_json():
    data = load_json_file("codegurureviewer_RepositoryAssociation.json")

    from tropoloco.model.codegurureviewer import RepositoryAssociation as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("codepipeline_CustomActionType.yaml"), reason="Skipping Test for compatability reason")
def test_codepipeline_CustomActionType_yaml():
    data = load_yaml_file("codepipeline_CustomActionType.yaml")

    from tropoloco.model.codepipeline import CustomActionType as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("codepipeline_CustomActionType.json"), reason="Skipping Test for compatability reason")
def test_codepipeline_CustomActionType_json():
    data = load_json_file("codepipeline_CustomActionType.json")

    from tropoloco.model.codepipeline import CustomActionType as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("codestar_GitHubRepository.yaml"), reason="Skipping Test for compatability reason")
def test_codestar_GitHubRepository_yaml():
    data = load_yaml_file("codestar_GitHubRepository.yaml")

    from tropoloco.model.codestar import GitHubRepository as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("codestar_GitHubRepository.json"), reason="Skipping Test for compatability reason")
def test_codestar_GitHubRepository_json():
    data = load_json_file("codestar_GitHubRepository.json")

    from tropoloco.model.codestar import GitHubRepository as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("codestarconnections_Connection.yaml"), reason="Skipping Test for compatability reason")
def test_codestarconnections_Connection_yaml():
    data = load_yaml_file("codestarconnections_Connection.yaml")

    from tropoloco.model.codestarconnections import Connection as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("codestarconnections_Connection.json"), reason="Skipping Test for compatability reason")
def test_codestarconnections_Connection_json():
    data = load_json_file("codestarconnections_Connection.json")

    from tropoloco.model.codestarconnections import Connection as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("codestarnotifications_NotificationRule.yaml"), reason="Skipping Test for compatability reason")
def test_codestarnotifications_NotificationRule_yaml():
    data = load_yaml_file("codestarnotifications_NotificationRule.yaml")

    from tropoloco.model.codestarnotifications import NotificationRule as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("codestarnotifications_NotificationRule.json"), reason="Skipping Test for compatability reason")
def test_codestarnotifications_NotificationRule_json():
    data = load_json_file("codestarnotifications_NotificationRule.json")

    from tropoloco.model.codestarnotifications import NotificationRule as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("config_ConfigurationRecorder.yaml"), reason="Skipping Test for compatability reason")
def test_config_ConfigurationRecorder_yaml():
    data = load_yaml_file("config_ConfigurationRecorder.yaml")

    from tropoloco.model.config import ConfigurationRecorder as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("config_ConfigurationRecorder.json"), reason="Skipping Test for compatability reason")
def test_config_ConfigurationRecorder_json():
    data = load_json_file("config_ConfigurationRecorder.json")

    from tropoloco.model.config import ConfigurationRecorder as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("config_ConformancePack.yaml"), reason="Skipping Test for compatability reason")
def test_config_ConformancePack_yaml():
    data = load_yaml_file("config_ConformancePack.yaml")

    from tropoloco.model.config import ConformancePack as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("config_ConformancePack.json"), reason="Skipping Test for compatability reason")
def test_config_ConformancePack_json():
    data = load_json_file("config_ConformancePack.json")

    from tropoloco.model.config import ConformancePack as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("config_DeliveryChannel.yaml"), reason="Skipping Test for compatability reason")
def test_config_DeliveryChannel_yaml():
    data = load_yaml_file("config_DeliveryChannel.yaml")

    from tropoloco.model.config import DeliveryChannel as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("config_DeliveryChannel.json"), reason="Skipping Test for compatability reason")
def test_config_DeliveryChannel_json():
    data = load_json_file("config_DeliveryChannel.json")

    from tropoloco.model.config import DeliveryChannel as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("config_OrganizationConfigRule.yaml"), reason="Skipping Test for compatability reason")
def test_config_OrganizationConfigRule_yaml():
    data = load_yaml_file("config_OrganizationConfigRule.yaml")

    from tropoloco.model.config import OrganizationConfigRule as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("config_OrganizationConfigRule.json"), reason="Skipping Test for compatability reason")
def test_config_OrganizationConfigRule_json():
    data = load_json_file("config_OrganizationConfigRule.json")

    from tropoloco.model.config import OrganizationConfigRule as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("config_OrganizationConformancePack.yaml"), reason="Skipping Test for compatability reason")
def test_config_OrganizationConformancePack_yaml():
    data = load_yaml_file("config_OrganizationConformancePack.yaml")

    from tropoloco.model.config import OrganizationConformancePack as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("config_OrganizationConformancePack.json"), reason="Skipping Test for compatability reason")
def test_config_OrganizationConformancePack_json():
    data = load_json_file("config_OrganizationConformancePack.json")

    from tropoloco.model.config import OrganizationConformancePack as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("config_RemediationConfiguration.yaml"), reason="Skipping Test for compatability reason")
def test_config_RemediationConfiguration_yaml():
    data = load_yaml_file("config_RemediationConfiguration.yaml")

    from tropoloco.model.config import RemediationConfiguration as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("config_RemediationConfiguration.json"), reason="Skipping Test for compatability reason")
def test_config_RemediationConfiguration_json():
    data = load_json_file("config_RemediationConfiguration.json")

    from tropoloco.model.config import RemediationConfiguration as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("controltower_EnabledControl.yaml"), reason="Skipping Test for compatability reason")
def test_controltower_EnabledControl_yaml():
    data = load_yaml_file("controltower_EnabledControl.yaml")

    from tropoloco.model.controltower import EnabledControl as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("controltower_EnabledControl.json"), reason="Skipping Test for compatability reason")
def test_controltower_EnabledControl_json():
    data = load_json_file("controltower_EnabledControl.json")

    from tropoloco.model.controltower import EnabledControl as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("customerprofiles_Domain.yaml"), reason="Skipping Test for compatability reason")
def test_customerprofiles_Domain_yaml():
    data = load_yaml_file("customerprofiles_Domain.yaml")

    from tropoloco.model.customerprofiles import Domain as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("customerprofiles_Domain.json"), reason="Skipping Test for compatability reason")
def test_customerprofiles_Domain_json():
    data = load_json_file("customerprofiles_Domain.json")

    from tropoloco.model.customerprofiles import Domain as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("customerprofiles_ObjectType.yaml"), reason="Skipping Test for compatability reason")
def test_customerprofiles_ObjectType_yaml():
    data = load_yaml_file("customerprofiles_ObjectType.yaml")

    from tropoloco.model.customerprofiles import ObjectType as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("customerprofiles_ObjectType.json"), reason="Skipping Test for compatability reason")
def test_customerprofiles_ObjectType_json():
    data = load_json_file("customerprofiles_ObjectType.json")

    from tropoloco.model.customerprofiles import ObjectType as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("dlm_LifecyclePolicy.yaml"), reason="Skipping Test for compatability reason")
def test_dlm_LifecyclePolicy_yaml():
    data = load_yaml_file("dlm_LifecyclePolicy.yaml")

    from tropoloco.model.dlm import LifecyclePolicy as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("dlm_LifecyclePolicy.json"), reason="Skipping Test for compatability reason")
def test_dlm_LifecyclePolicy_json():
    data = load_json_file("dlm_LifecyclePolicy.json")

    from tropoloco.model.dlm import LifecyclePolicy as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("dms_Certificate.yaml"), reason="Skipping Test for compatability reason")
def test_dms_Certificate_yaml():
    data = load_yaml_file("dms_Certificate.yaml")

    from tropoloco.model.dms import Certificate as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("dms_Certificate.json"), reason="Skipping Test for compatability reason")
def test_dms_Certificate_json():
    data = load_json_file("dms_Certificate.json")

    from tropoloco.model.dms import Certificate as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("dms_Endpoint.yaml"), reason="Skipping Test for compatability reason")
def test_dms_Endpoint_yaml():
    data = load_yaml_file("dms_Endpoint.yaml")

    from tropoloco.model.dms import Endpoint as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("dms_Endpoint.json"), reason="Skipping Test for compatability reason")
def test_dms_Endpoint_json():
    data = load_json_file("dms_Endpoint.json")

    from tropoloco.model.dms import Endpoint as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("dms_EventSubscription.yaml"), reason="Skipping Test for compatability reason")
def test_dms_EventSubscription_yaml():
    data = load_yaml_file("dms_EventSubscription.yaml")

    from tropoloco.model.dms import EventSubscription as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("dms_EventSubscription.json"), reason="Skipping Test for compatability reason")
def test_dms_EventSubscription_json():
    data = load_json_file("dms_EventSubscription.json")

    from tropoloco.model.dms import EventSubscription as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("dms_ReplicationInstance.yaml"), reason="Skipping Test for compatability reason")
def test_dms_ReplicationInstance_yaml():
    data = load_yaml_file("dms_ReplicationInstance.yaml")

    from tropoloco.model.dms import ReplicationInstance as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("dms_ReplicationInstance.json"), reason="Skipping Test for compatability reason")
def test_dms_ReplicationInstance_json():
    data = load_json_file("dms_ReplicationInstance.json")

    from tropoloco.model.dms import ReplicationInstance as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("dms_ReplicationSubnetGroup.yaml"), reason="Skipping Test for compatability reason")
def test_dms_ReplicationSubnetGroup_yaml():
    data = load_yaml_file("dms_ReplicationSubnetGroup.yaml")

    from tropoloco.model.dms import ReplicationSubnetGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("dms_ReplicationSubnetGroup.json"), reason="Skipping Test for compatability reason")
def test_dms_ReplicationSubnetGroup_json():
    data = load_json_file("dms_ReplicationSubnetGroup.json")

    from tropoloco.model.dms import ReplicationSubnetGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("dms_ReplicationTask.yaml"), reason="Skipping Test for compatability reason")
def test_dms_ReplicationTask_yaml():
    data = load_yaml_file("dms_ReplicationTask.yaml")

    from tropoloco.model.dms import ReplicationTask as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("dms_ReplicationTask.json"), reason="Skipping Test for compatability reason")
def test_dms_ReplicationTask_json():
    data = load_json_file("dms_ReplicationTask.json")

    from tropoloco.model.dms import ReplicationTask as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("databrew_Project.yaml"), reason="Skipping Test for compatability reason")
def test_databrew_Project_yaml():
    data = load_yaml_file("databrew_Project.yaml")

    from tropoloco.model.databrew import Project as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("databrew_Project.json"), reason="Skipping Test for compatability reason")
def test_databrew_Project_json():
    data = load_json_file("databrew_Project.json")

    from tropoloco.model.databrew import Project as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("databrew_Recipe.yaml"), reason="Skipping Test for compatability reason")
def test_databrew_Recipe_yaml():
    data = load_yaml_file("databrew_Recipe.yaml")

    from tropoloco.model.databrew import Recipe as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("databrew_Recipe.json"), reason="Skipping Test for compatability reason")
def test_databrew_Recipe_json():
    data = load_json_file("databrew_Recipe.json")

    from tropoloco.model.databrew import Recipe as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("databrew_Schedule.yaml"), reason="Skipping Test for compatability reason")
def test_databrew_Schedule_yaml():
    data = load_yaml_file("databrew_Schedule.yaml")

    from tropoloco.model.databrew import Schedule as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("databrew_Schedule.json"), reason="Skipping Test for compatability reason")
def test_databrew_Schedule_json():
    data = load_json_file("databrew_Schedule.json")

    from tropoloco.model.databrew import Schedule as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("datapipeline_Pipeline.yaml"), reason="Skipping Test for compatability reason")
def test_datapipeline_Pipeline_yaml():
    data = load_yaml_file("datapipeline_Pipeline.yaml")

    from tropoloco.model.datapipeline import Pipeline as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("datapipeline_Pipeline.json"), reason="Skipping Test for compatability reason")
def test_datapipeline_Pipeline_json():
    data = load_json_file("datapipeline_Pipeline.json")

    from tropoloco.model.datapipeline import Pipeline as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("datasync_Agent.yaml"), reason="Skipping Test for compatability reason")
def test_datasync_Agent_yaml():
    data = load_yaml_file("datasync_Agent.yaml")

    from tropoloco.model.datasync import Agent as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("datasync_Agent.json"), reason="Skipping Test for compatability reason")
def test_datasync_Agent_json():
    data = load_json_file("datasync_Agent.json")

    from tropoloco.model.datasync import Agent as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("datasync_LocationFSxLustre.yaml"), reason="Skipping Test for compatability reason")
def test_datasync_LocationFSxLustre_yaml():
    data = load_yaml_file("datasync_LocationFSxLustre.yaml")

    from tropoloco.model.datasync import LocationFSxLustre as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("datasync_LocationFSxLustre.json"), reason="Skipping Test for compatability reason")
def test_datasync_LocationFSxLustre_json():
    data = load_json_file("datasync_LocationFSxLustre.json")

    from tropoloco.model.datasync import LocationFSxLustre as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("datasync_LocationFSxOpenZFS.yaml"), reason="Skipping Test for compatability reason")
def test_datasync_LocationFSxOpenZFS_yaml():
    data = load_yaml_file("datasync_LocationFSxOpenZFS.yaml")

    from tropoloco.model.datasync import LocationFSxOpenZFS as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("datasync_LocationFSxOpenZFS.json"), reason="Skipping Test for compatability reason")
def test_datasync_LocationFSxOpenZFS_json():
    data = load_json_file("datasync_LocationFSxOpenZFS.json")

    from tropoloco.model.datasync import LocationFSxOpenZFS as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("datasync_LocationNFS.yaml"), reason="Skipping Test for compatability reason")
def test_datasync_LocationNFS_yaml():
    data = load_yaml_file("datasync_LocationNFS.yaml")

    from tropoloco.model.datasync import LocationNFS as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("datasync_LocationNFS.json"), reason="Skipping Test for compatability reason")
def test_datasync_LocationNFS_json():
    data = load_json_file("datasync_LocationNFS.json")

    from tropoloco.model.datasync import LocationNFS as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("datasync_LocationS3.yaml"), reason="Skipping Test for compatability reason")
def test_datasync_LocationS3_yaml():
    data = load_yaml_file("datasync_LocationS3.yaml")

    from tropoloco.model.datasync import LocationS3 as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("datasync_LocationS3.json"), reason="Skipping Test for compatability reason")
def test_datasync_LocationS3_json():
    data = load_json_file("datasync_LocationS3.json")

    from tropoloco.model.datasync import LocationS3 as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("datasync_StorageSystem.yaml"), reason="Skipping Test for compatability reason")
def test_datasync_StorageSystem_yaml():
    data = load_yaml_file("datasync_StorageSystem.yaml")

    from tropoloco.model.datasync import StorageSystem as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("datasync_StorageSystem.json"), reason="Skipping Test for compatability reason")
def test_datasync_StorageSystem_json():
    data = load_json_file("datasync_StorageSystem.json")

    from tropoloco.model.datasync import StorageSystem as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("datasync_Task.yaml"), reason="Skipping Test for compatability reason")
def test_datasync_Task_yaml():
    data = load_yaml_file("datasync_Task.yaml")

    from tropoloco.model.datasync import Task as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("datasync_Task.json"), reason="Skipping Test for compatability reason")
def test_datasync_Task_json():
    data = load_json_file("datasync_Task.json")

    from tropoloco.model.datasync import Task as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("detective_MemberInvitation.yaml"), reason="Skipping Test for compatability reason")
def test_detective_MemberInvitation_yaml():
    data = load_yaml_file("detective_MemberInvitation.yaml")

    from tropoloco.model.detective import MemberInvitation as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("detective_MemberInvitation.json"), reason="Skipping Test for compatability reason")
def test_detective_MemberInvitation_json():
    data = load_json_file("detective_MemberInvitation.json")

    from tropoloco.model.detective import MemberInvitation as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("detective_OrganizationAdmin.yaml"), reason="Skipping Test for compatability reason")
def test_detective_OrganizationAdmin_yaml():
    data = load_yaml_file("detective_OrganizationAdmin.yaml")

    from tropoloco.model.detective import OrganizationAdmin as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("detective_OrganizationAdmin.json"), reason="Skipping Test for compatability reason")
def test_detective_OrganizationAdmin_json():
    data = load_json_file("detective_OrganizationAdmin.json")

    from tropoloco.model.detective import OrganizationAdmin as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("devopsguru_NotificationChannel.yaml"), reason="Skipping Test for compatability reason")
def test_devopsguru_NotificationChannel_yaml():
    data = load_yaml_file("devopsguru_NotificationChannel.yaml")

    from tropoloco.model.devopsguru import NotificationChannel as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("devopsguru_NotificationChannel.json"), reason="Skipping Test for compatability reason")
def test_devopsguru_NotificationChannel_json():
    data = load_json_file("devopsguru_NotificationChannel.json")

    from tropoloco.model.devopsguru import NotificationChannel as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("devopsguru_ResourceCollection.yaml"), reason="Skipping Test for compatability reason")
def test_devopsguru_ResourceCollection_yaml():
    data = load_yaml_file("devopsguru_ResourceCollection.yaml")

    from tropoloco.model.devopsguru import ResourceCollection as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("devopsguru_ResourceCollection.json"), reason="Skipping Test for compatability reason")
def test_devopsguru_ResourceCollection_json():
    data = load_json_file("devopsguru_ResourceCollection.json")

    from tropoloco.model.devopsguru import ResourceCollection as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("directoryservice_MicrosoftAD.yaml"), reason="Skipping Test for compatability reason")
def test_directoryservice_MicrosoftAD_yaml():
    data = load_yaml_file("directoryservice_MicrosoftAD.yaml")

    from tropoloco.model.directoryservice import MicrosoftAD as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("directoryservice_MicrosoftAD.json"), reason="Skipping Test for compatability reason")
def test_directoryservice_MicrosoftAD_json():
    data = load_json_file("directoryservice_MicrosoftAD.json")

    from tropoloco.model.directoryservice import MicrosoftAD as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("directoryservice_SimpleAD.yaml"), reason="Skipping Test for compatability reason")
def test_directoryservice_SimpleAD_yaml():
    data = load_yaml_file("directoryservice_SimpleAD.yaml")

    from tropoloco.model.directoryservice import SimpleAD as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("directoryservice_SimpleAD.json"), reason="Skipping Test for compatability reason")
def test_directoryservice_SimpleAD_json():
    data = load_json_file("directoryservice_SimpleAD.json")

    from tropoloco.model.directoryservice import SimpleAD as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("docdb_DBCluster.yaml"), reason="Skipping Test for compatability reason")
def test_docdb_DBCluster_yaml():
    data = load_yaml_file("docdb_DBCluster.yaml")

    from tropoloco.model.docdb import DBCluster as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("docdb_DBCluster.json"), reason="Skipping Test for compatability reason")
def test_docdb_DBCluster_json():
    data = load_json_file("docdb_DBCluster.json")

    from tropoloco.model.docdb import DBCluster as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("docdb_DBInstance.yaml"), reason="Skipping Test for compatability reason")
def test_docdb_DBInstance_yaml():
    data = load_yaml_file("docdb_DBInstance.yaml")

    from tropoloco.model.docdb import DBInstance as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("docdb_DBInstance.json"), reason="Skipping Test for compatability reason")
def test_docdb_DBInstance_json():
    data = load_json_file("docdb_DBInstance.json")

    from tropoloco.model.docdb import DBInstance as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("docdb_DBSubnetGroup.yaml"), reason="Skipping Test for compatability reason")
def test_docdb_DBSubnetGroup_yaml():
    data = load_yaml_file("docdb_DBSubnetGroup.yaml")

    from tropoloco.model.docdb import DBSubnetGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("docdb_DBSubnetGroup.json"), reason="Skipping Test for compatability reason")
def test_docdb_DBSubnetGroup_json():
    data = load_json_file("docdb_DBSubnetGroup.json")

    from tropoloco.model.docdb import DBSubnetGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_ClientVpnAuthorizationRule.yaml"), reason="Skipping Test for compatability reason")
def test_ec2_ClientVpnAuthorizationRule_yaml():
    data = load_yaml_file("ec2_ClientVpnAuthorizationRule.yaml")

    from tropoloco.model.ec2 import ClientVpnAuthorizationRule as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_ClientVpnAuthorizationRule.json"), reason="Skipping Test for compatability reason")
def test_ec2_ClientVpnAuthorizationRule_json():
    data = load_json_file("ec2_ClientVpnAuthorizationRule.json")

    from tropoloco.model.ec2 import ClientVpnAuthorizationRule as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_ClientVpnEndpoint.yaml"), reason="Skipping Test for compatability reason")
def test_ec2_ClientVpnEndpoint_yaml():
    data = load_yaml_file("ec2_ClientVpnEndpoint.yaml")

    from tropoloco.model.ec2 import ClientVpnEndpoint as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_ClientVpnEndpoint.json"), reason="Skipping Test for compatability reason")
def test_ec2_ClientVpnEndpoint_json():
    data = load_json_file("ec2_ClientVpnEndpoint.json")

    from tropoloco.model.ec2 import ClientVpnEndpoint as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_ClientVpnRoute.yaml"), reason="Skipping Test for compatability reason")
def test_ec2_ClientVpnRoute_yaml():
    data = load_yaml_file("ec2_ClientVpnRoute.yaml")

    from tropoloco.model.ec2 import ClientVpnRoute as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_ClientVpnRoute.json"), reason="Skipping Test for compatability reason")
def test_ec2_ClientVpnRoute_json():
    data = load_json_file("ec2_ClientVpnRoute.json")

    from tropoloco.model.ec2 import ClientVpnRoute as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_ClientVpnTargetNetworkAssociation.yaml"), reason="Skipping Test for compatability reason")
def test_ec2_ClientVpnTargetNetworkAssociation_yaml():
    data = load_yaml_file("ec2_ClientVpnTargetNetworkAssociation.yaml")

    from tropoloco.model.ec2 import ClientVpnTargetNetworkAssociation as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_ClientVpnTargetNetworkAssociation.json"), reason="Skipping Test for compatability reason")
def test_ec2_ClientVpnTargetNetworkAssociation_json():
    data = load_json_file("ec2_ClientVpnTargetNetworkAssociation.json")

    from tropoloco.model.ec2 import ClientVpnTargetNetworkAssociation as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_CustomerGateway.yaml"), reason="Skipping Test for compatability reason")
def test_ec2_CustomerGateway_yaml():
    data = load_yaml_file("ec2_CustomerGateway.yaml")

    from tropoloco.model.ec2 import CustomerGateway as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_CustomerGateway.json"), reason="Skipping Test for compatability reason")
def test_ec2_CustomerGateway_json():
    data = load_json_file("ec2_CustomerGateway.json")

    from tropoloco.model.ec2 import CustomerGateway as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_DHCPOptions.yaml"), reason="Skipping Test for compatability reason")
def test_ec2_DHCPOptions_yaml():
    data = load_yaml_file("ec2_DHCPOptions.yaml")

    from tropoloco.model.ec2 import DHCPOptions as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_DHCPOptions.json"), reason="Skipping Test for compatability reason")
def test_ec2_DHCPOptions_json():
    data = load_json_file("ec2_DHCPOptions.json")

    from tropoloco.model.ec2 import DHCPOptions as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_EgressOnlyInternetGateway.yaml"), reason="Skipping Test for compatability reason")
def test_ec2_EgressOnlyInternetGateway_yaml():
    data = load_yaml_file("ec2_EgressOnlyInternetGateway.yaml")

    from tropoloco.model.ec2 import EgressOnlyInternetGateway as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_EgressOnlyInternetGateway.json"), reason="Skipping Test for compatability reason")
def test_ec2_EgressOnlyInternetGateway_json():
    data = load_json_file("ec2_EgressOnlyInternetGateway.json")

    from tropoloco.model.ec2 import EgressOnlyInternetGateway as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_EnclaveCertificateIamRoleAssociation.yaml"), reason="Skipping Test for compatability reason")
def test_ec2_EnclaveCertificateIamRoleAssociation_yaml():
    data = load_yaml_file("ec2_EnclaveCertificateIamRoleAssociation.yaml")

    from tropoloco.model.ec2 import EnclaveCertificateIamRoleAssociation as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_EnclaveCertificateIamRoleAssociation.json"), reason="Skipping Test for compatability reason")
def test_ec2_EnclaveCertificateIamRoleAssociation_json():
    data = load_json_file("ec2_EnclaveCertificateIamRoleAssociation.json")

    from tropoloco.model.ec2 import EnclaveCertificateIamRoleAssociation as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_Host.yaml"), reason="Skipping Test for compatability reason")
def test_ec2_Host_yaml():
    data = load_yaml_file("ec2_Host.yaml")

    from tropoloco.model.ec2 import Host as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_Host.json"), reason="Skipping Test for compatability reason")
def test_ec2_Host_json():
    data = load_json_file("ec2_Host.json")

    from tropoloco.model.ec2 import Host as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_Instance.yaml"), reason="Skipping Test for compatability reason")
def test_ec2_Instance_yaml():
    data = load_yaml_file("ec2_Instance.yaml")

    from tropoloco.model.ec2 import Instance as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_Instance.json"), reason="Skipping Test for compatability reason")
def test_ec2_Instance_json():
    data = load_json_file("ec2_Instance.json")

    from tropoloco.model.ec2 import Instance as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_InternetGateway.yaml"), reason="Skipping Test for compatability reason")
def test_ec2_InternetGateway_yaml():
    data = load_yaml_file("ec2_InternetGateway.yaml")

    from tropoloco.model.ec2 import InternetGateway as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_InternetGateway.json"), reason="Skipping Test for compatability reason")
def test_ec2_InternetGateway_json():
    data = load_json_file("ec2_InternetGateway.json")

    from tropoloco.model.ec2 import InternetGateway as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_KeyPair.yaml"), reason="Skipping Test for compatability reason")
def test_ec2_KeyPair_yaml():
    data = load_yaml_file("ec2_KeyPair.yaml")

    from tropoloco.model.ec2 import KeyPair as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_KeyPair.json"), reason="Skipping Test for compatability reason")
def test_ec2_KeyPair_json():
    data = load_json_file("ec2_KeyPair.json")

    from tropoloco.model.ec2 import KeyPair as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_NetworkAcl.yaml"), reason="Skipping Test for compatability reason")
def test_ec2_NetworkAcl_yaml():
    data = load_yaml_file("ec2_NetworkAcl.yaml")

    from tropoloco.model.ec2 import NetworkAcl as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_NetworkAcl.json"), reason="Skipping Test for compatability reason")
def test_ec2_NetworkAcl_json():
    data = load_json_file("ec2_NetworkAcl.json")

    from tropoloco.model.ec2 import NetworkAcl as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_NetworkAclEntry.yaml"), reason="Skipping Test for compatability reason")
def test_ec2_NetworkAclEntry_yaml():
    data = load_yaml_file("ec2_NetworkAclEntry.yaml")

    from tropoloco.model.ec2 import NetworkAclEntry as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_NetworkAclEntry.json"), reason="Skipping Test for compatability reason")
def test_ec2_NetworkAclEntry_json():
    data = load_json_file("ec2_NetworkAclEntry.json")

    from tropoloco.model.ec2 import NetworkAclEntry as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_NetworkInterfaceAttachment.yaml"), reason="Skipping Test for compatability reason")
def test_ec2_NetworkInterfaceAttachment_yaml():
    data = load_yaml_file("ec2_NetworkInterfaceAttachment.yaml")

    from tropoloco.model.ec2 import NetworkInterfaceAttachment as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_NetworkInterfaceAttachment.json"), reason="Skipping Test for compatability reason")
def test_ec2_NetworkInterfaceAttachment_json():
    data = load_json_file("ec2_NetworkInterfaceAttachment.json")

    from tropoloco.model.ec2 import NetworkInterfaceAttachment as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_NetworkInterfacePermission.yaml"), reason="Skipping Test for compatability reason")
def test_ec2_NetworkInterfacePermission_yaml():
    data = load_yaml_file("ec2_NetworkInterfacePermission.yaml")

    from tropoloco.model.ec2 import NetworkInterfacePermission as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_NetworkInterfacePermission.json"), reason="Skipping Test for compatability reason")
def test_ec2_NetworkInterfacePermission_json():
    data = load_json_file("ec2_NetworkInterfacePermission.json")

    from tropoloco.model.ec2 import NetworkInterfacePermission as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_PrefixList.yaml"), reason="Skipping Test for compatability reason")
def test_ec2_PrefixList_yaml():
    data = load_yaml_file("ec2_PrefixList.yaml")

    from tropoloco.model.ec2 import PrefixList as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_PrefixList.json"), reason="Skipping Test for compatability reason")
def test_ec2_PrefixList_json():
    data = load_json_file("ec2_PrefixList.json")

    from tropoloco.model.ec2 import PrefixList as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_Route.yaml"), reason="Skipping Test for compatability reason")
def test_ec2_Route_yaml():
    data = load_yaml_file("ec2_Route.yaml")

    from tropoloco.model.ec2 import Route as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_Route.json"), reason="Skipping Test for compatability reason")
def test_ec2_Route_json():
    data = load_json_file("ec2_Route.json")

    from tropoloco.model.ec2 import Route as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_RouteTable.yaml"), reason="Skipping Test for compatability reason")
def test_ec2_RouteTable_yaml():
    data = load_yaml_file("ec2_RouteTable.yaml")

    from tropoloco.model.ec2 import RouteTable as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_RouteTable.json"), reason="Skipping Test for compatability reason")
def test_ec2_RouteTable_json():
    data = load_json_file("ec2_RouteTable.json")

    from tropoloco.model.ec2 import RouteTable as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_SecurityGroupEgress.yaml"), reason="Skipping Test for compatability reason")
def test_ec2_SecurityGroupEgress_yaml():
    data = load_yaml_file("ec2_SecurityGroupEgress.yaml")

    from tropoloco.model.ec2 import SecurityGroupEgress as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_SecurityGroupEgress.json"), reason="Skipping Test for compatability reason")
def test_ec2_SecurityGroupEgress_json():
    data = load_json_file("ec2_SecurityGroupEgress.json")

    from tropoloco.model.ec2 import SecurityGroupEgress as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_Subnet.yaml"), reason="Skipping Test for compatability reason")
def test_ec2_Subnet_yaml():
    data = load_yaml_file("ec2_Subnet.yaml")

    from tropoloco.model.ec2 import Subnet as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_Subnet.json"), reason="Skipping Test for compatability reason")
def test_ec2_Subnet_json():
    data = load_json_file("ec2_Subnet.json")

    from tropoloco.model.ec2 import Subnet as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_SubnetNetworkAclAssociation.yaml"), reason="Skipping Test for compatability reason")
def test_ec2_SubnetNetworkAclAssociation_yaml():
    data = load_yaml_file("ec2_SubnetNetworkAclAssociation.yaml")

    from tropoloco.model.ec2 import SubnetNetworkAclAssociation as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_SubnetNetworkAclAssociation.json"), reason="Skipping Test for compatability reason")
def test_ec2_SubnetNetworkAclAssociation_json():
    data = load_json_file("ec2_SubnetNetworkAclAssociation.json")

    from tropoloco.model.ec2 import SubnetNetworkAclAssociation as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_SubnetRouteTableAssociation.yaml"), reason="Skipping Test for compatability reason")
def test_ec2_SubnetRouteTableAssociation_yaml():
    data = load_yaml_file("ec2_SubnetRouteTableAssociation.yaml")

    from tropoloco.model.ec2 import SubnetRouteTableAssociation as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_SubnetRouteTableAssociation.json"), reason="Skipping Test for compatability reason")
def test_ec2_SubnetRouteTableAssociation_json():
    data = load_json_file("ec2_SubnetRouteTableAssociation.json")

    from tropoloco.model.ec2 import SubnetRouteTableAssociation as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_TrafficMirrorFilter.yaml"), reason="Skipping Test for compatability reason")
def test_ec2_TrafficMirrorFilter_yaml():
    data = load_yaml_file("ec2_TrafficMirrorFilter.yaml")

    from tropoloco.model.ec2 import TrafficMirrorFilter as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_TrafficMirrorFilter.json"), reason="Skipping Test for compatability reason")
def test_ec2_TrafficMirrorFilter_json():
    data = load_json_file("ec2_TrafficMirrorFilter.json")

    from tropoloco.model.ec2 import TrafficMirrorFilter as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_TrafficMirrorFilterRule.yaml"), reason="Skipping Test for compatability reason")
def test_ec2_TrafficMirrorFilterRule_yaml():
    data = load_yaml_file("ec2_TrafficMirrorFilterRule.yaml")

    from tropoloco.model.ec2 import TrafficMirrorFilterRule as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_TrafficMirrorFilterRule.json"), reason="Skipping Test for compatability reason")
def test_ec2_TrafficMirrorFilterRule_json():
    data = load_json_file("ec2_TrafficMirrorFilterRule.json")

    from tropoloco.model.ec2 import TrafficMirrorFilterRule as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_TrafficMirrorSession.yaml"), reason="Skipping Test for compatability reason")
def test_ec2_TrafficMirrorSession_yaml():
    data = load_yaml_file("ec2_TrafficMirrorSession.yaml")

    from tropoloco.model.ec2 import TrafficMirrorSession as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_TrafficMirrorSession.json"), reason="Skipping Test for compatability reason")
def test_ec2_TrafficMirrorSession_json():
    data = load_json_file("ec2_TrafficMirrorSession.json")

    from tropoloco.model.ec2 import TrafficMirrorSession as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_TrafficMirrorTarget.yaml"), reason="Skipping Test for compatability reason")
def test_ec2_TrafficMirrorTarget_yaml():
    data = load_yaml_file("ec2_TrafficMirrorTarget.yaml")

    from tropoloco.model.ec2 import TrafficMirrorTarget as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_TrafficMirrorTarget.json"), reason="Skipping Test for compatability reason")
def test_ec2_TrafficMirrorTarget_json():
    data = load_json_file("ec2_TrafficMirrorTarget.json")

    from tropoloco.model.ec2 import TrafficMirrorTarget as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_VPC.yaml"), reason="Skipping Test for compatability reason")
def test_ec2_VPC_yaml():
    data = load_yaml_file("ec2_VPC.yaml")

    from tropoloco.model.ec2 import VPC as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_VPC.json"), reason="Skipping Test for compatability reason")
def test_ec2_VPC_json():
    data = load_json_file("ec2_VPC.json")

    from tropoloco.model.ec2 import VPC as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_VPCDHCPOptionsAssociation.yaml"), reason="Skipping Test for compatability reason")
def test_ec2_VPCDHCPOptionsAssociation_yaml():
    data = load_yaml_file("ec2_VPCDHCPOptionsAssociation.yaml")

    from tropoloco.model.ec2 import VPCDHCPOptionsAssociation as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_VPCDHCPOptionsAssociation.json"), reason="Skipping Test for compatability reason")
def test_ec2_VPCDHCPOptionsAssociation_json():
    data = load_json_file("ec2_VPCDHCPOptionsAssociation.json")

    from tropoloco.model.ec2 import VPCDHCPOptionsAssociation as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_VPCGatewayAttachment.yaml"), reason="Skipping Test for compatability reason")
def test_ec2_VPCGatewayAttachment_yaml():
    data = load_yaml_file("ec2_VPCGatewayAttachment.yaml")

    from tropoloco.model.ec2 import VPCGatewayAttachment as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_VPCGatewayAttachment.json"), reason="Skipping Test for compatability reason")
def test_ec2_VPCGatewayAttachment_json():
    data = load_json_file("ec2_VPCGatewayAttachment.json")

    from tropoloco.model.ec2 import VPCGatewayAttachment as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_VPNGateway.yaml"), reason="Skipping Test for compatability reason")
def test_ec2_VPNGateway_yaml():
    data = load_yaml_file("ec2_VPNGateway.yaml")

    from tropoloco.model.ec2 import VPNGateway as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ec2_VPNGateway.json"), reason="Skipping Test for compatability reason")
def test_ec2_VPNGateway_json():
    data = load_json_file("ec2_VPNGateway.json")

    from tropoloco.model.ec2 import VPNGateway as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ecr_PublicRepository.yaml"), reason="Skipping Test for compatability reason")
def test_ecr_PublicRepository_yaml():
    data = load_yaml_file("ecr_PublicRepository.yaml")

    from tropoloco.model.ecr import PublicRepository as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ecr_PublicRepository.json"), reason="Skipping Test for compatability reason")
def test_ecr_PublicRepository_json():
    data = load_json_file("ecr_PublicRepository.json")

    from tropoloco.model.ecr import PublicRepository as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ecr_PullThroughCacheRule.yaml"), reason="Skipping Test for compatability reason")
def test_ecr_PullThroughCacheRule_yaml():
    data = load_yaml_file("ecr_PullThroughCacheRule.yaml")

    from tropoloco.model.ecr import PullThroughCacheRule as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ecr_PullThroughCacheRule.json"), reason="Skipping Test for compatability reason")
def test_ecr_PullThroughCacheRule_json():
    data = load_json_file("ecr_PullThroughCacheRule.json")

    from tropoloco.model.ecr import PullThroughCacheRule as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ecr_RegistryPolicy.yaml"), reason="Skipping Test for compatability reason")
def test_ecr_RegistryPolicy_yaml():
    data = load_yaml_file("ecr_RegistryPolicy.yaml")

    from tropoloco.model.ecr import RegistryPolicy as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ecr_RegistryPolicy.json"), reason="Skipping Test for compatability reason")
def test_ecr_RegistryPolicy_json():
    data = load_json_file("ecr_RegistryPolicy.json")

    from tropoloco.model.ecr import RegistryPolicy as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ecr_ReplicationConfiguration.yaml"), reason="Skipping Test for compatability reason")
def test_ecr_ReplicationConfiguration_yaml():
    data = load_yaml_file("ecr_ReplicationConfiguration.yaml")

    from tropoloco.model.ecr import ReplicationConfiguration as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ecr_ReplicationConfiguration.json"), reason="Skipping Test for compatability reason")
def test_ecr_ReplicationConfiguration_json():
    data = load_json_file("ecr_ReplicationConfiguration.json")

    from tropoloco.model.ecr import ReplicationConfiguration as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ecs_CapacityProvider.yaml"), reason="Skipping Test for compatability reason")
def test_ecs_CapacityProvider_yaml():
    data = load_yaml_file("ecs_CapacityProvider.yaml")

    from tropoloco.model.ecs import CapacityProvider as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ecs_CapacityProvider.json"), reason="Skipping Test for compatability reason")
def test_ecs_CapacityProvider_json():
    data = load_json_file("ecs_CapacityProvider.json")

    from tropoloco.model.ecs import CapacityProvider as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ecs_Cluster.yaml"), reason="Skipping Test for compatability reason")
def test_ecs_Cluster_yaml():
    data = load_yaml_file("ecs_Cluster.yaml")

    from tropoloco.model.ecs import Cluster as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ecs_Cluster.json"), reason="Skipping Test for compatability reason")
def test_ecs_Cluster_json():
    data = load_json_file("ecs_Cluster.json")

    from tropoloco.model.ecs import Cluster as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ecs_Service.yaml"), reason="Skipping Test for compatability reason")
def test_ecs_Service_yaml():
    data = load_yaml_file("ecs_Service.yaml")

    from tropoloco.model.ecs import Service as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ecs_Service.json"), reason="Skipping Test for compatability reason")
def test_ecs_Service_json():
    data = load_json_file("ecs_Service.json")

    from tropoloco.model.ecs import Service as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("efs_MountTarget.yaml"), reason="Skipping Test for compatability reason")
def test_efs_MountTarget_yaml():
    data = load_yaml_file("efs_MountTarget.yaml")

    from tropoloco.model.efs import MountTarget as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("efs_MountTarget.json"), reason="Skipping Test for compatability reason")
def test_efs_MountTarget_json():
    data = load_json_file("efs_MountTarget.json")

    from tropoloco.model.efs import MountTarget as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("eks_Cluster.yaml"), reason="Skipping Test for compatability reason")
def test_eks_Cluster_yaml():
    data = load_yaml_file("eks_Cluster.yaml")

    from tropoloco.model.eks import Cluster as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("eks_Cluster.json"), reason="Skipping Test for compatability reason")
def test_eks_Cluster_json():
    data = load_json_file("eks_Cluster.json")

    from tropoloco.model.eks import Cluster as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("eks_FargateProfile.yaml"), reason="Skipping Test for compatability reason")
def test_eks_FargateProfile_yaml():
    data = load_yaml_file("eks_FargateProfile.yaml")

    from tropoloco.model.eks import FargateProfile as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("eks_FargateProfile.json"), reason="Skipping Test for compatability reason")
def test_eks_FargateProfile_json():
    data = load_json_file("eks_FargateProfile.json")

    from tropoloco.model.eks import FargateProfile as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("eks_IdentityProviderConfig.yaml"), reason="Skipping Test for compatability reason")
def test_eks_IdentityProviderConfig_yaml():
    data = load_yaml_file("eks_IdentityProviderConfig.yaml")

    from tropoloco.model.eks import IdentityProviderConfig as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("eks_IdentityProviderConfig.json"), reason="Skipping Test for compatability reason")
def test_eks_IdentityProviderConfig_json():
    data = load_json_file("eks_IdentityProviderConfig.json")

    from tropoloco.model.eks import IdentityProviderConfig as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("eks_Nodegroup.yaml"), reason="Skipping Test for compatability reason")
def test_eks_Nodegroup_yaml():
    data = load_yaml_file("eks_Nodegroup.yaml")

    from tropoloco.model.eks import Nodegroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("eks_Nodegroup.json"), reason="Skipping Test for compatability reason")
def test_eks_Nodegroup_json():
    data = load_json_file("eks_Nodegroup.json")

    from tropoloco.model.eks import Nodegroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("elasticache_CacheCluster.yaml"), reason="Skipping Test for compatability reason")
def test_elasticache_CacheCluster_yaml():
    data = load_yaml_file("elasticache_CacheCluster.yaml")

    from tropoloco.model.elasticache import CacheCluster as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("elasticache_CacheCluster.json"), reason="Skipping Test for compatability reason")
def test_elasticache_CacheCluster_json():
    data = load_json_file("elasticache_CacheCluster.json")

    from tropoloco.model.elasticache import CacheCluster as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("elasticache_ParameterGroup.yaml"), reason="Skipping Test for compatability reason")
def test_elasticache_ParameterGroup_yaml():
    data = load_yaml_file("elasticache_ParameterGroup.yaml")

    from tropoloco.model.elasticache import ParameterGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("elasticache_ParameterGroup.json"), reason="Skipping Test for compatability reason")
def test_elasticache_ParameterGroup_json():
    data = load_json_file("elasticache_ParameterGroup.json")

    from tropoloco.model.elasticache import ParameterGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("elasticbeanstalk_Application.yaml"), reason="Skipping Test for compatability reason")
def test_elasticbeanstalk_Application_yaml():
    data = load_yaml_file("elasticbeanstalk_Application.yaml")

    from tropoloco.model.elasticbeanstalk import Application as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("elasticbeanstalk_Application.json"), reason="Skipping Test for compatability reason")
def test_elasticbeanstalk_Application_json():
    data = load_json_file("elasticbeanstalk_Application.json")

    from tropoloco.model.elasticbeanstalk import Application as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("elasticbeanstalk_ApplicationVersion.yaml"), reason="Skipping Test for compatability reason")
def test_elasticbeanstalk_ApplicationVersion_yaml():
    data = load_yaml_file("elasticbeanstalk_ApplicationVersion.yaml")

    from tropoloco.model.elasticbeanstalk import ApplicationVersion as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("elasticbeanstalk_ApplicationVersion.json"), reason="Skipping Test for compatability reason")
def test_elasticbeanstalk_ApplicationVersion_json():
    data = load_json_file("elasticbeanstalk_ApplicationVersion.json")

    from tropoloco.model.elasticbeanstalk import ApplicationVersion as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("elasticbeanstalk_ConfigurationTemplate.yaml"), reason="Skipping Test for compatability reason")
def test_elasticbeanstalk_ConfigurationTemplate_yaml():
    data = load_yaml_file("elasticbeanstalk_ConfigurationTemplate.yaml")

    from tropoloco.model.elasticbeanstalk import ConfigurationTemplate as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("elasticbeanstalk_ConfigurationTemplate.json"), reason="Skipping Test for compatability reason")
def test_elasticbeanstalk_ConfigurationTemplate_json():
    data = load_json_file("elasticbeanstalk_ConfigurationTemplate.json")

    from tropoloco.model.elasticbeanstalk import ConfigurationTemplate as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("elasticloadbalancing_LoadBalancer.yaml"), reason="Skipping Test for compatability reason")
def test_elasticloadbalancing_LoadBalancer_yaml():
    data = load_yaml_file("elasticloadbalancing_LoadBalancer.yaml")

    from tropoloco.model.elasticloadbalancing import LoadBalancer as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("elasticloadbalancing_LoadBalancer.json"), reason="Skipping Test for compatability reason")
def test_elasticloadbalancing_LoadBalancer_json():
    data = load_json_file("elasticloadbalancing_LoadBalancer.json")

    from tropoloco.model.elasticloadbalancing import LoadBalancer as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("elasticsearch_Domain.yaml"), reason="Skipping Test for compatability reason")
def test_elasticsearch_Domain_yaml():
    data = load_yaml_file("elasticsearch_Domain.yaml")

    from tropoloco.model.elasticsearch import Domain as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("elasticsearch_Domain.json"), reason="Skipping Test for compatability reason")
def test_elasticsearch_Domain_json():
    data = load_json_file("elasticsearch_Domain.json")

    from tropoloco.model.elasticsearch import Domain as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("eventschemas_RegistryPolicy.yaml"), reason="Skipping Test for compatability reason")
def test_eventschemas_RegistryPolicy_yaml():
    data = load_yaml_file("eventschemas_RegistryPolicy.yaml")

    from tropoloco.model.eventschemas import RegistryPolicy as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("eventschemas_RegistryPolicy.json"), reason="Skipping Test for compatability reason")
def test_eventschemas_RegistryPolicy_json():
    data = load_json_file("eventschemas_RegistryPolicy.json")

    from tropoloco.model.eventschemas import RegistryPolicy as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("events_EventBus.yaml"), reason="Skipping Test for compatability reason")
def test_events_EventBus_yaml():
    data = load_yaml_file("events_EventBus.yaml")

    from tropoloco.model.events import EventBus as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("events_EventBus.json"), reason="Skipping Test for compatability reason")
def test_events_EventBus_json():
    data = load_json_file("events_EventBus.json")

    from tropoloco.model.events import EventBus as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("fsx_FileSystem.yaml"), reason="Skipping Test for compatability reason")
def test_fsx_FileSystem_yaml():
    data = load_yaml_file("fsx_FileSystem.yaml")

    from tropoloco.model.fsx import FileSystem as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("fsx_FileSystem.json"), reason="Skipping Test for compatability reason")
def test_fsx_FileSystem_json():
    data = load_json_file("fsx_FileSystem.json")

    from tropoloco.model.fsx import FileSystem as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("finspace_Environment.yaml"), reason="Skipping Test for compatability reason")
def test_finspace_Environment_yaml():
    data = load_yaml_file("finspace_Environment.yaml")

    from tropoloco.model.finspace import Environment as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("finspace_Environment.json"), reason="Skipping Test for compatability reason")
def test_finspace_Environment_json():
    data = load_json_file("finspace_Environment.json")

    from tropoloco.model.finspace import Environment as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("gamelift_Alias.yaml"), reason="Skipping Test for compatability reason")
def test_gamelift_Alias_yaml():
    data = load_yaml_file("gamelift_Alias.yaml")

    from tropoloco.model.gamelift import Alias as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("gamelift_Alias.json"), reason="Skipping Test for compatability reason")
def test_gamelift_Alias_json():
    data = load_json_file("gamelift_Alias.json")

    from tropoloco.model.gamelift import Alias as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("gamelift_GameSessionQueue.yaml"), reason="Skipping Test for compatability reason")
def test_gamelift_GameSessionQueue_yaml():
    data = load_yaml_file("gamelift_GameSessionQueue.yaml")

    from tropoloco.model.gamelift import GameSessionQueue as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("gamelift_GameSessionQueue.json"), reason="Skipping Test for compatability reason")
def test_gamelift_GameSessionQueue_json():
    data = load_json_file("gamelift_GameSessionQueue.json")

    from tropoloco.model.gamelift import GameSessionQueue as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("globalaccelerator_Accelerator.yaml"), reason="Skipping Test for compatability reason")
def test_globalaccelerator_Accelerator_yaml():
    data = load_yaml_file("globalaccelerator_Accelerator.yaml")

    from tropoloco.model.globalaccelerator import Accelerator as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("globalaccelerator_Accelerator.json"), reason="Skipping Test for compatability reason")
def test_globalaccelerator_Accelerator_json():
    data = load_json_file("globalaccelerator_Accelerator.json")

    from tropoloco.model.globalaccelerator import Accelerator as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("globalaccelerator_EndpointGroup.yaml"), reason="Skipping Test for compatability reason")
def test_globalaccelerator_EndpointGroup_yaml():
    data = load_yaml_file("globalaccelerator_EndpointGroup.yaml")

    from tropoloco.model.globalaccelerator import EndpointGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("globalaccelerator_EndpointGroup.json"), reason="Skipping Test for compatability reason")
def test_globalaccelerator_EndpointGroup_json():
    data = load_json_file("globalaccelerator_EndpointGroup.json")

    from tropoloco.model.globalaccelerator import EndpointGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("globalaccelerator_Listener.yaml"), reason="Skipping Test for compatability reason")
def test_globalaccelerator_Listener_yaml():
    data = load_yaml_file("globalaccelerator_Listener.yaml")

    from tropoloco.model.globalaccelerator import Listener as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("globalaccelerator_Listener.json"), reason="Skipping Test for compatability reason")
def test_globalaccelerator_Listener_json():
    data = load_json_file("globalaccelerator_Listener.json")

    from tropoloco.model.globalaccelerator import Listener as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("glue_Crawler.yaml"), reason="Skipping Test for compatability reason")
def test_glue_Crawler_yaml():
    data = load_yaml_file("glue_Crawler.yaml")

    from tropoloco.model.glue import Crawler as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("glue_Crawler.json"), reason="Skipping Test for compatability reason")
def test_glue_Crawler_json():
    data = load_json_file("glue_Crawler.json")

    from tropoloco.model.glue import Crawler as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("greengrass_LoggerDefinition.yaml"), reason="Skipping Test for compatability reason")
def test_greengrass_LoggerDefinition_yaml():
    data = load_yaml_file("greengrass_LoggerDefinition.yaml")

    from tropoloco.model.greengrass import LoggerDefinition as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("greengrass_LoggerDefinition.json"), reason="Skipping Test for compatability reason")
def test_greengrass_LoggerDefinition_json():
    data = load_json_file("greengrass_LoggerDefinition.json")

    from tropoloco.model.greengrass import LoggerDefinition as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("groundstation_DataflowEndpointGroup.yaml"), reason="Skipping Test for compatability reason")
def test_groundstation_DataflowEndpointGroup_yaml():
    data = load_yaml_file("groundstation_DataflowEndpointGroup.yaml")

    from tropoloco.model.groundstation import DataflowEndpointGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("groundstation_DataflowEndpointGroup.json"), reason="Skipping Test for compatability reason")
def test_groundstation_DataflowEndpointGroup_json():
    data = load_json_file("groundstation_DataflowEndpointGroup.json")

    from tropoloco.model.groundstation import DataflowEndpointGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("groundstation_MissionProfile.yaml"), reason="Skipping Test for compatability reason")
def test_groundstation_MissionProfile_yaml():
    data = load_yaml_file("groundstation_MissionProfile.yaml")

    from tropoloco.model.groundstation import MissionProfile as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("groundstation_MissionProfile.json"), reason="Skipping Test for compatability reason")
def test_groundstation_MissionProfile_json():
    data = load_json_file("groundstation_MissionProfile.json")

    from tropoloco.model.groundstation import MissionProfile as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("guardduty_Master.yaml"), reason="Skipping Test for compatability reason")
def test_guardduty_Master_yaml():
    data = load_yaml_file("guardduty_Master.yaml")

    from tropoloco.model.guardduty import Master as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("guardduty_Master.json"), reason="Skipping Test for compatability reason")
def test_guardduty_Master_json():
    data = load_json_file("guardduty_Master.json")

    from tropoloco.model.guardduty import Master as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("guardduty_Member.yaml"), reason="Skipping Test for compatability reason")
def test_guardduty_Member_yaml():
    data = load_yaml_file("guardduty_Member.yaml")

    from tropoloco.model.guardduty import Member as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("guardduty_Member.json"), reason="Skipping Test for compatability reason")
def test_guardduty_Member_json():
    data = load_json_file("guardduty_Member.json")

    from tropoloco.model.guardduty import Member as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("guardduty_ThreatIntelSet.yaml"), reason="Skipping Test for compatability reason")
def test_guardduty_ThreatIntelSet_yaml():
    data = load_yaml_file("guardduty_ThreatIntelSet.yaml")

    from tropoloco.model.guardduty import ThreatIntelSet as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("guardduty_ThreatIntelSet.json"), reason="Skipping Test for compatability reason")
def test_guardduty_ThreatIntelSet_json():
    data = load_json_file("guardduty_ThreatIntelSet.json")

    from tropoloco.model.guardduty import ThreatIntelSet as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("iam_InstanceProfile.yaml"), reason="Skipping Test for compatability reason")
def test_iam_InstanceProfile_yaml():
    data = load_yaml_file("iam_InstanceProfile.yaml")

    from tropoloco.model.iam import InstanceProfile as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("iam_InstanceProfile.json"), reason="Skipping Test for compatability reason")
def test_iam_InstanceProfile_json():
    data = load_json_file("iam_InstanceProfile.json")

    from tropoloco.model.iam import InstanceProfile as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("iam_Role.yaml"), reason="Skipping Test for compatability reason")
def test_iam_Role_yaml():
    data = load_yaml_file("iam_Role.yaml")

    from tropoloco.model.iam import Role as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("iam_Role.json"), reason="Skipping Test for compatability reason")
def test_iam_Role_json():
    data = load_json_file("iam_Role.json")

    from tropoloco.model.iam import Role as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("imagebuilder_Component.yaml"), reason="Skipping Test for compatability reason")
def test_imagebuilder_Component_yaml():
    data = load_yaml_file("imagebuilder_Component.yaml")

    from tropoloco.model.imagebuilder import Component as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("imagebuilder_Component.json"), reason="Skipping Test for compatability reason")
def test_imagebuilder_Component_json():
    data = load_json_file("imagebuilder_Component.json")

    from tropoloco.model.imagebuilder import Component as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("imagebuilder_DistributionConfiguration.yaml"), reason="Skipping Test for compatability reason")
def test_imagebuilder_DistributionConfiguration_yaml():
    data = load_yaml_file("imagebuilder_DistributionConfiguration.yaml")

    from tropoloco.model.imagebuilder import DistributionConfiguration as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("imagebuilder_DistributionConfiguration.json"), reason="Skipping Test for compatability reason")
def test_imagebuilder_DistributionConfiguration_json():
    data = load_json_file("imagebuilder_DistributionConfiguration.json")

    from tropoloco.model.imagebuilder import DistributionConfiguration as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("inspector_AssessmentTarget.yaml"), reason="Skipping Test for compatability reason")
def test_inspector_AssessmentTarget_yaml():
    data = load_yaml_file("inspector_AssessmentTarget.yaml")

    from tropoloco.model.inspector import AssessmentTarget as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("inspector_AssessmentTarget.json"), reason="Skipping Test for compatability reason")
def test_inspector_AssessmentTarget_json():
    data = load_json_file("inspector_AssessmentTarget.json")

    from tropoloco.model.inspector import AssessmentTarget as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("inspector_AssessmentTemplate.yaml"), reason="Skipping Test for compatability reason")
def test_inspector_AssessmentTemplate_yaml():
    data = load_yaml_file("inspector_AssessmentTemplate.yaml")

    from tropoloco.model.inspector import AssessmentTemplate as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("inspector_AssessmentTemplate.json"), reason="Skipping Test for compatability reason")
def test_inspector_AssessmentTemplate_json():
    data = load_json_file("inspector_AssessmentTemplate.json")

    from tropoloco.model.inspector import AssessmentTemplate as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("inspector_ResourceGroup.yaml"), reason="Skipping Test for compatability reason")
def test_inspector_ResourceGroup_yaml():
    data = load_yaml_file("inspector_ResourceGroup.yaml")

    from tropoloco.model.inspector import ResourceGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("inspector_ResourceGroup.json"), reason="Skipping Test for compatability reason")
def test_inspector_ResourceGroup_json():
    data = load_json_file("inspector_ResourceGroup.json")

    from tropoloco.model.inspector import ResourceGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("iot1click_Device.yaml"), reason="Skipping Test for compatability reason")
def test_iot1click_Device_yaml():
    data = load_yaml_file("iot1click_Device.yaml")

    from tropoloco.model.iot1click import Device as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("iot1click_Device.json"), reason="Skipping Test for compatability reason")
def test_iot1click_Device_json():
    data = load_json_file("iot1click_Device.json")

    from tropoloco.model.iot1click import Device as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("iotanalytics_Channel.yaml"), reason="Skipping Test for compatability reason")
def test_iotanalytics_Channel_yaml():
    data = load_yaml_file("iotanalytics_Channel.yaml")

    from tropoloco.model.iotanalytics import Channel as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("iotanalytics_Channel.json"), reason="Skipping Test for compatability reason")
def test_iotanalytics_Channel_json():
    data = load_json_file("iotanalytics_Channel.json")

    from tropoloco.model.iotanalytics import Channel as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("iotanalytics_Dataset.yaml"), reason="Skipping Test for compatability reason")
def test_iotanalytics_Dataset_yaml():
    data = load_yaml_file("iotanalytics_Dataset.yaml")

    from tropoloco.model.iotanalytics import Dataset as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("iotanalytics_Dataset.json"), reason="Skipping Test for compatability reason")
def test_iotanalytics_Dataset_json():
    data = load_json_file("iotanalytics_Dataset.json")

    from tropoloco.model.iotanalytics import Dataset as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("iotanalytics_Datastore.yaml"), reason="Skipping Test for compatability reason")
def test_iotanalytics_Datastore_yaml():
    data = load_yaml_file("iotanalytics_Datastore.yaml")

    from tropoloco.model.iotanalytics import Datastore as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("iotanalytics_Datastore.json"), reason="Skipping Test for compatability reason")
def test_iotanalytics_Datastore_json():
    data = load_json_file("iotanalytics_Datastore.json")

    from tropoloco.model.iotanalytics import Datastore as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("iotanalytics_Pipeline.yaml"), reason="Skipping Test for compatability reason")
def test_iotanalytics_Pipeline_yaml():
    data = load_yaml_file("iotanalytics_Pipeline.yaml")

    from tropoloco.model.iotanalytics import Pipeline as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("iotanalytics_Pipeline.json"), reason="Skipping Test for compatability reason")
def test_iotanalytics_Pipeline_json():
    data = load_json_file("iotanalytics_Pipeline.json")

    from tropoloco.model.iotanalytics import Pipeline as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("iotcoredeviceadvisor_SuiteDefinition.yaml"), reason="Skipping Test for compatability reason")
def test_iotcoredeviceadvisor_SuiteDefinition_yaml():
    data = load_yaml_file("iotcoredeviceadvisor_SuiteDefinition.yaml")

    from tropoloco.model.iotcoredeviceadvisor import SuiteDefinition as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("iotcoredeviceadvisor_SuiteDefinition.json"), reason="Skipping Test for compatability reason")
def test_iotcoredeviceadvisor_SuiteDefinition_json():
    data = load_json_file("iotcoredeviceadvisor_SuiteDefinition.json")

    from tropoloco.model.iotcoredeviceadvisor import SuiteDefinition as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("iotevents_Input.yaml"), reason="Skipping Test for compatability reason")
def test_iotevents_Input_yaml():
    data = load_yaml_file("iotevents_Input.yaml")

    from tropoloco.model.iotevents import Input as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("iotevents_Input.json"), reason="Skipping Test for compatability reason")
def test_iotevents_Input_json():
    data = load_json_file("iotevents_Input.json")

    from tropoloco.model.iotevents import Input as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("kms_Key.yaml"), reason="Skipping Test for compatability reason")
def test_kms_Key_yaml():
    data = load_yaml_file("kms_Key.yaml")

    from tropoloco.model.kms import Key as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("kms_Key.json"), reason="Skipping Test for compatability reason")
def test_kms_Key_json():
    data = load_json_file("kms_Key.json")

    from tropoloco.model.kms import Key as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("kms_ReplicaKey.yaml"), reason="Skipping Test for compatability reason")
def test_kms_ReplicaKey_yaml():
    data = load_yaml_file("kms_ReplicaKey.yaml")

    from tropoloco.model.kms import ReplicaKey as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("kms_ReplicaKey.json"), reason="Skipping Test for compatability reason")
def test_kms_ReplicaKey_json():
    data = load_json_file("kms_ReplicaKey.json")

    from tropoloco.model.kms import ReplicaKey as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("kinesisanalyticsv2_ApplicationCloudWatchLoggingOption.yaml"), reason="Skipping Test for compatability reason")
def test_kinesisanalyticsv2_ApplicationCloudWatchLoggingOption_yaml():
    data = load_yaml_file("kinesisanalyticsv2_ApplicationCloudWatchLoggingOption.yaml")

    from tropoloco.model.kinesisanalyticsv2 import ApplicationCloudWatchLoggingOption as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("kinesisanalyticsv2_ApplicationCloudWatchLoggingOption.json"), reason="Skipping Test for compatability reason")
def test_kinesisanalyticsv2_ApplicationCloudWatchLoggingOption_json():
    data = load_json_file("kinesisanalyticsv2_ApplicationCloudWatchLoggingOption.json")

    from tropoloco.model.kinesisanalyticsv2 import ApplicationCloudWatchLoggingOption as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("kinesisanalyticsv2_ApplicationOutput.yaml"), reason="Skipping Test for compatability reason")
def test_kinesisanalyticsv2_ApplicationOutput_yaml():
    data = load_yaml_file("kinesisanalyticsv2_ApplicationOutput.yaml")

    from tropoloco.model.kinesisanalyticsv2 import ApplicationOutput as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("kinesisanalyticsv2_ApplicationOutput.json"), reason="Skipping Test for compatability reason")
def test_kinesisanalyticsv2_ApplicationOutput_json():
    data = load_json_file("kinesisanalyticsv2_ApplicationOutput.json")

    from tropoloco.model.kinesisanalyticsv2 import ApplicationOutput as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("kinesisanalyticsv2_ApplicationReferenceDataSource.yaml"), reason="Skipping Test for compatability reason")
def test_kinesisanalyticsv2_ApplicationReferenceDataSource_yaml():
    data = load_yaml_file("kinesisanalyticsv2_ApplicationReferenceDataSource.yaml")

    from tropoloco.model.kinesisanalyticsv2 import ApplicationReferenceDataSource as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("kinesisanalyticsv2_ApplicationReferenceDataSource.json"), reason="Skipping Test for compatability reason")
def test_kinesisanalyticsv2_ApplicationReferenceDataSource_json():
    data = load_json_file("kinesisanalyticsv2_ApplicationReferenceDataSource.json")

    from tropoloco.model.kinesisanalyticsv2 import ApplicationReferenceDataSource as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("lakeformation_DataCellsFilter.yaml"), reason="Skipping Test for compatability reason")
def test_lakeformation_DataCellsFilter_yaml():
    data = load_yaml_file("lakeformation_DataCellsFilter.yaml")

    from tropoloco.model.lakeformation import DataCellsFilter as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("lakeformation_DataCellsFilter.json"), reason="Skipping Test for compatability reason")
def test_lakeformation_DataCellsFilter_json():
    data = load_json_file("lakeformation_DataCellsFilter.json")

    from tropoloco.model.lakeformation import DataCellsFilter as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("lakeformation_DataLakeSettings.yaml"), reason="Skipping Test for compatability reason")
def test_lakeformation_DataLakeSettings_yaml():
    data = load_yaml_file("lakeformation_DataLakeSettings.yaml")

    from tropoloco.model.lakeformation import DataLakeSettings as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("lakeformation_DataLakeSettings.json"), reason="Skipping Test for compatability reason")
def test_lakeformation_DataLakeSettings_json():
    data = load_json_file("lakeformation_DataLakeSettings.json")

    from tropoloco.model.lakeformation import DataLakeSettings as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("lakeformation_Tag.yaml"), reason="Skipping Test for compatability reason")
def test_lakeformation_Tag_yaml():
    data = load_yaml_file("lakeformation_Tag.yaml")

    from tropoloco.model.lakeformation import Tag as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("lakeformation_Tag.json"), reason="Skipping Test for compatability reason")
def test_lakeformation_Tag_json():
    data = load_json_file("lakeformation_Tag.json")

    from tropoloco.model.lakeformation import Tag as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("lakeformation_TagAssociation.yaml"), reason="Skipping Test for compatability reason")
def test_lakeformation_TagAssociation_yaml():
    data = load_yaml_file("lakeformation_TagAssociation.yaml")

    from tropoloco.model.lakeformation import TagAssociation as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("lakeformation_TagAssociation.json"), reason="Skipping Test for compatability reason")
def test_lakeformation_TagAssociation_json():
    data = load_json_file("lakeformation_TagAssociation.json")

    from tropoloco.model.lakeformation import TagAssociation as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("awslambda_EventSourceMapping.yaml"), reason="Skipping Test for compatability reason")
def test_awslambda_EventSourceMapping_yaml():
    data = load_yaml_file("awslambda_EventSourceMapping.yaml")

    from tropoloco.model.awslambda import EventSourceMapping as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("awslambda_EventSourceMapping.json"), reason="Skipping Test for compatability reason")
def test_awslambda_EventSourceMapping_json():
    data = load_json_file("awslambda_EventSourceMapping.json")

    from tropoloco.model.awslambda import EventSourceMapping as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("awslambda_Function.yaml"), reason="Skipping Test for compatability reason")
def test_awslambda_Function_yaml():
    data = load_yaml_file("awslambda_Function.yaml")

    from tropoloco.model.awslambda import Function as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("awslambda_Function.json"), reason="Skipping Test for compatability reason")
def test_awslambda_Function_json():
    data = load_json_file("awslambda_Function.json")

    from tropoloco.model.awslambda import Function as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("awslambda_LayerVersion.yaml"), reason="Skipping Test for compatability reason")
def test_awslambda_LayerVersion_yaml():
    data = load_yaml_file("awslambda_LayerVersion.yaml")

    from tropoloco.model.awslambda import LayerVersion as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("awslambda_LayerVersion.json"), reason="Skipping Test for compatability reason")
def test_awslambda_LayerVersion_json():
    data = load_json_file("awslambda_LayerVersion.json")

    from tropoloco.model.awslambda import LayerVersion as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("logs_AccountPolicy.yaml"), reason="Skipping Test for compatability reason")
def test_logs_AccountPolicy_yaml():
    data = load_yaml_file("logs_AccountPolicy.yaml")

    from tropoloco.model.logs import AccountPolicy as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("logs_AccountPolicy.json"), reason="Skipping Test for compatability reason")
def test_logs_AccountPolicy_json():
    data = load_json_file("logs_AccountPolicy.json")

    from tropoloco.model.logs import AccountPolicy as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("logs_Destination.yaml"), reason="Skipping Test for compatability reason")
def test_logs_Destination_yaml():
    data = load_yaml_file("logs_Destination.yaml")

    from tropoloco.model.logs import Destination as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("logs_Destination.json"), reason="Skipping Test for compatability reason")
def test_logs_Destination_json():
    data = load_json_file("logs_Destination.json")

    from tropoloco.model.logs import Destination as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("logs_LogGroup.yaml"), reason="Skipping Test for compatability reason")
def test_logs_LogGroup_yaml():
    data = load_yaml_file("logs_LogGroup.yaml")

    from tropoloco.model.logs import LogGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("logs_LogGroup.json"), reason="Skipping Test for compatability reason")
def test_logs_LogGroup_json():
    data = load_json_file("logs_LogGroup.json")

    from tropoloco.model.logs import LogGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("logs_LogStream.yaml"), reason="Skipping Test for compatability reason")
def test_logs_LogStream_yaml():
    data = load_yaml_file("logs_LogStream.yaml")

    from tropoloco.model.logs import LogStream as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("logs_LogStream.json"), reason="Skipping Test for compatability reason")
def test_logs_LogStream_json():
    data = load_json_file("logs_LogStream.json")

    from tropoloco.model.logs import LogStream as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("logs_MetricFilter.yaml"), reason="Skipping Test for compatability reason")
def test_logs_MetricFilter_yaml():
    data = load_yaml_file("logs_MetricFilter.yaml")

    from tropoloco.model.logs import MetricFilter as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("logs_MetricFilter.json"), reason="Skipping Test for compatability reason")
def test_logs_MetricFilter_json():
    data = load_json_file("logs_MetricFilter.json")

    from tropoloco.model.logs import MetricFilter as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("logs_ResourcePolicy.yaml"), reason="Skipping Test for compatability reason")
def test_logs_ResourcePolicy_yaml():
    data = load_yaml_file("logs_ResourcePolicy.yaml")

    from tropoloco.model.logs import ResourcePolicy as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("logs_ResourcePolicy.json"), reason="Skipping Test for compatability reason")
def test_logs_ResourcePolicy_json():
    data = load_json_file("logs_ResourcePolicy.json")

    from tropoloco.model.logs import ResourcePolicy as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("mwaa_Environment.yaml"), reason="Skipping Test for compatability reason")
def test_mwaa_Environment_yaml():
    data = load_yaml_file("mwaa_Environment.yaml")

    from tropoloco.model.mwaa import Environment as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("mwaa_Environment.json"), reason="Skipping Test for compatability reason")
def test_mwaa_Environment_json():
    data = load_json_file("mwaa_Environment.json")

    from tropoloco.model.mwaa import Environment as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("macie_AllowList.yaml"), reason="Skipping Test for compatability reason")
def test_macie_AllowList_yaml():
    data = load_yaml_file("macie_AllowList.yaml")

    from tropoloco.model.macie import AllowList as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("macie_AllowList.json"), reason="Skipping Test for compatability reason")
def test_macie_AllowList_json():
    data = load_json_file("macie_AllowList.json")

    from tropoloco.model.macie import AllowList as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("macie_CustomDataIdentifier.yaml"), reason="Skipping Test for compatability reason")
def test_macie_CustomDataIdentifier_yaml():
    data = load_yaml_file("macie_CustomDataIdentifier.yaml")

    from tropoloco.model.macie import CustomDataIdentifier as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("macie_CustomDataIdentifier.json"), reason="Skipping Test for compatability reason")
def test_macie_CustomDataIdentifier_json():
    data = load_json_file("macie_CustomDataIdentifier.json")

    from tropoloco.model.macie import CustomDataIdentifier as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("macie_FindingsFilter.yaml"), reason="Skipping Test for compatability reason")
def test_macie_FindingsFilter_yaml():
    data = load_yaml_file("macie_FindingsFilter.yaml")

    from tropoloco.model.macie import FindingsFilter as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("macie_FindingsFilter.json"), reason="Skipping Test for compatability reason")
def test_macie_FindingsFilter_json():
    data = load_json_file("macie_FindingsFilter.json")

    from tropoloco.model.macie import FindingsFilter as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("macie_Session.yaml"), reason="Skipping Test for compatability reason")
def test_macie_Session_yaml():
    data = load_yaml_file("macie_Session.yaml")

    from tropoloco.model.macie import Session as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("macie_Session.json"), reason="Skipping Test for compatability reason")
def test_macie_Session_json():
    data = load_json_file("macie_Session.json")

    from tropoloco.model.macie import Session as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("networkfirewall_RuleGroup.yaml"), reason="Skipping Test for compatability reason")
def test_networkfirewall_RuleGroup_yaml():
    data = load_yaml_file("networkfirewall_RuleGroup.yaml")

    from tropoloco.model.networkfirewall import RuleGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("networkfirewall_RuleGroup.json"), reason="Skipping Test for compatability reason")
def test_networkfirewall_RuleGroup_json():
    data = load_json_file("networkfirewall_RuleGroup.json")

    from tropoloco.model.networkfirewall import RuleGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("networkmanager_GlobalNetwork.yaml"), reason="Skipping Test for compatability reason")
def test_networkmanager_GlobalNetwork_yaml():
    data = load_yaml_file("networkmanager_GlobalNetwork.yaml")

    from tropoloco.model.networkmanager import GlobalNetwork as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("networkmanager_GlobalNetwork.json"), reason="Skipping Test for compatability reason")
def test_networkmanager_GlobalNetwork_json():
    data = load_json_file("networkmanager_GlobalNetwork.json")

    from tropoloco.model.networkmanager import GlobalNetwork as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("opensearchserverless_Collection.yaml"), reason="Skipping Test for compatability reason")
def test_opensearchserverless_Collection_yaml():
    data = load_yaml_file("opensearchserverless_Collection.yaml")

    from tropoloco.model.opensearchserverless import Collection as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("opensearchserverless_Collection.json"), reason="Skipping Test for compatability reason")
def test_opensearchserverless_Collection_json():
    data = load_json_file("opensearchserverless_Collection.json")

    from tropoloco.model.opensearchserverless import Collection as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("opensearchserverless_SecurityConfig.yaml"), reason="Skipping Test for compatability reason")
def test_opensearchserverless_SecurityConfig_yaml():
    data = load_yaml_file("opensearchserverless_SecurityConfig.yaml")

    from tropoloco.model.opensearchserverless import SecurityConfig as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("opensearchserverless_SecurityConfig.json"), reason="Skipping Test for compatability reason")
def test_opensearchserverless_SecurityConfig_json():
    data = load_json_file("opensearchserverless_SecurityConfig.json")

    from tropoloco.model.opensearchserverless import SecurityConfig as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("opensearchserverless_SecurityPolicy.yaml"), reason="Skipping Test for compatability reason")
def test_opensearchserverless_SecurityPolicy_yaml():
    data = load_yaml_file("opensearchserverless_SecurityPolicy.yaml")

    from tropoloco.model.opensearchserverless import SecurityPolicy as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("opensearchserverless_SecurityPolicy.json"), reason="Skipping Test for compatability reason")
def test_opensearchserverless_SecurityPolicy_json():
    data = load_json_file("opensearchserverless_SecurityPolicy.json")

    from tropoloco.model.opensearchserverless import SecurityPolicy as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("opensearchserverless_VpcEndpoint.yaml"), reason="Skipping Test for compatability reason")
def test_opensearchserverless_VpcEndpoint_yaml():
    data = load_yaml_file("opensearchserverless_VpcEndpoint.yaml")

    from tropoloco.model.opensearchserverless import VpcEndpoint as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("opensearchserverless_VpcEndpoint.json"), reason="Skipping Test for compatability reason")
def test_opensearchserverless_VpcEndpoint_json():
    data = load_json_file("opensearchserverless_VpcEndpoint.json")

    from tropoloco.model.opensearchserverless import VpcEndpoint as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("opensearchservice_Domain.yaml"), reason="Skipping Test for compatability reason")
def test_opensearchservice_Domain_yaml():
    data = load_yaml_file("opensearchservice_Domain.yaml")

    from tropoloco.model.opensearchservice import Domain as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("opensearchservice_Domain.json"), reason="Skipping Test for compatability reason")
def test_opensearchservice_Domain_json():
    data = load_json_file("opensearchservice_Domain.json")

    from tropoloco.model.opensearchservice import Domain as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("opsworks_App.yaml"), reason="Skipping Test for compatability reason")
def test_opsworks_App_yaml():
    data = load_yaml_file("opsworks_App.yaml")

    from tropoloco.model.opsworks import App as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("opsworks_App.json"), reason="Skipping Test for compatability reason")
def test_opsworks_App_json():
    data = load_json_file("opsworks_App.json")

    from tropoloco.model.opsworks import App as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("opsworks_ElasticLoadBalancerAttachment.yaml"), reason="Skipping Test for compatability reason")
def test_opsworks_ElasticLoadBalancerAttachment_yaml():
    data = load_yaml_file("opsworks_ElasticLoadBalancerAttachment.yaml")

    from tropoloco.model.opsworks import ElasticLoadBalancerAttachment as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("opsworks_ElasticLoadBalancerAttachment.json"), reason="Skipping Test for compatability reason")
def test_opsworks_ElasticLoadBalancerAttachment_json():
    data = load_json_file("opsworks_ElasticLoadBalancerAttachment.json")

    from tropoloco.model.opsworks import ElasticLoadBalancerAttachment as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("opsworks_Instance.yaml"), reason="Skipping Test for compatability reason")
def test_opsworks_Instance_yaml():
    data = load_yaml_file("opsworks_Instance.yaml")

    from tropoloco.model.opsworks import Instance as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("opsworks_Instance.json"), reason="Skipping Test for compatability reason")
def test_opsworks_Instance_json():
    data = load_json_file("opsworks_Instance.json")

    from tropoloco.model.opsworks import Instance as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("organizations_Organization.yaml"), reason="Skipping Test for compatability reason")
def test_organizations_Organization_yaml():
    data = load_yaml_file("organizations_Organization.yaml")

    from tropoloco.model.organizations import Organization as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("organizations_Organization.json"), reason="Skipping Test for compatability reason")
def test_organizations_Organization_json():
    data = load_json_file("organizations_Organization.json")

    from tropoloco.model.organizations import Organization as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("organizations_Policy.yaml"), reason="Skipping Test for compatability reason")
def test_organizations_Policy_yaml():
    data = load_yaml_file("organizations_Policy.yaml")

    from tropoloco.model.organizations import Policy as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("organizations_Policy.json"), reason="Skipping Test for compatability reason")
def test_organizations_Policy_json():
    data = load_json_file("organizations_Policy.json")

    from tropoloco.model.organizations import Policy as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("organizations_ResourcePolicy.yaml"), reason="Skipping Test for compatability reason")
def test_organizations_ResourcePolicy_yaml():
    data = load_yaml_file("organizations_ResourcePolicy.yaml")

    from tropoloco.model.organizations import ResourcePolicy as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("organizations_ResourcePolicy.json"), reason="Skipping Test for compatability reason")
def test_organizations_ResourcePolicy_json():
    data = load_json_file("organizations_ResourcePolicy.json")

    from tropoloco.model.organizations import ResourcePolicy as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("personalize_Dataset.yaml"), reason="Skipping Test for compatability reason")
def test_personalize_Dataset_yaml():
    data = load_yaml_file("personalize_Dataset.yaml")

    from tropoloco.model.personalize import Dataset as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("personalize_Dataset.json"), reason="Skipping Test for compatability reason")
def test_personalize_Dataset_json():
    data = load_json_file("personalize_Dataset.json")

    from tropoloco.model.personalize import Dataset as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("personalize_DatasetGroup.yaml"), reason="Skipping Test for compatability reason")
def test_personalize_DatasetGroup_yaml():
    data = load_yaml_file("personalize_DatasetGroup.yaml")

    from tropoloco.model.personalize import DatasetGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("personalize_DatasetGroup.json"), reason="Skipping Test for compatability reason")
def test_personalize_DatasetGroup_json():
    data = load_json_file("personalize_DatasetGroup.json")

    from tropoloco.model.personalize import DatasetGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("personalize_Schema.yaml"), reason="Skipping Test for compatability reason")
def test_personalize_Schema_yaml():
    data = load_yaml_file("personalize_Schema.yaml")

    from tropoloco.model.personalize import Schema as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("personalize_Schema.json"), reason="Skipping Test for compatability reason")
def test_personalize_Schema_json():
    data = load_json_file("personalize_Schema.json")

    from tropoloco.model.personalize import Schema as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("personalize_Solution.yaml"), reason="Skipping Test for compatability reason")
def test_personalize_Solution_yaml():
    data = load_yaml_file("personalize_Solution.yaml")

    from tropoloco.model.personalize import Solution as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("personalize_Solution.json"), reason="Skipping Test for compatability reason")
def test_personalize_Solution_json():
    data = load_json_file("personalize_Solution.json")

    from tropoloco.model.personalize import Solution as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("pipes_Pipe.yaml"), reason="Skipping Test for compatability reason")
def test_pipes_Pipe_yaml():
    data = load_yaml_file("pipes_Pipe.yaml")

    from tropoloco.model.pipes import Pipe as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("pipes_Pipe.json"), reason="Skipping Test for compatability reason")
def test_pipes_Pipe_json():
    data = load_json_file("pipes_Pipe.json")

    from tropoloco.model.pipes import Pipe as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("qldb_Ledger.yaml"), reason="Skipping Test for compatability reason")
def test_qldb_Ledger_yaml():
    data = load_yaml_file("qldb_Ledger.yaml")

    from tropoloco.model.qldb import Ledger as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("qldb_Ledger.json"), reason="Skipping Test for compatability reason")
def test_qldb_Ledger_json():
    data = load_json_file("qldb_Ledger.json")

    from tropoloco.model.qldb import Ledger as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("qldb_Stream.yaml"), reason="Skipping Test for compatability reason")
def test_qldb_Stream_yaml():
    data = load_yaml_file("qldb_Stream.yaml")

    from tropoloco.model.qldb import Stream as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("qldb_Stream.json"), reason="Skipping Test for compatability reason")
def test_qldb_Stream_json():
    data = load_json_file("qldb_Stream.json")

    from tropoloco.model.qldb import Stream as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ram_ResourceShare.yaml"), reason="Skipping Test for compatability reason")
def test_ram_ResourceShare_yaml():
    data = load_yaml_file("ram_ResourceShare.yaml")

    from tropoloco.model.ram import ResourceShare as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ram_ResourceShare.json"), reason="Skipping Test for compatability reason")
def test_ram_ResourceShare_json():
    data = load_json_file("ram_ResourceShare.json")

    from tropoloco.model.ram import ResourceShare as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("rds_DBClusterParameterGroup.yaml"), reason="Skipping Test for compatability reason")
def test_rds_DBClusterParameterGroup_yaml():
    data = load_yaml_file("rds_DBClusterParameterGroup.yaml")

    from tropoloco.model.rds import DBClusterParameterGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("rds_DBClusterParameterGroup.json"), reason="Skipping Test for compatability reason")
def test_rds_DBClusterParameterGroup_json():
    data = load_json_file("rds_DBClusterParameterGroup.json")

    from tropoloco.model.rds import DBClusterParameterGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("rds_DBParameterGroup.yaml"), reason="Skipping Test for compatability reason")
def test_rds_DBParameterGroup_yaml():
    data = load_yaml_file("rds_DBParameterGroup.yaml")

    from tropoloco.model.rds import DBParameterGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("rds_DBParameterGroup.json"), reason="Skipping Test for compatability reason")
def test_rds_DBParameterGroup_json():
    data = load_json_file("rds_DBParameterGroup.json")

    from tropoloco.model.rds import DBParameterGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("rds_DBSecurityGroup.yaml"), reason="Skipping Test for compatability reason")
def test_rds_DBSecurityGroup_yaml():
    data = load_yaml_file("rds_DBSecurityGroup.yaml")

    from tropoloco.model.rds import DBSecurityGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("rds_DBSecurityGroup.json"), reason="Skipping Test for compatability reason")
def test_rds_DBSecurityGroup_json():
    data = load_json_file("rds_DBSecurityGroup.json")

    from tropoloco.model.rds import DBSecurityGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("rds_DBSubnetGroup.yaml"), reason="Skipping Test for compatability reason")
def test_rds_DBSubnetGroup_yaml():
    data = load_yaml_file("rds_DBSubnetGroup.yaml")

    from tropoloco.model.rds import DBSubnetGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("rds_DBSubnetGroup.json"), reason="Skipping Test for compatability reason")
def test_rds_DBSubnetGroup_json():
    data = load_json_file("rds_DBSubnetGroup.json")

    from tropoloco.model.rds import DBSubnetGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("rds_OptionGroup.yaml"), reason="Skipping Test for compatability reason")
def test_rds_OptionGroup_yaml():
    data = load_yaml_file("rds_OptionGroup.yaml")

    from tropoloco.model.rds import OptionGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("rds_OptionGroup.json"), reason="Skipping Test for compatability reason")
def test_rds_OptionGroup_json():
    data = load_json_file("rds_OptionGroup.json")

    from tropoloco.model.rds import OptionGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("redshift_ClusterParameterGroup.yaml"), reason="Skipping Test for compatability reason")
def test_redshift_ClusterParameterGroup_yaml():
    data = load_yaml_file("redshift_ClusterParameterGroup.yaml")

    from tropoloco.model.redshift import ClusterParameterGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("redshift_ClusterParameterGroup.json"), reason="Skipping Test for compatability reason")
def test_redshift_ClusterParameterGroup_json():
    data = load_json_file("redshift_ClusterParameterGroup.json")

    from tropoloco.model.redshift import ClusterParameterGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("redshift_ClusterSecurityGroup.yaml"), reason="Skipping Test for compatability reason")
def test_redshift_ClusterSecurityGroup_yaml():
    data = load_yaml_file("redshift_ClusterSecurityGroup.yaml")

    from tropoloco.model.redshift import ClusterSecurityGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("redshift_ClusterSecurityGroup.json"), reason="Skipping Test for compatability reason")
def test_redshift_ClusterSecurityGroup_json():
    data = load_json_file("redshift_ClusterSecurityGroup.json")

    from tropoloco.model.redshift import ClusterSecurityGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("redshift_ClusterSecurityGroupIngress.yaml"), reason="Skipping Test for compatability reason")
def test_redshift_ClusterSecurityGroupIngress_yaml():
    data = load_yaml_file("redshift_ClusterSecurityGroupIngress.yaml")

    from tropoloco.model.redshift import ClusterSecurityGroupIngress as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("redshift_ClusterSecurityGroupIngress.json"), reason="Skipping Test for compatability reason")
def test_redshift_ClusterSecurityGroupIngress_json():
    data = load_json_file("redshift_ClusterSecurityGroupIngress.json")

    from tropoloco.model.redshift import ClusterSecurityGroupIngress as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("redshift_ClusterSubnetGroup.yaml"), reason="Skipping Test for compatability reason")
def test_redshift_ClusterSubnetGroup_yaml():
    data = load_yaml_file("redshift_ClusterSubnetGroup.yaml")

    from tropoloco.model.redshift import ClusterSubnetGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("redshift_ClusterSubnetGroup.json"), reason="Skipping Test for compatability reason")
def test_redshift_ClusterSubnetGroup_json():
    data = load_json_file("redshift_ClusterSubnetGroup.json")

    from tropoloco.model.redshift import ClusterSubnetGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("rekognition_StreamProcessor.yaml"), reason="Skipping Test for compatability reason")
def test_rekognition_StreamProcessor_yaml():
    data = load_yaml_file("rekognition_StreamProcessor.yaml")

    from tropoloco.model.rekognition import StreamProcessor as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("rekognition_StreamProcessor.json"), reason="Skipping Test for compatability reason")
def test_rekognition_StreamProcessor_json():
    data = load_json_file("rekognition_StreamProcessor.json")

    from tropoloco.model.rekognition import StreamProcessor as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("resourceexplorer2_Index.yaml"), reason="Skipping Test for compatability reason")
def test_resourceexplorer2_Index_yaml():
    data = load_yaml_file("resourceexplorer2_Index.yaml")

    from tropoloco.model.resourceexplorer2 import Index as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("resourceexplorer2_Index.json"), reason="Skipping Test for compatability reason")
def test_resourceexplorer2_Index_json():
    data = load_json_file("resourceexplorer2_Index.json")

    from tropoloco.model.resourceexplorer2 import Index as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("resourcegroups_Group.yaml"), reason="Skipping Test for compatability reason")
def test_resourcegroups_Group_yaml():
    data = load_yaml_file("resourcegroups_Group.yaml")

    from tropoloco.model.resourcegroups import Group as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("resourcegroups_Group.json"), reason="Skipping Test for compatability reason")
def test_resourcegroups_Group_json():
    data = load_json_file("resourcegroups_Group.json")

    from tropoloco.model.resourcegroups import Group as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("route53_CidrCollection.yaml"), reason="Skipping Test for compatability reason")
def test_route53_CidrCollection_yaml():
    data = load_yaml_file("route53_CidrCollection.yaml")

    from tropoloco.model.route53 import CidrCollection as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("route53_CidrCollection.json"), reason="Skipping Test for compatability reason")
def test_route53_CidrCollection_json():
    data = load_json_file("route53_CidrCollection.json")

    from tropoloco.model.route53 import CidrCollection as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("route53_HealthCheck.yaml"), reason="Skipping Test for compatability reason")
def test_route53_HealthCheck_yaml():
    data = load_yaml_file("route53_HealthCheck.yaml")

    from tropoloco.model.route53 import HealthCheck as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("route53_HealthCheck.json"), reason="Skipping Test for compatability reason")
def test_route53_HealthCheck_json():
    data = load_json_file("route53_HealthCheck.json")

    from tropoloco.model.route53 import HealthCheck as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("route53_RecordSetGroup.yaml"), reason="Skipping Test for compatability reason")
def test_route53_RecordSetGroup_yaml():
    data = load_yaml_file("route53_RecordSetGroup.yaml")

    from tropoloco.model.route53 import RecordSetGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("route53_RecordSetGroup.json"), reason="Skipping Test for compatability reason")
def test_route53_RecordSetGroup_json():
    data = load_json_file("route53_RecordSetGroup.json")

    from tropoloco.model.route53 import RecordSetGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("route53resolver_OutpostResolver.yaml"), reason="Skipping Test for compatability reason")
def test_route53resolver_OutpostResolver_yaml():
    data = load_yaml_file("route53resolver_OutpostResolver.yaml")

    from tropoloco.model.route53resolver import OutpostResolver as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("route53resolver_OutpostResolver.json"), reason="Skipping Test for compatability reason")
def test_route53resolver_OutpostResolver_json():
    data = load_json_file("route53resolver_OutpostResolver.json")

    from tropoloco.model.route53resolver import OutpostResolver as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("s3_AccessPoint.yaml"), reason="Skipping Test for compatability reason")
def test_s3_AccessPoint_yaml():
    data = load_yaml_file("s3_AccessPoint.yaml")

    from tropoloco.model.s3 import AccessPoint as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("s3_AccessPoint.json"), reason="Skipping Test for compatability reason")
def test_s3_AccessPoint_json():
    data = load_json_file("s3_AccessPoint.json")

    from tropoloco.model.s3 import AccessPoint as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("s3_MultiRegionAccessPointPolicy.yaml"), reason="Skipping Test for compatability reason")
def test_s3_MultiRegionAccessPointPolicy_yaml():
    data = load_yaml_file("s3_MultiRegionAccessPointPolicy.yaml")

    from tropoloco.model.s3 import MultiRegionAccessPointPolicy as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("s3_MultiRegionAccessPointPolicy.json"), reason="Skipping Test for compatability reason")
def test_s3_MultiRegionAccessPointPolicy_json():
    data = load_json_file("s3_MultiRegionAccessPointPolicy.json")

    from tropoloco.model.s3 import MultiRegionAccessPointPolicy as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("s3outposts_AccessPoint.yaml"), reason="Skipping Test for compatability reason")
def test_s3outposts_AccessPoint_yaml():
    data = load_yaml_file("s3outposts_AccessPoint.yaml")

    from tropoloco.model.s3outposts import AccessPoint as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("s3outposts_AccessPoint.json"), reason="Skipping Test for compatability reason")
def test_s3outposts_AccessPoint_json():
    data = load_json_file("s3outposts_AccessPoint.json")

    from tropoloco.model.s3outposts import AccessPoint as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("s3outposts_Bucket.yaml"), reason="Skipping Test for compatability reason")
def test_s3outposts_Bucket_yaml():
    data = load_yaml_file("s3outposts_Bucket.yaml")

    from tropoloco.model.s3outposts import Bucket as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("s3outposts_Bucket.json"), reason="Skipping Test for compatability reason")
def test_s3outposts_Bucket_json():
    data = load_json_file("s3outposts_Bucket.json")

    from tropoloco.model.s3outposts import Bucket as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("s3outposts_Endpoint.yaml"), reason="Skipping Test for compatability reason")
def test_s3outposts_Endpoint_yaml():
    data = load_yaml_file("s3outposts_Endpoint.yaml")

    from tropoloco.model.s3outposts import Endpoint as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("s3outposts_Endpoint.json"), reason="Skipping Test for compatability reason")
def test_s3outposts_Endpoint_json():
    data = load_json_file("s3outposts_Endpoint.json")

    from tropoloco.model.s3outposts import Endpoint as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("sns_Topic.yaml"), reason="Skipping Test for compatability reason")
def test_sns_Topic_yaml():
    data = load_yaml_file("sns_Topic.yaml")

    from tropoloco.model.sns import Topic as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("sns_Topic.json"), reason="Skipping Test for compatability reason")
def test_sns_Topic_json():
    data = load_json_file("sns_Topic.json")

    from tropoloco.model.sns import Topic as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("sqs_Queue.yaml"), reason="Skipping Test for compatability reason")
def test_sqs_Queue_yaml():
    data = load_yaml_file("sqs_Queue.yaml")

    from tropoloco.model.sqs import Queue as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("sqs_Queue.json"), reason="Skipping Test for compatability reason")
def test_sqs_Queue_json():
    data = load_json_file("sqs_Queue.json")

    from tropoloco.model.sqs import Queue as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("sqs_QueuePolicy.yaml"), reason="Skipping Test for compatability reason")
def test_sqs_QueuePolicy_yaml():
    data = load_yaml_file("sqs_QueuePolicy.yaml")

    from tropoloco.model.sqs import QueuePolicy as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("sqs_QueuePolicy.json"), reason="Skipping Test for compatability reason")
def test_sqs_QueuePolicy_json():
    data = load_json_file("sqs_QueuePolicy.json")

    from tropoloco.model.sqs import QueuePolicy as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ssm_Document.yaml"), reason="Skipping Test for compatability reason")
def test_ssm_Document_yaml():
    data = load_yaml_file("ssm_Document.yaml")

    from tropoloco.model.ssm import Document as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ssm_Document.json"), reason="Skipping Test for compatability reason")
def test_ssm_Document_json():
    data = load_json_file("ssm_Document.json")

    from tropoloco.model.ssm import Document as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ssm_MaintenanceWindow.yaml"), reason="Skipping Test for compatability reason")
def test_ssm_MaintenanceWindow_yaml():
    data = load_yaml_file("ssm_MaintenanceWindow.yaml")

    from tropoloco.model.ssm import MaintenanceWindow as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ssm_MaintenanceWindow.json"), reason="Skipping Test for compatability reason")
def test_ssm_MaintenanceWindow_json():
    data = load_json_file("ssm_MaintenanceWindow.json")

    from tropoloco.model.ssm import MaintenanceWindow as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ssm_MaintenanceWindowTarget.yaml"), reason="Skipping Test for compatability reason")
def test_ssm_MaintenanceWindowTarget_yaml():
    data = load_yaml_file("ssm_MaintenanceWindowTarget.yaml")

    from tropoloco.model.ssm import MaintenanceWindowTarget as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ssm_MaintenanceWindowTarget.json"), reason="Skipping Test for compatability reason")
def test_ssm_MaintenanceWindowTarget_json():
    data = load_json_file("ssm_MaintenanceWindowTarget.json")

    from tropoloco.model.ssm import MaintenanceWindowTarget as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ssm_MaintenanceWindowTask.yaml"), reason="Skipping Test for compatability reason")
def test_ssm_MaintenanceWindowTask_yaml():
    data = load_yaml_file("ssm_MaintenanceWindowTask.yaml")

    from tropoloco.model.ssm import MaintenanceWindowTask as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ssm_MaintenanceWindowTask.json"), reason="Skipping Test for compatability reason")
def test_ssm_MaintenanceWindowTask_json():
    data = load_json_file("ssm_MaintenanceWindowTask.json")

    from tropoloco.model.ssm import MaintenanceWindowTask as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ssm_Parameter.yaml"), reason="Skipping Test for compatability reason")
def test_ssm_Parameter_yaml():
    data = load_yaml_file("ssm_Parameter.yaml")

    from tropoloco.model.ssm import Parameter as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ssm_Parameter.json"), reason="Skipping Test for compatability reason")
def test_ssm_Parameter_json():
    data = load_json_file("ssm_Parameter.json")

    from tropoloco.model.ssm import Parameter as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ssm_ResourceDataSync.yaml"), reason="Skipping Test for compatability reason")
def test_ssm_ResourceDataSync_yaml():
    data = load_yaml_file("ssm_ResourceDataSync.yaml")

    from tropoloco.model.ssm import ResourceDataSync as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ssm_ResourceDataSync.json"), reason="Skipping Test for compatability reason")
def test_ssm_ResourceDataSync_json():
    data = load_json_file("ssm_ResourceDataSync.json")

    from tropoloco.model.ssm import ResourceDataSync as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ssmincidents_ReplicationSet.yaml"), reason="Skipping Test for compatability reason")
def test_ssmincidents_ReplicationSet_yaml():
    data = load_yaml_file("ssmincidents_ReplicationSet.yaml")

    from tropoloco.model.ssmincidents import ReplicationSet as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ssmincidents_ReplicationSet.json"), reason="Skipping Test for compatability reason")
def test_ssmincidents_ReplicationSet_json():
    data = load_json_file("ssmincidents_ReplicationSet.json")

    from tropoloco.model.ssmincidents import ReplicationSet as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ssmincidents_ResponsePlan.yaml"), reason="Skipping Test for compatability reason")
def test_ssmincidents_ResponsePlan_yaml():
    data = load_yaml_file("ssmincidents_ResponsePlan.yaml")

    from tropoloco.model.ssmincidents import ResponsePlan as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("ssmincidents_ResponsePlan.json"), reason="Skipping Test for compatability reason")
def test_ssmincidents_ResponsePlan_json():
    data = load_json_file("ssmincidents_ResponsePlan.json")

    from tropoloco.model.ssmincidents import ResponsePlan as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("sso_InstanceAccessControlAttributeConfiguration.yaml"), reason="Skipping Test for compatability reason")
def test_sso_InstanceAccessControlAttributeConfiguration_yaml():
    data = load_yaml_file("sso_InstanceAccessControlAttributeConfiguration.yaml")

    from tropoloco.model.sso import InstanceAccessControlAttributeConfiguration as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("sso_InstanceAccessControlAttributeConfiguration.json"), reason="Skipping Test for compatability reason")
def test_sso_InstanceAccessControlAttributeConfiguration_json():
    data = load_json_file("sso_InstanceAccessControlAttributeConfiguration.json")

    from tropoloco.model.sso import InstanceAccessControlAttributeConfiguration as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("sagemaker_Project.yaml"), reason="Skipping Test for compatability reason")
def test_sagemaker_Project_yaml():
    data = load_yaml_file("sagemaker_Project.yaml")

    from tropoloco.model.sagemaker import Project as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("sagemaker_Project.json"), reason="Skipping Test for compatability reason")
def test_sagemaker_Project_json():
    data = load_json_file("sagemaker_Project.json")

    from tropoloco.model.sagemaker import Project as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("secretsmanager_ResourcePolicy.yaml"), reason="Skipping Test for compatability reason")
def test_secretsmanager_ResourcePolicy_yaml():
    data = load_yaml_file("secretsmanager_ResourcePolicy.yaml")

    from tropoloco.model.secretsmanager import ResourcePolicy as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("secretsmanager_ResourcePolicy.json"), reason="Skipping Test for compatability reason")
def test_secretsmanager_ResourcePolicy_json():
    data = load_json_file("secretsmanager_ResourcePolicy.json")

    from tropoloco.model.secretsmanager import ResourcePolicy as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("secretsmanager_RotationSchedule.yaml"), reason="Skipping Test for compatability reason")
def test_secretsmanager_RotationSchedule_yaml():
    data = load_yaml_file("secretsmanager_RotationSchedule.yaml")

    from tropoloco.model.secretsmanager import RotationSchedule as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("secretsmanager_RotationSchedule.json"), reason="Skipping Test for compatability reason")
def test_secretsmanager_RotationSchedule_json():
    data = load_json_file("secretsmanager_RotationSchedule.json")

    from tropoloco.model.secretsmanager import RotationSchedule as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("securityhub_AutomationRule.yaml"), reason="Skipping Test for compatability reason")
def test_securityhub_AutomationRule_yaml():
    data = load_yaml_file("securityhub_AutomationRule.yaml")

    from tropoloco.model.securityhub import AutomationRule as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("securityhub_AutomationRule.json"), reason="Skipping Test for compatability reason")
def test_securityhub_AutomationRule_json():
    data = load_json_file("securityhub_AutomationRule.json")

    from tropoloco.model.securityhub import AutomationRule as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("servicediscovery_HttpNamespace.yaml"), reason="Skipping Test for compatability reason")
def test_servicediscovery_HttpNamespace_yaml():
    data = load_yaml_file("servicediscovery_HttpNamespace.yaml")

    from tropoloco.model.servicediscovery import HttpNamespace as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("servicediscovery_HttpNamespace.json"), reason="Skipping Test for compatability reason")
def test_servicediscovery_HttpNamespace_json():
    data = load_json_file("servicediscovery_HttpNamespace.json")

    from tropoloco.model.servicediscovery import HttpNamespace as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("servicediscovery_Instance.yaml"), reason="Skipping Test for compatability reason")
def test_servicediscovery_Instance_yaml():
    data = load_yaml_file("servicediscovery_Instance.yaml")

    from tropoloco.model.servicediscovery import Instance as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("servicediscovery_Instance.json"), reason="Skipping Test for compatability reason")
def test_servicediscovery_Instance_json():
    data = load_json_file("servicediscovery_Instance.json")

    from tropoloco.model.servicediscovery import Instance as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("servicediscovery_PrivateDnsNamespace.yaml"), reason="Skipping Test for compatability reason")
def test_servicediscovery_PrivateDnsNamespace_yaml():
    data = load_yaml_file("servicediscovery_PrivateDnsNamespace.yaml")

    from tropoloco.model.servicediscovery import PrivateDnsNamespace as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("servicediscovery_PrivateDnsNamespace.json"), reason="Skipping Test for compatability reason")
def test_servicediscovery_PrivateDnsNamespace_json():
    data = load_json_file("servicediscovery_PrivateDnsNamespace.json")

    from tropoloco.model.servicediscovery import PrivateDnsNamespace as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("servicediscovery_PublicDnsNamespace.yaml"), reason="Skipping Test for compatability reason")
def test_servicediscovery_PublicDnsNamespace_yaml():
    data = load_yaml_file("servicediscovery_PublicDnsNamespace.yaml")

    from tropoloco.model.servicediscovery import PublicDnsNamespace as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("servicediscovery_PublicDnsNamespace.json"), reason="Skipping Test for compatability reason")
def test_servicediscovery_PublicDnsNamespace_json():
    data = load_json_file("servicediscovery_PublicDnsNamespace.json")

    from tropoloco.model.servicediscovery import PublicDnsNamespace as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("servicediscovery_Service.yaml"), reason="Skipping Test for compatability reason")
def test_servicediscovery_Service_yaml():
    data = load_yaml_file("servicediscovery_Service.yaml")

    from tropoloco.model.servicediscovery import Service as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("servicediscovery_Service.json"), reason="Skipping Test for compatability reason")
def test_servicediscovery_Service_json():
    data = load_json_file("servicediscovery_Service.json")

    from tropoloco.model.servicediscovery import Service as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("shield_ProtectionGroup.yaml"), reason="Skipping Test for compatability reason")
def test_shield_ProtectionGroup_yaml():
    data = load_yaml_file("shield_ProtectionGroup.yaml")

    from tropoloco.model.shield import ProtectionGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("shield_ProtectionGroup.json"), reason="Skipping Test for compatability reason")
def test_shield_ProtectionGroup_json():
    data = load_json_file("shield_ProtectionGroup.json")

    from tropoloco.model.shield import ProtectionGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("simspaceweaver_Simulation.yaml"), reason="Skipping Test for compatability reason")
def test_simspaceweaver_Simulation_yaml():
    data = load_yaml_file("simspaceweaver_Simulation.yaml")

    from tropoloco.model.simspaceweaver import Simulation as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("simspaceweaver_Simulation.json"), reason="Skipping Test for compatability reason")
def test_simspaceweaver_Simulation_json():
    data = load_json_file("simspaceweaver_Simulation.json")

    from tropoloco.model.simspaceweaver import Simulation as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("stepfunctions_Activity.yaml"), reason="Skipping Test for compatability reason")
def test_stepfunctions_Activity_yaml():
    data = load_yaml_file("stepfunctions_Activity.yaml")

    from tropoloco.model.stepfunctions import Activity as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("stepfunctions_Activity.json"), reason="Skipping Test for compatability reason")
def test_stepfunctions_Activity_json():
    data = load_json_file("stepfunctions_Activity.json")

    from tropoloco.model.stepfunctions import Activity as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("supportapp_SlackWorkspaceConfiguration.yaml"), reason="Skipping Test for compatability reason")
def test_supportapp_SlackWorkspaceConfiguration_yaml():
    data = load_yaml_file("supportapp_SlackWorkspaceConfiguration.yaml")

    from tropoloco.model.supportapp import SlackWorkspaceConfiguration as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("supportapp_SlackWorkspaceConfiguration.json"), reason="Skipping Test for compatability reason")
def test_supportapp_SlackWorkspaceConfiguration_json():
    data = load_json_file("supportapp_SlackWorkspaceConfiguration.json")

    from tropoloco.model.supportapp import SlackWorkspaceConfiguration as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("synthetics_Canary.yaml"), reason="Skipping Test for compatability reason")
def test_synthetics_Canary_yaml():
    data = load_yaml_file("synthetics_Canary.yaml")

    from tropoloco.model.synthetics import Canary as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("synthetics_Canary.json"), reason="Skipping Test for compatability reason")
def test_synthetics_Canary_json():
    data = load_json_file("synthetics_Canary.json")

    from tropoloco.model.synthetics import Canary as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("transfer_Server.yaml"), reason="Skipping Test for compatability reason")
def test_transfer_Server_yaml():
    data = load_yaml_file("transfer_Server.yaml")

    from tropoloco.model.transfer import Server as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("transfer_Server.json"), reason="Skipping Test for compatability reason")
def test_transfer_Server_json():
    data = load_json_file("transfer_Server.json")

    from tropoloco.model.transfer import Server as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("verifiedpermissions_PolicyStore.yaml"), reason="Skipping Test for compatability reason")
def test_verifiedpermissions_PolicyStore_yaml():
    data = load_yaml_file("verifiedpermissions_PolicyStore.yaml")

    from tropoloco.model.verifiedpermissions import PolicyStore as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("verifiedpermissions_PolicyStore.json"), reason="Skipping Test for compatability reason")
def test_verifiedpermissions_PolicyStore_json():
    data = load_json_file("verifiedpermissions_PolicyStore.json")

    from tropoloco.model.verifiedpermissions import PolicyStore as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("waf_Rule.yaml"), reason="Skipping Test for compatability reason")
def test_waf_Rule_yaml():
    data = load_yaml_file("waf_Rule.yaml")

    from tropoloco.model.waf import Rule as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("waf_Rule.json"), reason="Skipping Test for compatability reason")
def test_waf_Rule_json():
    data = load_json_file("waf_Rule.json")

    from tropoloco.model.waf import Rule as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("wafregional_Rule.yaml"), reason="Skipping Test for compatability reason")
def test_wafregional_Rule_yaml():
    data = load_yaml_file("wafregional_Rule.yaml")

    from tropoloco.model.wafregional import Rule as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("wafregional_Rule.json"), reason="Skipping Test for compatability reason")
def test_wafregional_Rule_json():
    data = load_json_file("wafregional_Rule.json")

    from tropoloco.model.wafregional import Rule as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("wafregional_WebACL.yaml"), reason="Skipping Test for compatability reason")
def test_wafregional_WebACL_yaml():
    data = load_yaml_file("wafregional_WebACL.yaml")

    from tropoloco.model.wafregional import WebACL as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("wafregional_WebACL.json"), reason="Skipping Test for compatability reason")
def test_wafregional_WebACL_json():
    data = load_json_file("wafregional_WebACL.json")

    from tropoloco.model.wafregional import WebACL as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("wafregional_WebACLAssociation.yaml"), reason="Skipping Test for compatability reason")
def test_wafregional_WebACLAssociation_yaml():
    data = load_yaml_file("wafregional_WebACLAssociation.yaml")

    from tropoloco.model.wafregional import WebACLAssociation as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("wafregional_WebACLAssociation.json"), reason="Skipping Test for compatability reason")
def test_wafregional_WebACLAssociation_json():
    data = load_json_file("wafregional_WebACLAssociation.json")

    from tropoloco.model.wafregional import WebACLAssociation as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("wafv2_IPSet.yaml"), reason="Skipping Test for compatability reason")
def test_wafv2_IPSet_yaml():
    data = load_yaml_file("wafv2_IPSet.yaml")

    from tropoloco.model.wafv2 import IPSet as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("wafv2_IPSet.json"), reason="Skipping Test for compatability reason")
def test_wafv2_IPSet_json():
    data = load_json_file("wafv2_IPSet.json")

    from tropoloco.model.wafv2 import IPSet as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("wafv2_LoggingConfiguration.yaml"), reason="Skipping Test for compatability reason")
def test_wafv2_LoggingConfiguration_yaml():
    data = load_yaml_file("wafv2_LoggingConfiguration.yaml")

    from tropoloco.model.wafv2 import LoggingConfiguration as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("wafv2_LoggingConfiguration.json"), reason="Skipping Test for compatability reason")
def test_wafv2_LoggingConfiguration_json():
    data = load_json_file("wafv2_LoggingConfiguration.json")

    from tropoloco.model.wafv2 import LoggingConfiguration as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("wafv2_RegexPatternSet.yaml"), reason="Skipping Test for compatability reason")
def test_wafv2_RegexPatternSet_yaml():
    data = load_yaml_file("wafv2_RegexPatternSet.yaml")

    from tropoloco.model.wafv2 import RegexPatternSet as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("wafv2_RegexPatternSet.json"), reason="Skipping Test for compatability reason")
def test_wafv2_RegexPatternSet_json():
    data = load_json_file("wafv2_RegexPatternSet.json")

    from tropoloco.model.wafv2 import RegexPatternSet as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("wafv2_RuleGroup.yaml"), reason="Skipping Test for compatability reason")
def test_wafv2_RuleGroup_yaml():
    data = load_yaml_file("wafv2_RuleGroup.yaml")

    from tropoloco.model.wafv2 import RuleGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("wafv2_RuleGroup.json"), reason="Skipping Test for compatability reason")
def test_wafv2_RuleGroup_json():
    data = load_json_file("wafv2_RuleGroup.json")

    from tropoloco.model.wafv2 import RuleGroup as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("wafv2_WebACL.yaml"), reason="Skipping Test for compatability reason")
def test_wafv2_WebACL_yaml():
    data = load_yaml_file("wafv2_WebACL.yaml")

    from tropoloco.model.wafv2 import WebACL as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("wafv2_WebACL.json"), reason="Skipping Test for compatability reason")
def test_wafv2_WebACL_json():
    data = load_json_file("wafv2_WebACL.json")

    from tropoloco.model.wafv2 import WebACL as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("wafv2_WebACLAssociation.yaml"), reason="Skipping Test for compatability reason")
def test_wafv2_WebACLAssociation_yaml():
    data = load_yaml_file("wafv2_WebACLAssociation.yaml")

    from tropoloco.model.wafv2 import WebACLAssociation as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("wafv2_WebACLAssociation.json"), reason="Skipping Test for compatability reason")
def test_wafv2_WebACLAssociation_json():
    data = load_json_file("wafv2_WebACLAssociation.json")

    from tropoloco.model.wafv2 import WebACLAssociation as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("xray_Group.yaml"), reason="Skipping Test for compatability reason")
def test_xray_Group_yaml():
    data = load_yaml_file("xray_Group.yaml")

    from tropoloco.model.xray import Group as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("xray_Group.json"), reason="Skipping Test for compatability reason")
def test_xray_Group_json():
    data = load_json_file("xray_Group.json")

    from tropoloco.model.xray import Group as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("xray_SamplingRule.yaml"), reason="Skipping Test for compatability reason")
def test_xray_SamplingRule_yaml():
    data = load_yaml_file("xray_SamplingRule.yaml")

    from tropoloco.model.xray import SamplingRule as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()


@pytest.mark.skipif(should_skip_test("xray_SamplingRule.json"), reason="Skipping Test for compatability reason")
def test_xray_SamplingRule_json():
    data = load_json_file("xray_SamplingRule.json")

    from tropoloco.model.xray import SamplingRule as TropoT
    loaded_resource = TropoT(title="foo", **data["Properties"])

    loaded_resource.to_troposphere()
