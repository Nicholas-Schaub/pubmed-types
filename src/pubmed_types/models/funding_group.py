from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional, Union
from .access_date import OpenAccess
from .award_group import AwardGroup
from .funding_statement import FundingStatement
from .org.w3.xml.pkg_1998.namespace.lang_value import LangValue


@dataclass
class FundingGroup:
    """
    <div> <h3>Funding Group</h3> </div>
    """
    class Meta:
        name = "funding-group"

    award_group: List[AwardGroup] = field(
        default_factory=list,
        metadata={
            "name": "award-group",
            "type": "Element",
        }
    )
    funding_statement: List[FundingStatement] = field(
        default_factory=list,
        metadata={
            "name": "funding-statement",
            "type": "Element",
        }
    )
    open_access: List[OpenAccess] = field(
        default_factory=list,
        metadata={
            "name": "open-access",
            "type": "Element",
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
