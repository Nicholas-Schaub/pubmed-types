from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional
from .u import (
    B,
    I,
    Sub,
    Sup,
    U,
)


@dataclass
class ArticleTitle:
    book: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    sec: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    part: Optional[str] = field(
        default=None,
        metadata={
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
            ),
        }
    )
