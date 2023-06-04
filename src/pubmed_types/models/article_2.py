from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional, Union
from .article_dtd_version import ArticleDtdVersion
from .back import Back
from .body import Body
from .floats_group import FloatsGroup
from .front import Front
from .org.w3.xml.pkg_1998.namespace.lang_value import LangValue
from .processing_meta import ProcessingMeta
from .response import Response
from .sub_article import SubArticle


@dataclass
class Article2:
    """
    <div> <h3>Article</h3> </div>
    """
    class Meta:
        name = "article"

    processing_meta: Optional[ProcessingMeta] = field(
        default=None,
        metadata={
            "name": "processing-meta",
            "type": "Element",
        }
    )
    front: Optional[Front] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    body: Optional[Body] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    back: Optional[Back] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    floats_group: Optional[FloatsGroup] = field(
        default=None,
        metadata={
            "name": "floats-group",
            "type": "Element",
        }
    )
    sub_article: List[SubArticle] = field(
        default_factory=list,
        metadata={
            "name": "sub-article",
            "type": "Element",
        }
    )
    response: List[Response] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    article_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "article-type",
            "type": "Attribute",
        }
    )
    dtd_version: Optional[ArticleDtdVersion] = field(
        default=None,
        metadata={
            "name": "dtd-version",
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
    lang: Union[str, LangValue] = field(
        default="en",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
