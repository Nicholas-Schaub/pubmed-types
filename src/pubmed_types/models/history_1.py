from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List
from .pub_med_pub_date import PubMedPubDate


@dataclass
class History1:
    class Meta:
        name = "History"

    pub_med_pub_date: List[PubMedPubDate] = field(
        default_factory=list,
        metadata={
            "name": "PubMedPubDate",
            "type": "Element",
            "min_occurs": 1,
        }
    )
