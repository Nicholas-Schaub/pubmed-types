from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional
from .issn_1 import Issn1
from .journal_issue import JournalIssue


@dataclass
class Journal:
    issn: Optional[Issn1] = field(
        default=None,
        metadata={
            "name": "ISSN",
            "type": "Element",
        }
    )
    journal_issue: Optional[JournalIssue] = field(
        default=None,
        metadata={
            "name": "JournalIssue",
            "type": "Element",
            "required": True,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
        }
    )
    isoabbreviation: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISOAbbreviation",
            "type": "Element",
        }
    )
