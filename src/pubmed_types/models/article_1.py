from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional
from .abstract_1 import Abstract1
from .article_date import ArticleDate
from .article_pub_model import ArticlePubModel
from .article_title_1 import ArticleTitle1
from .author_list import AuthorList
from .data_bank_list import DataBankList
from .elocation_id_1 import ElocationId1
from .grant_list import GrantList
from .journal import Journal
from .pagination import Pagination
from .publication_type_list import PublicationTypeList
from .vernacular_title import VernacularTitle


@dataclass
class Article1:
    class Meta:
        name = "Article"

    pub_model: Optional[ArticlePubModel] = field(
        default=None,
        metadata={
            "name": "PubModel",
            "type": "Attribute",
            "required": True,
        }
    )
    journal: Optional[Journal] = field(
        default=None,
        metadata={
            "name": "Journal",
            "type": "Element",
            "required": True,
        }
    )
    article_title: Optional[ArticleTitle1] = field(
        default=None,
        metadata={
            "name": "ArticleTitle",
            "type": "Element",
            "required": True,
        }
    )
    pagination: Optional[Pagination] = field(
        default=None,
        metadata={
            "name": "Pagination",
            "type": "Element",
        }
    )
    elocation_id: List[ElocationId1] = field(
        default_factory=list,
        metadata={
            "name": "ELocationID",
            "type": "Element",
            "max_occurs": 2,
        }
    )
    abstract: Optional[Abstract1] = field(
        default=None,
        metadata={
            "name": "Abstract",
            "type": "Element",
        }
    )
    author_list: Optional[AuthorList] = field(
        default=None,
        metadata={
            "name": "AuthorList",
            "type": "Element",
        }
    )
    language: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Language",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    data_bank_list: Optional[DataBankList] = field(
        default=None,
        metadata={
            "name": "DataBankList",
            "type": "Element",
        }
    )
    grant_list: Optional[GrantList] = field(
        default=None,
        metadata={
            "name": "GrantList",
            "type": "Element",
        }
    )
    publication_type_list: Optional[PublicationTypeList] = field(
        default=None,
        metadata={
            "name": "PublicationTypeList",
            "type": "Element",
            "required": True,
        }
    )
    vernacular_title: Optional[VernacularTitle] = field(
        default=None,
        metadata={
            "name": "VernacularTitle",
            "type": "Element",
        }
    )
    article_date: List[ArticleDate] = field(
        default_factory=list,
        metadata={
            "name": "ArticleDate",
            "type": "Element",
        }
    )
