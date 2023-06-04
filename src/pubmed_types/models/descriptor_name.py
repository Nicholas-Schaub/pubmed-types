from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional
from .descriptor_name_major_topic_yn import DescriptorNameMajorTopicYn
from .descriptor_name_type import DescriptorNameType


@dataclass
class DescriptorName:
    major_topic_yn: DescriptorNameMajorTopicYn = field(
        default=DescriptorNameMajorTopicYn.N,
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
    type: Optional[DescriptorNameType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
