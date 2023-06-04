from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional
from .book_document import BookDocument
from .delete_document import DeleteDocument


@dataclass
class BookDocumentSet:
    book_document: List[BookDocument] = field(
        default_factory=list,
        metadata={
            "name": "BookDocument",
            "type": "Element",
        }
    )
    delete_document: Optional[DeleteDocument] = field(
        default=None,
        metadata={
            "name": "DeleteDocument",
            "type": "Element",
        }
    )
