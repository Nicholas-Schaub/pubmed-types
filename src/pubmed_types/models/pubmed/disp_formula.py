from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional
from ..jats.org.w3.pkg_1998.math.math_ml.math import Math


@dataclass
class DispFormula:
    math: Optional[Math] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
			"namespace": "http://www.w3.org/1998/Math/MathML",
        }
    )
