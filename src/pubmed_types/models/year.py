from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional, Union
from .org.w3.xml.pkg_1998.namespace.lang_value import LangValue


@dataclass
class Year:
    """
    <div> <h3>Year</h3> </div>
    """
    class Meta:
        name = "year"

    calendar: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
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
        }
    )
