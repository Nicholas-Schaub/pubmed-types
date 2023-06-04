from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional
from .delete_citation import DeleteCitation
from .pubmed_article import PubmedArticle
from .pubmed_book_article import PubmedBookArticle


@dataclass
class PubmedArticleSet:
    pubmed_article: List[PubmedArticle] = field(
        default_factory=list,
        metadata={
            "name": "PubmedArticle",
            "type": "Element",
        }
    )
    pubmed_book_article: List[PubmedBookArticle] = field(
        default_factory=list,
        metadata={
            "name": "PubmedBookArticle",
            "type": "Element",
        }
    )
    delete_citation: Optional[DeleteCitation] = field(
        default=None,
        metadata={
            "name": "DeleteCitation",
            "type": "Element",
        }
    )
