import os
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import List

import git
import jinja2
from tqdm import tqdm

from parse_troposphere import parse_troposphere_file
from scrape import scrape_cfn_docs

IGNORE = set(["__init__.py", "helpers", "type_defs", "validators", "openstack"])


JINJA_ENV = jinja2.Environment(keep_trailing_newline=True)


# TODO: NEED to handle enum types that troposphere implements validators for.
# Probably need to do this with a chat GPT request...because they are not in a standard format for parsing.


def ignore(py_file: str):
    for ig in IGNORE:
        if ig in str(py_file):
            return True


def map_properties_to_fields(fields: dict, scaped_meta: List):
    for f in fields:
        for prop in scaped_meta.properties:
            if f.name == prop.name:
                print("we wound a match")
                f.scraped_properties = prop


def main():
    destination_directory = TemporaryDirectory()
    with TemporaryDirectory() as td:
        repo_url = "https://github.com/cloudtools/troposphere.git"

        repo = git.Repo.clone_from(repo_url, td)
        py_files = list(Path(os.path.join(td, "troposphere/")).rglob(f"*.py"))

        with open("templates/troposphere_aws_service.py.tpl.j2") as template_file:
            template = JINJA_ENV.from_string(template_file.read())
        for py_file in tqdm(py_files):
            if ignore(py_file=py_file):
                print(f"Encountered ignore path: {py_file}")
                continue
            print("parsing troposphere file")
            parsed_troposphere_obj = parse_troposphere_file(py_file)

            for tropo_obj in parsed_troposphere_obj:
                if tropo_obj.obj_type == "AWSObject":
                    print(f"scraping: {tropo_obj.url}")
                    scraped_meta = scrape_cfn_docs(url=tropo_obj.url)
                    tropo_obj.scraped_meta = scraped_meta

                    if tropo_obj.scraped_meta:
                        map_properties_to_fields(
                            fields=tropo_obj.fields, scaped_meta=scraped_meta
                        )

            with open(
                f"../tropoloco/src/tropoloco/models/{Path(py_file).name}", "w"
            ) as output_file:
                template.stream(parsed_tropo_objs=parsed_troposphere_obj).dump(
                    output_file
                )


main()
