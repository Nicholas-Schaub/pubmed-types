from dataclasses import field
from pydantic.dataclasses import dataclass
from .first_name_empty_yn import FirstNameEmptyYn


@dataclass
class FirstName:
    empty_yn: FirstNameEmptyYn = field(
        default=FirstNameEmptyYn.N,
        metadata={
            "name": "EmptyYN",
            "type": "Attribute",
            "required": True,
        }
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
