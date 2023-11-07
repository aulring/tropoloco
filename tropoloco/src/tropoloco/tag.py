from pydantic import BaseModel, RootModel, root_validator
from typing import List, Dict, Union


class Tag(BaseModel):
    Key: str
    Value: Union[int, str]


class Tags(RootModel):
    root: List[Tag]

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value: Dict[str, str]):
        return [{"Key": k, "Value": v} for k, v in value.items()]

    def to_dict(self):
        return self.root
