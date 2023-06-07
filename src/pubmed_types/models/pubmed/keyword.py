from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List
from .keyword_major_topic_yn import KeywordMajorTopicYn
from .u import (
    B,
    I,
    Sub,
    Sup,
    U,
)


@dataclass
class Keyword:
    major_topic_yn: KeywordMajorTopicYn = field(
        default=KeywordMajorTopicYn.N,
        metadata={
            "name": "MajorTopicYN",
            "type": "Attribute",
            "required": True,
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
