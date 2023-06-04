from dataclasses import field
from pydantic.dataclasses import dataclass


@dataclass
class ArchiveCopySource:
    doc_type: str = field(
        init=False,
        default="pdf",
        metadata={
            "name": "DocType",
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
