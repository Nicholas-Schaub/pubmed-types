from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional


@dataclass
class Pagination:
    start_page: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartPage",
            "type": "Element",
        }
    )
    end_page: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndPage",
            "type": "Element",
        }
    )
    medline_pgn: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MedlinePgn",
            "type": "Element",
            "max_occurs": 2,
        }
    )
