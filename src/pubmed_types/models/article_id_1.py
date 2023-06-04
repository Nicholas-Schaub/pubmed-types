from dataclasses import field
from pydantic.dataclasses import dataclass
from .article_id_id_type import ArticleIdIdType


@dataclass
class ArticleId1:
    class Meta:
        name = "ArticleId"

    id_type: ArticleIdIdType = field(
        default=ArticleIdIdType.PUBMED,
        metadata={
            "name": "IdType",
            "type": "Attribute",
            "required": True,
        }
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
