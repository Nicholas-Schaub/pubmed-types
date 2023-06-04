from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List
from .article_1 import Article1


@dataclass
class ArticleSet:
    article: List[Article1] = field(
        default_factory=list,
        metadata={
            "name": "Article",
            "type": "Element",
            "min_occurs": 1,
        }
    )
