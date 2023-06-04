from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional
from .article_id_list import ArticleIdList
from .citation import Citation


@dataclass
class Reference:
    citation: Optional[Citation] = field(
        default=None,
        metadata={
            "name": "Citation",
            "type": "Element",
            "required": True,
        }
    )
    article_id_list: Optional[ArticleIdList] = field(
        default=None,
        metadata={
            "name": "ArticleIdList",
            "type": "Element",
        }
    )
