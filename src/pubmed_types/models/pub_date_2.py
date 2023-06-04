from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional, Union
from .access_date import (
    StringDate,
    X,
)
from .day import Day
from .era import Era
from .month import Month
from .org.w3.xml.pkg_1998.namespace.lang_value import LangValue
from .season import Season
from .year import Year


@dataclass
class PubDate2:
    """
    <div> <h3>Publication Date</h3> </div>
    """
    class Meta:
        name = "pub-date"

    day: List[Day] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    era: List[Era] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    month: List[Month] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    season: List[Season] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    year: List[Year] = field(
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
    x: List[X] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    assigning_authority: Optional[str] = field(
        default=None,
        metadata={
            "name": "assigning-authority",
            "type": "Attribute",
        }
    )
    calendar: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    date_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "date-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    iso_8601_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "iso-8601-date",
            "type": "Attribute",
        }
    )
    pub_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "pub-type",
            "type": "Attribute",
        }
    )
    publication_format: Optional[str] = field(
        default=None,
        metadata={
            "name": "publication-format",
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
