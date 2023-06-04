from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional
from .article_id_list import ArticleIdList
from .history_1 import History1
from .object_list import ObjectList
from .reference_list import ReferenceList


@dataclass
class PubmedData:
    history: Optional[History1] = field(
        default=None,
        metadata={
            "name": "History",
            "type": "Element",
        }
    )
    publication_status: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicationStatus",
            "type": "Element",
            "required": True,
        }
    )
    article_id_list: Optional[ArticleIdList] = field(
        default=None,
        metadata={
            "name": "ArticleIdList",
            "type": "Element",
            "required": True,
        }
    )
    object_list: Optional[ObjectList] = field(
        default=None,
        metadata={
            "name": "ObjectList",
            "type": "Element",
        }
    )
    reference_list: List[ReferenceList] = field(
        default_factory=list,
        metadata={
            "name": "ReferenceList",
            "type": "Element",
        }
    )
