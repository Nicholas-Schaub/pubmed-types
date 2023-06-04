from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional, Union
from .award_group import AwardGroup
from .org.w3.xml.pkg_1998.namespace.lang_value import LangValue
from .resource_group import ResourceGroup
from .support_description import SupportDescription


@dataclass
class ContributedResourceGroup:
    """
    <div> <h3>Contributed Resource Group</h3> </div>
    """
    class Meta:
        name = "contributed-resource-group"

    award_group: List[AwardGroup] = field(
        default_factory=list,
        metadata={
            "name": "award-group",
            "type": "Element",
        }
    )
    support_description: List[SupportDescription] = field(
        default_factory=list,
        metadata={
            "name": "support-description",
            "type": "Element",
        }
    )
    resource_group: List[ResourceGroup] = field(
        default_factory=list,
        metadata={
            "name": "resource-group",
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    resource_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "resource-type",
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
