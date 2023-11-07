import json
import yaml
import requests
import jinja2
from bs4 import BeautifulSoup

CLOUDFORMATION_SPEC_URL = "https://d1uauaxba7bl26.cloudfront.net/latest/gzip/CloudFormationResourceSpecification.json"
JINJA_ENV = jinja2.Environment(keep_trailing_newline=True)


def download_spec():
    response = requests.get(CLOUDFORMATION_SPEC_URL)
    cfn_spec = json.loads(response.text)
    return cfn_spec


def find_resource_by_type(data, target_type):
    if isinstance(data, dict):
        if data.get("Type") == target_type:
            return data
        for key, val in data.items():
            resource = find_resource_by_type(val, target_type)
            if resource:
                return resource


def main():
    spec = download_spec()
    resources = []

    with open("manifest.json", "r") as f:
        manifest = json.loads(f.read())

    for resource_type in spec["ResourceTypes"].keys():
        doc_url = spec["ResourceTypes"][resource_type]["Documentation"]

        if not doc_url in manifest:
            doc_resp = requests.get(doc_url)
            doc_resp.raise_for_status()
            manifest[doc_url] = doc_resp.text
            with open("manifest.json", "w") as f:
                f.write(json.dumps(manifest))
            response = manifest[doc_url]
        else:
            response = manifest[doc_url]

        soup = BeautifulSoup(response, "html.parser")

        try:
            yaml_code_block = soup.find_all("code", {"class": "yaml"})[-1]
        except IndexError:
            pass

        try:
            json_code_block = soup.find_all("code", {"class": "json"})[-1]
        except IndexError:
            if not yaml_code_block:
                print("failed to find any code blocks!")
                continue

        try:
            json_data = json.loads(json_code_block.get_text(strip=True))
            json_resource_data = find_resource_by_type(json_data, resource_type)
        except (AttributeError, json.JSONDecodeError):
            try:
                json_data = json.loads("{" + json_code_block.get_text(strip=True) + "}")
                json_resource_data = find_resource_by_type(json_data, resource_type)
            except (AttributeError, json.JSONDecodeError, Exception):
                json_resource_data = None

        try:
            yaml_data = yaml.safe_load(yaml_code_block.get_text())
            yaml_resource_data = find_resource_by_type(yaml_data, resource_type)
        except (
            AttributeError,
            yaml.constructor.ConstructorError,
            yaml.scanner.ScannerError,
            yaml.parser.ParserError,
            yaml.reader.ReaderError,
        ):
            yaml_resource_data = None

        if not yaml_resource_data or not json_resource_data:
            print("failed to parse an example")
            continue

        scraped_data = [yaml_resource_data, json_resource_data]
        print(scraped_data[0])
        service_name = scraped_data[0]["Type"].split("::")[1].lower()
        resource_name = scraped_data[0]["Type"].split("::")[2]
        if service_name == "lambda":
            service_name = "awslambda"

        if yaml_resource_data:
            resources.append(
                {
                    "service_name": service_name,
                    "resource_name": resource_name,
                    "file_type": "yaml",
                }
            )
            with open(
                f"../tropoloco/tests/aws_cfn_examples/{service_name}_{resource_name}.yaml",
                "w",
            ) as f:
                f.write(yaml.dump(yaml_resource_data))

        if json_resource_data:
            resources.append(
                {
                    "service_name": service_name,
                    "resource_name": resource_name,
                    "file_type": "json",
                }
            )
            with open(
                f"../tropoloco/tests/aws_cfn_examples/{service_name}_{resource_name}.json",
                "w",
            ) as f:
                f.write(json.dumps(json_resource_data))

    with open("templates/write_test_cfn_examples.py.tpl.j2") as template_file:
        template = JINJA_ENV.from_string(template_file.read())

    with open(f"../tropoloco/tests/test_cfn_examples.py", "w") as output_file:
        template.stream(resources=resources).dump(output_file)


if __name__ == "__main__":
    main()
