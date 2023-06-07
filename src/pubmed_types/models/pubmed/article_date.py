from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional


@dataclass
class ArticleDate:
    date_type: str = field(
        init=False,
        default="Electronic",
        metadata={
            "name": "DateType",
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
