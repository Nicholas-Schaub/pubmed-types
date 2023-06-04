from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional
from .abstract_text_nlm_category import AbstractTextNlmCategory
from .access_date import (
    Sub,
    Sup,
)
from .disp_formula_1 import DispFormula1
from .u import (
    B,
    I,
    U,
)


@dataclass
class AbstractText:
    label: Optional[str] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Attribute",
        }
    )
    nlm_category: Optional[AbstractTextNlmCategory] = field(
        default=None,
        metadata={
            "name": "NlmCategory",
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "b",
                    "type": B,
                },
                {
                    "name": "i",
                    "type": I,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "u",
                    "type": U,
                },
                {
                    "name": "math",
                    "type": str,
                },
                {
                    "name": "DispFormula",
                    "type": DispFormula1,
                },
            ),
        }
    )
