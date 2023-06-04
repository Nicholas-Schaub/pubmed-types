from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional


@dataclass
class MedlineJournalInfo:
    country: Optional[str] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
        }
    )
    medline_ta: Optional[str] = field(
        default=None,
        metadata={
            "name": "MedlineTA",
            "type": "Element",
            "required": True,
        }
    )
    nlm_unique_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "NlmUniqueID",
            "type": "Element",
        }
    )
    issnlinking: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISSNLinking",
            "type": "Element",
        }
    )
