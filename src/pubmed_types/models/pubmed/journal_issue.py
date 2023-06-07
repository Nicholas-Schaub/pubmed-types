from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional
from .journal_issue_cited_medium import JournalIssueCitedMedium
from .pub_date import PubDate


@dataclass
class JournalIssue:
    cited_medium: Optional[JournalIssueCitedMedium] = field(
        default=None,
        metadata={
            "name": "CitedMedium",
            "type": "Attribute",
            "required": True,
        }
    )
    volume: Optional[str] = field(
        default=None,
        metadata={
            "name": "Volume",
            "type": "Element",
        }
    )
    issue: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issue",
            "type": "Element",
        }
    )
    pub_date: Optional[PubDate] = field(
        default=None,
        metadata={
            "name": "PubDate",
            "type": "Element",
            "required": True,
        }
    )
