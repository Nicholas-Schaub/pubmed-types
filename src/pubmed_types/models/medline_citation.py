from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional
from .article_1 import Article1
from .chemical_list import ChemicalList
from .coi_statement import CoiStatement
from .comments_corrections_list import CommentsCorrectionsList
from .date_completed import DateCompleted
from .date_revised import DateRevised
from .gene_symbol_list import GeneSymbolList
from .general_note import GeneralNote
from .investigator_list import InvestigatorList
from .keyword_list import KeywordList
from .medline_citation_owner import MedlineCitationOwner
from .medline_citation_status import MedlineCitationStatus
from .medline_journal_info import MedlineJournalInfo
from .mesh_heading_list import MeshHeadingList
from .other_abstract import OtherAbstract
from .other_id import OtherId
from .personal_name_subject_list import PersonalNameSubjectList
from .pmid import Pmid
from .suppl_mesh_list import SupplMeshList


@dataclass
class MedlineCitation:
    owner: MedlineCitationOwner = field(
        default=MedlineCitationOwner.NLM,
        metadata={
            "name": "Owner",
            "type": "Attribute",
            "required": True,
        }
    )
    indexing_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "IndexingMethod",
            "type": "Attribute",
        }
    )
    version_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "VersionDate",
            "type": "Attribute",
        }
    )
    version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "VersionID",
            "type": "Attribute",
        }
    )
    status: Optional[MedlineCitationStatus] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        }
    )
    pmid: Optional[Pmid] = field(
        default=None,
        metadata={
            "name": "PMID",
            "type": "Element",
            "required": True,
        }
    )
    date_completed: Optional[DateCompleted] = field(
        default=None,
        metadata={
            "name": "DateCompleted",
            "type": "Element",
        }
    )
    date_revised: Optional[DateRevised] = field(
        default=None,
        metadata={
            "name": "DateRevised",
            "type": "Element",
        }
    )
    article: Optional[Article1] = field(
        default=None,
        metadata={
            "name": "Article",
            "type": "Element",
            "required": True,
        }
    )
    medline_journal_info: Optional[MedlineJournalInfo] = field(
        default=None,
        metadata={
            "name": "MedlineJournalInfo",
            "type": "Element",
            "required": True,
        }
    )
    chemical_list: Optional[ChemicalList] = field(
        default=None,
        metadata={
            "name": "ChemicalList",
            "type": "Element",
        }
    )
    suppl_mesh_list: Optional[SupplMeshList] = field(
        default=None,
        metadata={
            "name": "SupplMeshList",
            "type": "Element",
        }
    )
    citation_subset: List[str] = field(
        default_factory=list,
        metadata={
            "name": "CitationSubset",
            "type": "Element",
        }
    )
    comments_corrections_list: Optional[CommentsCorrectionsList] = field(
        default=None,
        metadata={
            "name": "CommentsCorrectionsList",
            "type": "Element",
        }
    )
    gene_symbol_list: Optional[GeneSymbolList] = field(
        default=None,
        metadata={
            "name": "GeneSymbolList",
            "type": "Element",
        }
    )
    mesh_heading_list: Optional[MeshHeadingList] = field(
        default=None,
        metadata={
            "name": "MeshHeadingList",
            "type": "Element",
        }
    )
    number_of_references: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumberOfReferences",
            "type": "Element",
        }
    )
    personal_name_subject_list: Optional[PersonalNameSubjectList] = field(
        default=None,
        metadata={
            "name": "PersonalNameSubjectList",
            "type": "Element",
        }
    )
    other_id: List[OtherId] = field(
        default_factory=list,
        metadata={
            "name": "OtherID",
            "type": "Element",
        }
    )
    other_abstract: List[OtherAbstract] = field(
        default_factory=list,
        metadata={
            "name": "OtherAbstract",
            "type": "Element",
        }
    )
    keyword_list: List[KeywordList] = field(
        default_factory=list,
        metadata={
            "name": "KeywordList",
            "type": "Element",
        }
    )
    coi_statement: Optional[CoiStatement] = field(
        default=None,
        metadata={
            "name": "CoiStatement",
            "type": "Element",
        }
    )
    space_flight_mission: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SpaceFlightMission",
            "type": "Element",
        }
    )
    investigator_list: Optional[InvestigatorList] = field(
        default=None,
        metadata={
            "name": "InvestigatorList",
            "type": "Element",
        }
    )
    general_note: List[GeneralNote] = field(
        default_factory=list,
        metadata={
            "name": "GeneralNote",
            "type": "Element",
        }
    )
