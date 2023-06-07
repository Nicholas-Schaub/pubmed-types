from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional


@dataclass
class ArticleId:
    """
    <div> <h3>Article Identifier</h3> </div>
    """
    class Meta:
        name = "article-id"

    assigning_authority: Optional[str] = field(
        default=None,
        metadata={
            "name": "assigning-authority",
            "type": "Attribute",
        }
    )
    custom_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "custom-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    pub_id_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "pub-id-type",
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
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
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
