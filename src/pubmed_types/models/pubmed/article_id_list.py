from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List
from .article_id import ArticleId


@dataclass
class ArticleIdList:
    article_id: List[ArticleId] = field(
        default_factory=list,
        metadata={
            "name": "ArticleId",
            "type": "Element",
            "min_occurs": 1,
        }
    )
