from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional


@dataclass
class PubDate1:
    class Meta:
        name = "PubDate"

    year: Optional[str] = field(
        default=None,
        metadata={
            "name": "Year",
            "type": "Element",
        }
    )
    month: Optional[str] = field(
        default=None,
        metadata={
            "name": "Month",
            "type": "Element",
        }
    )
    day: Optional[str] = field(
        default=None,
        metadata={
            "name": "Day",
            "type": "Element",
        }
    )
    season: Optional[str] = field(
        default=None,
        metadata={
            "name": "Season",
            "type": "Element",
        }
    )
    medline_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "MedlineDate",
            "type": "Element",
        }
    )
