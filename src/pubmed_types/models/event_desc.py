from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional, Union
from .access_date import (
    Date,
    Email,
    ExtLink,
    Isbn,
    Issn,
    IssnL,
    StringDate,
    Uri,
)
from .article_id import ArticleId
from .article_version import ArticleVersion
from .article_version_alternatives import ArticleVersionAlternatives
from .org.w3.xml.pkg_1998.namespace.lang_value import LangValue
from .pub_date_2 import PubDate2
from .pub_date_not_available import PubDateNotAvailable


@dataclass
class EventDesc:
    """
    <div> <h3>Event Description</h3> </div>
    """
    class Meta:
        name = "event-desc"

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
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "article-id",
                    "type": ArticleId,
                },
                {
                    "name": "issn",
                    "type": Issn,
                },
                {
                    "name": "issn-l",
                    "type": IssnL,
                },
                {
                    "name": "isbn",
                    "type": Isbn,
                },
                {
                    "name": "article-version",
                    "type": ArticleVersion,
                },
                {
                    "name": "article-version-alternatives",
                    "type": ArticleVersionAlternatives,
                },
                {
                    "name": "date",
                    "type": Date,
                },
                {
                    "name": "string-date",
                    "type": StringDate,
                },
                {
                    "name": "pub-date",
                    "type": PubDate2,
                },
                {
                    "name": "pub-date-not-available",
                    "type": PubDateNotAvailable,
                },
            ),
        }
    )
