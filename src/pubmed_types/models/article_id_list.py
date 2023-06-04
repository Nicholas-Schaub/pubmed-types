from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List
from .article_id_1 import ArticleId1


@dataclass
class ArticleIdList:
    article_id: List[ArticleId1] = field(
        default_factory=list,
        metadata={
            "name": "ArticleId",
            "type": "Element",
            "min_occurs": 1,
        }
    )
