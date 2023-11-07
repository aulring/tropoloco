from bs4 import BeautifulSoup

html = """<h3 id="aws-resource-lambda-layerversionpermission-return-values-ref">Ref</h3><p>
      When you pass the logical ID of this resource to the intrinsic <code class="code">Ref</code>function, <code class="code">Ref</code>returns the layer version ARN and statement ID, such as
        <code class="code">arn:aws:lambda:us-west-2:123456789012:layer:my-layer:1#engineering-org</code>.</p><p>For more information about using the <code class="code">Ref</code>function, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html">Ref</a>.</p><h3 id="aws-resource-lambda-layerversionpermission-return-values-fn--getatt">Fn::GetAtt</h3><h4 id="aws-resource-lambda-layerversionpermission-return-values-fn--getatt-fn--getatt"></h4><div class="variablelist"><dl><dt id="Id-fn::getatt"><span class="term"><code class="code">Id</code></span></dt><dd><p>Property description not available.</p></dd></dl></div>"""

soup = BeautifulSoup(html, "html.parser")

metadata_list = []

# Extract headers
headers = soup.find_all(["h3", "h4"])
for header in headers:
    header_text = header.get_text().strip()
    # If header is Ref
    if header_text == "Ref":
        description = header.find_next("p")
        description_text = description.get_text().strip() if description else None
        metadata_list.append({"Ref": {"description": description_text}})
    # If header is Fn::GetAtt
    elif header_text == "Fn::GetAtt":
        item_dict = {}
        definitions = header.find_next("div", class_="variablelist").find_all("dl")
        for definition in definitions:
            term = definition.find("dt").get_text().strip()
            description = definition.find("dd").get_text().strip()
            item_dict[term] = description
        metadata_list.append({"Fn::GetAtt": item_dict})

print(metadata_list)
