from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional
from .medline_citation import MedlineCitation
from .pubmed_data import PubmedData


@dataclass
class PubmedArticle:
    medline_citation: Optional[MedlineCitation] = field(
        default=None,
        metadata={
            "name": "MedlineCitation",
            "type": "Element",
            "required": True,
        }
    )
    pubmed_data: Optional[PubmedData] = field(
        default=None,
        metadata={
            "name": "PubmedData",
            "type": "Element",
        }
    )
