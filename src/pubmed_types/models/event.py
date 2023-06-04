from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional, Union
from .access_date import (
    Date,
    Isbn,
    Issn,
    IssnL,
    Notes,
    Permissions,
    StringDate,
)
from .article_id import ArticleId
from .article_version import ArticleVersion
from .article_version_alternatives import ArticleVersionAlternatives
from .event_desc import EventDesc
from .org.w3.xml.pkg_1998.namespace.lang_value import LangValue
from .pub_date_2 import PubDate2
from .pub_date_not_available import PubDateNotAvailable
from .self_uri import SelfUri


@dataclass
class Event:
    """
    <div> <h3>Event in Publishing History</h3> </div>
    """
    class Meta:
        name = "event"

    event_desc: Optional[EventDesc] = field(
        default=None,
        metadata={
            "name": "event-desc",
            "type": "Element",
        }
    )
    article_id: List[ArticleId] = field(
        default_factory=list,
        metadata={
            "name": "article-id",
            "type": "Element",
        }
    )
    article_version: Optional[ArticleVersion] = field(
        default=None,
        metadata={
            "name": "article-version",
            "type": "Element",
        }
    )
    article_version_alternatives: Optional[ArticleVersionAlternatives] = field(
        default=None,
        metadata={
            "name": "article-version-alternatives",
            "type": "Element",
        }
    )
    pub_date: List[PubDate2] = field(
        default_factory=list,
        metadata={
            "name": "pub-date",
            "type": "Element",
        }
    )
    pub_date_not_available: Optional[PubDateNotAvailable] = field(
        default=None,
        metadata={
            "name": "pub-date-not-available",
            "type": "Element",
        }
    )
    date: List[Date] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    string_date: List[StringDate] = field(
        default_factory=list,
        metadata={
            "name": "string-date",
            "type": "Element",
        }
    )
    issn: List[Issn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    issn_l: Optional[IssnL] = field(
        default=None,
        metadata={
            "name": "issn-l",
            "type": "Element",
        }
    )
    isbn: List[Isbn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    permissions: Optional[Permissions] = field(
        default=None,
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
    self_uri: List[SelfUri] = field(
        default_factory=list,
        metadata={
            "name": "self-uri",
            "type": "Element",
        }
    )
    event_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "event-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
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
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
