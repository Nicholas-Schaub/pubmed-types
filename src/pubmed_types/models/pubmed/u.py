from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Type


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
                    "type": Type["Sup"],
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "u",
                    "type": Type["U"],
                },
            ),
        }
    )


@dataclass
class Sub:
    class Meta:
        name = "sub"

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
                    "type": Type["Sup"],
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "u",
                    "type": U,
                },
            ),
        }
    )


@dataclass
class Sup:
    class Meta:
        name = "sup"

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
                    "type": Type["Sup"],
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
