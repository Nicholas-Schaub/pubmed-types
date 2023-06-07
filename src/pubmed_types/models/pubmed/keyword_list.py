from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List
from .keyword import Keyword
from .keyword_list_owner import KeywordListOwner


@dataclass
class KeywordList:
    owner: KeywordListOwner = field(
        default=KeywordListOwner.NLM,
        metadata={
            "name": "Owner",
            "type": "Attribute",
            "required": True,
        }
    )
    keyword: List[Keyword] = field(
        default_factory=list,
        metadata={
            "name": "Keyword",
            "type": "Element",
            "min_occurs": 1,
        }
    )
