from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional, Union
from .org.w3.xml.pkg_1998.namespace.lang_value import LangValue


@dataclass
class MilestoneEnd:
    """
    <div> <h3>Milestone End</h3> </div>
    """
    class Meta:
        name = "milestone-end"

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
    rationale: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rid: Optional[str] = field(
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
