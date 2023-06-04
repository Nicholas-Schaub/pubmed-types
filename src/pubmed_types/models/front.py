from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional
from .access_date import (
    Ack,
    Bio,
    DefList,
    FnGroup,
    Glossary,
    ListType,
    Notes,
)
from .article_meta import ArticleMeta
from .journal_meta import JournalMeta


@dataclass
class Front:
    """
    <div> <h3>Front Matter</h3> </div>
    """
    class Meta:
        name = "front"

    journal_meta: Optional[JournalMeta] = field(
        default=None,
        metadata={
            "name": "journal-meta",
            "type": "Element",
        }
    )
    article_meta: Optional[ArticleMeta] = field(
        default=None,
        metadata={
            "name": "article-meta",
            "type": "Element",
            "required": True,
        }
    )
    def_list: List[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
        }
    )
    list_value: List[ListType] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
        }
    )
    ack: List[Ack] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    bio: List[Bio] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    fn_group: List[FnGroup] = field(
        default_factory=list,
        metadata={
            "name": "fn-group",
            "type": "Element",
        }
    )
    glossary: List[Glossary] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    notes: List[Notes] = field(
        default_factory=list,
        metadata={
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
