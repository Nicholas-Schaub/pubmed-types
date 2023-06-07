from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional
from .comments_corrections_ref_type import CommentsCorrectionsRefType
from .pmid import Pmid


@dataclass
class CommentsCorrections:
    ref_type: Optional[CommentsCorrectionsRefType] = field(
        default=None,
        metadata={
            "name": "RefType",
            "type": "Attribute",
            "required": True,
        }
    )
    ref_source: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefSource",
            "type": "Element",
            "required": True,
        }
    )
    pmid: Optional[Pmid] = field(
        default=None,
        metadata={
            "name": "PMID",
            "type": "Element",
        }
    )
    note: Optional[str] = field(
        default=None,
        metadata={
            "name": "Note",
            "type": "Element",
        }
    )
