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


# TODO if yamls fails try to grab json instead... and then write yaml.


def main():
    spec = download_spec()

    resources = []

    with open("manifest.json", "r") as f:
        manifest = json.loads(f.read())

    for resource_type in spec["ResourceTypes"].keys():
        doc_url = spec["ResourceTypes"][resource_type]["Documentation"]

        if not doc_url in manifest:
            print(f"requesting doc url: {doc_url}")
            doc_resp = requests.get(doc_url)
            doc_resp.raise_for_status()
            manifest[doc_url] = doc_resp.text
            with open("manifest.json", "w") as f:
                f.write(json.dumps(manifest))
            response = manifest[doc_url]
        else:
            response = manifest[doc_url]

        soup = BeautifulSoup(response, "html.parser")
        # get the last yaml and json blocks on the page they are the examples
        json_code_block = soup.find_all("code", {"class": "json"})[-1]
        yaml_code_block = soup.find_all("code", {"class": "yaml"})[-1]

        scraped_data = []
        try:
            scraped_yaml = yaml.safe_load(yaml_code_block.get_text())
            scraped_data.append(("yaml", yaml_code_block))
        except AttributeError as e:
            raise e
            print(f"ERROR: resource_type: {resource_type}")
        try:
            print(json_code_block.get_text(strip=True))
            print(type(json_code_block.get_text()))
            scraped_json = json.loads(json_code_block.get_text())
            scraped_data.append(("json", json_code_block))
        except AttributeError:
            print(f"ERROR: resource_type: {resource_type}")

        if not scraped_data:
            continue

        service_name = scraped_data[0]["Type"].split("::")[1].lower()
        resource_name = scraped_data[0]["Type"].split("::")[2]
        if service_name == "lambda":
            service_name = "awslambda"

        # loaded_yaml = yaml.safe_load(code_block.get_text())

        # add = True
        # if "Properties" in loaded_yaml:
        #     for k, v in loaded_yaml["Properties"].items():
        #         # bad aws example check. See: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html
        #         # The example users a placeholder instead of actually defining the type
        #         if k == v:
        #             add = False
        #         elif v == "String":
        #             add = False

        # else:
        #     print(f"NO PROPERTIES: ", {"service_name": service_name, "resource_name": resource_name})

        for file_type, code_block in scraped_data:
            resources.append(
                {"service_name": service_name, "resource_name": resource_name}
            )
            with open(
                f"../tropoloco/tests/aws_cfn_examples/{service_name}_{resource_name}.{file_type}",
                "w",
            ) as f:
                f.write(code_block)

    with open("templates/write_test_cfn_examples.py.tpl.j2") as template_file:
        template = JINJA_ENV.from_string(template_file.read())

    with open(f"../tropoloco/tests/test_cfn_examples.py", "w") as output_file:
        template.stream(resources=resources).dump(output_file)


if __name__ == "__main__":
    main()
