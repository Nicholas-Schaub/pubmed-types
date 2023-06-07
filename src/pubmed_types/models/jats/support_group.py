from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional, Union
from .contributed_resource_group import ContributedResourceGroup
from .funding_group import FundingGroup
from .org.w3.xml.pkg_1998.namespace.lang_value import LangValue


@dataclass
class SupportGroup:
    """
    <div> <h3>Support Group</h3> </div>
    """
    class Meta:
        name = "support-group"

    funding_group: List[FundingGroup] = field(
        default_factory=list,
        metadata={
            "name": "funding-group",
            "type": "Element",
        }
    )
    contributed_resource_group: List[ContributedResourceGroup] = field(
        default_factory=list,
        metadata={
            "name": "contributed-resource-group",
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
