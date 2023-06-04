from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List
from .pubmed_book_article import PubmedBookArticle


@dataclass
class PubmedBookArticleSet:
    pubmed_book_article: List[PubmedBookArticle] = field(
        default_factory=list,
        metadata={
            "name": "PubmedBookArticle",
            "type": "Element",
        }
    )
