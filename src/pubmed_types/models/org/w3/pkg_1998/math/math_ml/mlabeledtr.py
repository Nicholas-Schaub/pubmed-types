from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Dict, List, Optional, Union
from .columnalignstyle import Columnalignstyle
from .mlabeledtr_rowalign import MlabeledtrRowalign
from .mlabeledtr_value import MlabeledtrValue
from .mtd import Mtd

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


@dataclass
class Mlabeledtr:
    class Meta:
        name = "mlabeledtr"
        namespace = "http://www.w3.org/1998/Math/MathML"

    mtd: List[Mtd] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    xref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: List[str] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Attribute",
            "tokens": True,
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    other: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )
    mathcolor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        }
    )
    mathbackground: Optional[Union[str, MlabeledtrValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        }
    )
    rowalign: Optional[MlabeledtrRowalign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    columnalign: List[Columnalignstyle] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    groupalign: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"(\s*\{\s*(left|center|right|decimalpoint)(\s+(left|center|right|decimalpoint))*\})*\s*",
        }
    )
