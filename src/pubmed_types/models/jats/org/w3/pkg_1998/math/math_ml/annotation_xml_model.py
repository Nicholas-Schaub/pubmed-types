from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


@dataclass
class AnnotationXmlModel:
    class Meta:
        name = "annotation-xml.model"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
