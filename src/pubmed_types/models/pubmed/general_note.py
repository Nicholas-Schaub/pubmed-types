from dataclasses import field
from pydantic.dataclasses import dataclass
from .general_note_owner import GeneralNoteOwner


@dataclass
class GeneralNote:
    owner: GeneralNoteOwner = field(
        default=GeneralNoteOwner.NLM,
        metadata={
            "name": "Owner",
            "type": "Attribute",
            "required": True,
        }
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
