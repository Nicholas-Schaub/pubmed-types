from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional
from .abstract_text import AbstractText
from .other_abstract_type import OtherAbstractType


@dataclass
class OtherAbstract:
    type: Optional[OtherAbstractType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    language: str = field(
        default="eng",
        metadata={
            "name": "Language",
            "type": "Attribute",
            "required": True,
        }
    )
    abstract_text: List[AbstractText] = field(
        default_factory=list,
        metadata={
            "name": "AbstractText",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    copyright_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "CopyrightInformation",
            "type": "Element",
        }
    )
