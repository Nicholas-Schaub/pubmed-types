from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional, Union
from .access_date import (
    ConfAcronym,
    ConfDate,
    ConfLoc,
    ConfName,
    ConfSponsor,
    X,
)
from .conf_num import ConfNum
from .conf_theme import ConfTheme
from .org.w3.pkg_1999.xlink.actuate_value import ActuateValue
from .org.w3.pkg_1999.xlink.show_value import ShowValue
from .org.w3.pkg_1999.xlink.type_value import TypeValue
from .org.w3.xml.pkg_1998.namespace.lang_value import LangValue
from .string_conf import StringConf


@dataclass
class Conference:
    """
    <div> <h3>Conference Information</h3> </div>
    """
    class Meta:
        name = "conference"

    conf_date: List[ConfDate] = field(
        default_factory=list,
        metadata={
            "name": "conf-date",
            "type": "Element",
        }
    )
    conf_name: List[ConfName] = field(
        default_factory=list,
        metadata={
            "name": "conf-name",
            "type": "Element",
        }
    )
    conf_num: List[ConfNum] = field(
        default_factory=list,
        metadata={
            "name": "conf-num",
            "type": "Element",
        }
    )
    conf_loc: List[ConfLoc] = field(
        default_factory=list,
        metadata={
            "name": "conf-loc",
            "type": "Element",
        }
    )
    conf_sponsor: List[ConfSponsor] = field(
        default_factory=list,
        metadata={
            "name": "conf-sponsor",
            "type": "Element",
        }
    )
    conf_theme: List[ConfTheme] = field(
        default_factory=list,
        metadata={
            "name": "conf-theme",
            "type": "Element",
        }
    )
    conf_acronym: List[ConfAcronym] = field(
        default_factory=list,
        metadata={
            "name": "conf-acronym",
            "type": "Element",
        }
    )
    string_conf: List[StringConf] = field(
        default_factory=list,
        metadata={
            "name": "string-conf",
            "type": "Element",
        }
    )
    x: List[X] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
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
