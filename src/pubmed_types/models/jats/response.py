from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional, Union
from .back import Back
from .body import Body
from .floats_group import FloatsGroup
from .front import Front
from .front_stub import FrontStub
from .org.w3.xml.pkg_1998.namespace.lang_value import LangValue
from .processing_meta import ProcessingMeta


@dataclass
class Response:
    """
    <div> <h3>Response</h3> </div>
    """
    class Meta:
        name = "response"

    processing_meta: Optional[ProcessingMeta] = field(
        default=None,
        metadata={
            "name": "processing-meta",
            "type": "Element",
        }
    )
    front: Optional[Front] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    front_stub: Optional[FrontStub] = field(
        default=None,
        metadata={
            "name": "front-stub",
            "type": "Element",
        }
    )
    body: Optional[Body] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    back: Optional[Back] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    floats_group: Optional[FloatsGroup] = field(
        default=None,
        metadata={
            "name": "floats-group",
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    response_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "response-type",
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
