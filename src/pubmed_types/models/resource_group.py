from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional, Union
from .org.w3.xml.pkg_1998.namespace.lang_value import LangValue
from .resource_name import ResourceName
from .resource_wrap import ResourceWrap


@dataclass
class ResourceGroup:
    """
    <div> <h3>Resource Group</h3> </div>
    """
    class Meta:
        name = "resource-group"

    resource_name: List[ResourceName] = field(
        default_factory=list,
        metadata={
            "name": "resource-name",
            "type": "Element",
        }
    )
    resource_wrap: List[ResourceWrap] = field(
        default_factory=list,
        metadata={
            "name": "resource-wrap",
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
