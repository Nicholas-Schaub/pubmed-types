from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional
from .book_document import BookDocument
from .pubmed_book_data import PubmedBookData


@dataclass
class PubmedBookArticle:
    book_document: Optional[BookDocument] = field(
        default=None,
        metadata={
            "name": "BookDocument",
            "type": "Element",
            "required": True,
        }
    )
    pubmed_book_data: Optional[PubmedBookData] = field(
        default=None,
        metadata={
            "name": "PubmedBookData",
            "type": "Element",
        }
    )
