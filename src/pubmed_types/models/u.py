from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Type
from .access_date import (
    Sub,
    Sup,
)


@dataclass
class U:
    class Meta:
        name = "u"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "b",
                    "type": Type["B"],
                },
                {
                    "name": "i",
                    "type": Type["I"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "u",
                    "type": Type["U"],
                },
            ),
        }
    )


@dataclass
class I:
    class Meta:
        name = "i"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "b",
                    "type": Type["B"],
                },
                {
                    "name": "i",
                    "type": Type["I"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "u",
                    "type": U,
                },
            ),
        }
    )


@dataclass
class B:
    class Meta:
        name = "b"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "b",
                    "type": Type["B"],
                },
                {
                    "name": "i",
                    "type": I,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "u",
                    "type": U,
                },
            ),
        }
    )
