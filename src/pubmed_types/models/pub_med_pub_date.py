from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional
from .pub_med_pub_date_pub_status import PubMedPubDatePubStatus


@dataclass
class PubMedPubDate:
    pub_status: Optional[PubMedPubDatePubStatus] = field(
        default=None,
        metadata={
            "name": "PubStatus",
            "type": "Attribute",
            "required": True,
        }
    )
    year: Optional[str] = field(
        default=None,
        metadata={
            "name": "Year",
            "type": "Element",
            "required": True,
        }
    )
    month: Optional[str] = field(
        default=None,
        metadata={
            "name": "Month",
            "type": "Element",
            "required": True,
        }
    )
    day: Optional[str] = field(
        default=None,
        metadata={
            "name": "Day",
            "type": "Element",
            "required": True,
        }
    )
    hour: Optional[str] = field(
        default=None,
        metadata={
            "name": "Hour",
            "type": "Element",
            "required": True,
        }
    )
    minute: Optional[str] = field(
        default=None,
        metadata={
            "name": "Minute",
            "type": "Element",
            "required": True,
        }
    )
    second: Optional[str] = field(
        default=None,
        metadata={
            "name": "Second",
            "type": "Element",
        }
    )
