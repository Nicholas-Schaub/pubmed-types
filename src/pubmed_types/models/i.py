from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Type
from .access_date import (
    Sub,
    Sup,
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
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "inf",
                    "type": Type["Inf"],
                },
                {
                    "name": "b",
                    "type": Type["B"],
                },
                {
                    "name": "u",
                    "type": Type["U"],
                },
                {
                    "name": "i",
                    "type": Type["I"],
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
            ),
        }
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
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "inf",
                    "type": Type["Inf"],
                },
                {
                    "name": "b",
                    "type": Type["B"],
                },
                {
                    "name": "u",
                    "type": Type["U"],
                },
                {
                    "name": "i",
                    "type": I,
                },
                {
                    "name": "sub",
                    "type": Sub,
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
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "inf",
                    "type": Type["Inf"],
                },
                {
                    "name": "b",
                    "type": Type["B"],
                },
                {
                    "name": "u",
                    "type": U,
                },
                {
                    "name": "i",
                    "type": I,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
            ),
        }
    )


@dataclass
class Inf:
    class Meta:
        name = "inf"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "inf",
                    "type": Type["Inf"],
                },
                {
                    "name": "b",
                    "type": B,
                },
                {
                    "name": "u",
                    "type": U,
                },
                {
                    "name": "i",
                    "type": I,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
            ),
        }
    )
