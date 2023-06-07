from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List
from .personal_name_subject import PersonalNameSubject


@dataclass
class PersonalNameSubjectList:
    personal_name_subject: List[PersonalNameSubject] = field(
        default_factory=list,
        metadata={
            "name": "PersonalNameSubject",
            "type": "Element",
            "min_occurs": 1,
        }
    )
