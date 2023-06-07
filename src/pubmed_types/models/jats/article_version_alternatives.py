from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional
from .article_version import ArticleVersion


@dataclass
class ArticleVersionAlternatives:
    """
    <div> <h3>Article Version Alternatives</h3> </div>
    """
    class Meta:
        name = "article-version-alternatives"

    article_version: List[ArticleVersion] = field(
        default_factory=list,
        metadata={
            "name": "article-version",
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
