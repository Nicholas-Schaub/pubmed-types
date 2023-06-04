from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional, Union
from .access_date import (
    AwardId,
    FundingSource,
)
from .award_desc import AwardDesc
from .award_name import AwardName
from .org.w3.pkg_1999.xlink.actuate_value import ActuateValue
from .org.w3.pkg_1999.xlink.show_value import ShowValue
from .org.w3.pkg_1999.xlink.type_value import TypeValue
from .org.w3.xml.pkg_1998.namespace.lang_value import LangValue
from .principal_award_recipient import PrincipalAwardRecipient
from .principal_investigator import PrincipalInvestigator
from .support_source import SupportSource


@dataclass
class AwardGroup:
    """
    <div> <h3>Award Group</h3> </div>
    """
    class Meta:
        name = "award-group"

    funding_source: List[FundingSource] = field(
        default_factory=list,
        metadata={
            "name": "funding-source",
            "type": "Element",
        }
    )
    support_source: List[SupportSource] = field(
        default_factory=list,
        metadata={
            "name": "support-source",
            "type": "Element",
        }
    )
    award_id: List[AwardId] = field(
        default_factory=list,
        metadata={
            "name": "award-id",
            "type": "Element",
        }
    )
    award_name: Optional[AwardName] = field(
        default=None,
        metadata={
            "name": "award-name",
            "type": "Element",
        }
    )
    award_desc: Optional[AwardDesc] = field(
        default=None,
        metadata={
            "name": "award-desc",
            "type": "Element",
        }
    )
    principal_award_recipient: List[PrincipalAwardRecipient] = field(
        default_factory=list,
        metadata={
            "name": "principal-award-recipient",
            "type": "Element",
        }
    )
    principal_investigator: List[PrincipalInvestigator] = field(
        default_factory=list,
        metadata={
            "name": "principal-investigator",
            "type": "Element",
        }
    )
    award_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "award-type",
            "type": "Attribute",
        }
    )
    hreflang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    actuate: Optional[ActuateValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    type: TypeValue = field(
        init=False,
        default=TypeValue.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
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
