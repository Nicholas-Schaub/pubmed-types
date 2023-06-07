from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional
from .resource_id import ResourceId
from .resource_name import ResourceName


@dataclass
class ResourceWrap:
    """
    <div> <h3>Resource Wrap</h3> </div>
    """
    class Meta:
        name = "resource-wrap"

    resource_name: Optional[ResourceName] = field(
        default=None,
        metadata={
            "name": "resource-name",
            "type": "Element",
            "required": True,
        }
    )
    resource_id: List[ResourceId] = field(
        default_factory=list,
        metadata={
            "name": "resource-id",
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
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
