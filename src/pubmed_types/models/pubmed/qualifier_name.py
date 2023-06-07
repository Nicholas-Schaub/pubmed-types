from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional
from .qualifier_name_major_topic_yn import QualifierNameMajorTopicYn


@dataclass
class QualifierName:
    major_topic_yn: QualifierNameMajorTopicYn = field(
        default=QualifierNameMajorTopicYn.N,
        metadata={
            "name": "MajorTopicYN",
            "type": "Attribute",
            "required": True,
        }
    )
    ui: Optional[str] = field(
        default=None,
        metadata={
            "name": "UI",
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
