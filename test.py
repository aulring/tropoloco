import yaml

from tropoloco.model.awslambda import Function


with open("test.yaml", "r") as f:
    data = f.read()

data = yaml.safe_load(data)
function = Function(title="test", **data)
