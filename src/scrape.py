import time
from dataclasses import dataclass
from typing import Dict, List, Optional, Union

import requests
from bs4 import BeautifulSoup


@dataclass
class RefMetadata:
    description: Optional[str]


@dataclass
class FnGetAttMetadata:
    attributes: Dict[str, str]


@dataclass
class ReturnValues:
    fn_get_att_metadata: Optional[FnGetAttMetadata] = None
    ref_metadata: Optional[RefMetadata] = None


@dataclass
class PropertyMetadata:
    name: str
    description: str
    required: bool
    type: Optional[str]
    allowed_values: Optional[List[str]]
    update_requires: Optional[str]


@dataclass
class ScrapedMeta:
    properties: List[PropertyMetadata]
    return_values: List[ReturnValues]


def parse_return_values(soup) -> List[ReturnValues]:
    metadata_list = []

    # Extract headers
    headers = soup.find_all(["h3", "h4"])

    for header in headers:
        header_text = header.get_text().strip()
        # If header is Ref
        return_values = ReturnValues()
        if header_text == "Ref":
            description = header.find_next("p")
            description_text = (
                description.get_text().strip().replace("\n", " ")
                if description
                else None
            )
            return_values.ref_metadata = RefMetadata(description=description_text)
        # If header is Fn::GetAtt
        elif header_text == "Fn::GetAtt":
            item_dict = {}
            definitions = header.find_next("div", class_="variablelist").find_all("dl")
            for definition in definitions:
                term = definition.find("dt").get_text().strip()
                description = definition.find("dd").get_text().strip()
                item_dict[term] = description
            return_values.fn_get_att_metadata = FnGetAttMetadata(attributes=item_dict)
        if return_values.fn_get_att_metadata or return_values.ref_metadata:
            metadata_list.append(return_values)

    return metadata_list


def parse_properties(soup):
    properties_section = soup.find("div", class_="variablelist")
    # Extracting properties details
    properties = []
    if properties_section:
        for dt in properties_section.find_all("dt"):
            try:
                property_name = dt.find("code").get_text(strip=True)
            except AttributeError:
                print("ERRRORRRR: does not follow standard parsing rule")
                continue

            # Description and other details
            dd = dt.find_next_sibling("dd")
            if dd:
                description = dd.find("p").get_text(strip=True)

                # Extracting additional information
                required = "Required" in dd.get_text()
                prop_type = None
                allowed_values = None
                update_requires = None

                type_tag = dd.find("p", string=lambda x: x and "Type" in x)
                if type_tag:
                    prop_type = (
                        type_tag.get_text(strip=True).replace("Type:", "").strip()
                    )

                allowed_values_tag = dd.find("em", string="Allowed values")
                if allowed_values_tag:
                    code_tag = allowed_values_tag.find_next_sibling(
                        "code", class_="code"
                    )
                    if code_tag:
                        allowed_values = code_tag.get_text(strip=True).split(" | ")

                update_requires_tag = dd.find(
                    "p", string=lambda x: x and "Update requires" in x
                )
                # update_requires_tag.find("a")
                if update_requires_tag and update_requires_tag.find("a"):
                    update_requires = update_requires_tag.find("a").get_text(strip=True)
                else:
                    update_requires = "unknown"

                properties.append(
                    PropertyMetadata(
                        name=property_name,
                        description=description,
                        required=required,
                        type=prop_type,
                        allowed_values=allowed_values,
                        update_requires=update_requires,
                    )
                )

    return properties


def scrape_cfn_docs(
    url: str = "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html",
):
    if not url:
        print("URL is None returning")
        return
    time.sleep(1)

    # Fetch the webpage content
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")

    return_values = parse_return_values(soup=soup)
    properties = parse_properties(soup=soup)
    scraped_meta = ScrapedMeta(properties=properties, return_values=return_values)

    return scraped_meta


if __name__ == "__main__":
    scraped_meta = scrape_cfn_docs()
