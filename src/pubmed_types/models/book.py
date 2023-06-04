from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional
from .author_list import AuthorList
from .beginning_date import BeginningDate
from .book_title import BookTitle
from .collection_title import CollectionTitle
from .elocation_id_1 import ElocationId1
from .ending_date import EndingDate
from .investigator_list import InvestigatorList
from .pub_date_1 import PubDate1
from .publisher_1 import Publisher1
from .volume_title import VolumeTitle


@dataclass
class Book:
    publisher: Optional[Publisher1] = field(
        default=None,
        metadata={
            "name": "Publisher",
            "type": "Element",
            "required": True,
        }
    )
    book_title: Optional[BookTitle] = field(
        default=None,
        metadata={
            "name": "BookTitle",
            "type": "Element",
            "required": True,
        }
    )
    pub_date: Optional[PubDate1] = field(
        default=None,
        metadata={
            "name": "PubDate",
            "type": "Element",
            "required": True,
        }
    )
    beginning_date: Optional[BeginningDate] = field(
        default=None,
        metadata={
            "name": "BeginningDate",
            "type": "Element",
        }
    )
    ending_date: Optional[EndingDate] = field(
        default=None,
        metadata={
            "name": "EndingDate",
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
    volume: Optional[str] = field(
        default=None,
        metadata={
            "name": "Volume",
            "type": "Element",
        }
    )
    volume_title: Optional[VolumeTitle] = field(
        default=None,
        metadata={
            "name": "VolumeTitle",
            "type": "Element",
        }
    )
    edition: Optional[str] = field(
        default=None,
        metadata={
            "name": "Edition",
            "type": "Element",
        }
    )
    collection_title: Optional[CollectionTitle] = field(
        default=None,
        metadata={
            "name": "CollectionTitle",
            "type": "Element",
        }
    )
    isbn: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Isbn",
            "type": "Element",
        }
    )
    elocation_id: List[ElocationId1] = field(
        default_factory=list,
        metadata={
            "name": "ELocationID",
            "type": "Element",
        }
    )
    medium: Optional[str] = field(
        default=None,
        metadata={
            "name": "Medium",
            "type": "Element",
        }
    )
    report_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReportNumber",
            "type": "Element",
        }
    )
