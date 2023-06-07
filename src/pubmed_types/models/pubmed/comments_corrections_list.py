from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List
from .comments_corrections import CommentsCorrections


@dataclass
class CommentsCorrectionsList:
    comments_corrections: List[CommentsCorrections] = field(
        default_factory=list,
        metadata={
            "name": "CommentsCorrections",
            "type": "Element",
            "min_occurs": 1,
        }
    )
