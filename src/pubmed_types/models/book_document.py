from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional
from .abstract_1 import Abstract1
from .article_id_list import ArticleIdList
from .article_title_1 import ArticleTitle1
from .author_list import AuthorList
from .book import Book
from .contribution_date import ContributionDate
from .date_revised import DateRevised
from .grant_list import GrantList
from .investigator_list import InvestigatorList
from .item_list import ItemList
from .keyword_list import KeywordList
from .location_label import LocationLabel
from .pagination import Pagination
from .pmid import Pmid
from .publication_type import PublicationType
from .reference_list import ReferenceList
from .sections import Sections
from .vernacular_title import VernacularTitle


@dataclass
class BookDocument:
    pmid: Optional[Pmid] = field(
        default=None,
        metadata={
            "name": "PMID",
            "type": "Element",
            "required": True,
        }
    )
    article_id_list: Optional[ArticleIdList] = field(
        default=None,
        metadata={
            "name": "ArticleIdList",
            "type": "Element",
            "required": True,
        }
    )
    book: Optional[Book] = field(
        default=None,
        metadata={
            "name": "Book",
            "type": "Element",
            "required": True,
        }
    )
    location_label: List[LocationLabel] = field(
        default_factory=list,
        metadata={
            "name": "LocationLabel",
            "type": "Element",
        }
    )
    article_title: Optional[ArticleTitle1] = field(
        default=None,
        metadata={
            "name": "ArticleTitle",
            "type": "Element",
        }
    )
    vernacular_title: Optional[VernacularTitle] = field(
        default=None,
        metadata={
            "name": "VernacularTitle",
            "type": "Element",
        }
    )
    pagination: Optional[Pagination] = field(
        default=None,
        metadata={
            "name": "Pagination",
            "type": "Element",
        }
    )
    language: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Language",
            "type": "Element",
        }
    )
    author_list: List[AuthorList] = field(
        default_factory=list,
        metadata={
            "name": "AuthorList",
            "type": "Element",
        }
    )
    investigator_list: Optional[InvestigatorList] = field(
        default=None,
        metadata={
            "name": "InvestigatorList",
            "type": "Element",
        }
    )
    publication_type: List[PublicationType] = field(
        default_factory=list,
        metadata={
            "name": "PublicationType",
            "type": "Element",
        }
    )
    abstract: Optional[Abstract1] = field(
        default=None,
        metadata={
            "name": "Abstract",
            "type": "Element",
        }
    )
    sections: Optional[Sections] = field(
        default=None,
        metadata={
            "name": "Sections",
            "type": "Element",
        }
    )
    keyword_list: List[KeywordList] = field(
        default_factory=list,
        metadata={
            "name": "KeywordList",
            "type": "Element",
        }
    )
    contribution_date: Optional[ContributionDate] = field(
        default=None,
        metadata={
            "name": "ContributionDate",
            "type": "Element",
        }
    )
    date_revised: Optional[DateRevised] = field(
        default=None,
        metadata={
            "name": "DateRevised",
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
    item_list: List[ItemList] = field(
        default_factory=list,
        metadata={
            "name": "ItemList",
            "type": "Element",
        }
    )
    reference_list: List[ReferenceList] = field(
        default_factory=list,
        metadata={
            "name": "ReferenceList",
            "type": "Element",
        }
    )
