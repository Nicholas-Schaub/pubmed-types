from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional, Union
from .access_date import (
    Ack,
    Address,
    Alternatives,
    Answer,
    AnswerSet,
    Array,
    BlockAlternatives,
    BoxedText,
    ChemStructWrap,
    Code,
    DefList,
    DispFormula,
    DispFormulaGroup,
    DispQuote,
    Explanation,
    Fig,
    FigGroup,
    FnGroup,
    Glossary,
    Graphic,
    Label,
    ListType,
    Media,
    Notes,
    P,
    Preformat,
    Question,
    QuestionWrap,
    QuestionWrapGroup,
    RefList,
    RelatedArticle,
    RelatedObject,
    Sec,
    SecMeta,
    Speech,
    Statement,
    SupplementaryMaterial,
    TableWrap,
    TableWrapGroup,
    Title,
    VerseGroup,
    X,
)
from .object_id import ObjectId
from .org.w3.pkg_1998.math.math_ml.math import Math
from .org.w3.xml.pkg_1998.namespace.lang_value import LangValue
from .tex_math import TexMath


@dataclass
class TransAbstract:
    """
    <div> <h3>Translated Abstract</h3> </div>
    """
    class Meta:
        name = "trans-abstract"

    object_id: List[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        }
    )
    sec_meta: Optional[SecMeta] = field(
        default=None,
        metadata={
            "name": "sec-meta",
            "type": "Element",
        }
    )
    label: Optional[Label] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    title: Optional[Title] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    address: List[Address] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    alternatives: List[Alternatives] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    answer: List[Answer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    answer_set: List[AnswerSet] = field(
        default_factory=list,
        metadata={
            "name": "answer-set",
            "type": "Element",
        }
    )
    array: List[Array] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    block_alternatives: List[BlockAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "block-alternatives",
            "type": "Element",
        }
    )
    boxed_text: List[BoxedText] = field(
        default_factory=list,
        metadata={
            "name": "boxed-text",
            "type": "Element",
        }
    )
    chem_struct_wrap: List[ChemStructWrap] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct-wrap",
            "type": "Element",
        }
    )
    code: List[Code] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    explanation: List[Explanation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    fig: List[Fig] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    fig_group: List[FigGroup] = field(
        default_factory=list,
        metadata={
            "name": "fig-group",
            "type": "Element",
        }
    )
    graphic: List[Graphic] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    media: List[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    preformat: List[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    question: List[Question] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    question_wrap: List[QuestionWrap] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap",
            "type": "Element",
        }
    )
    question_wrap_group: List[QuestionWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap-group",
            "type": "Element",
        }
    )
    supplementary_material: List[SupplementaryMaterial] = field(
        default_factory=list,
        metadata={
            "name": "supplementary-material",
            "type": "Element",
        }
    )
    table_wrap: List[TableWrap] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
        }
    )
    table_wrap_group: List[TableWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap-group",
            "type": "Element",
        }
    )
    disp_formula: List[DispFormula] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
        }
    )
    disp_formula_group: List[DispFormulaGroup] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula-group",
            "type": "Element",
        }
    )
    def_list: List[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
        }
    )
    list_value: List[ListType] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
        }
    )
    tex_math: List[TexMath] = field(
        default_factory=list,
        metadata={
            "name": "tex-math",
            "type": "Element",
        }
    )
    math: List[Math] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1998/Math/MathML",
        }
    )
    p: List[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    related_article: List[RelatedArticle] = field(
        default_factory=list,
        metadata={
            "name": "related-article",
            "type": "Element",
        }
    )
    related_object: List[RelatedObject] = field(
        default_factory=list,
        metadata={
            "name": "related-object",
            "type": "Element",
        }
    )
    ack: List[Ack] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    disp_quote: List[DispQuote] = field(
        default_factory=list,
        metadata={
            "name": "disp-quote",
            "type": "Element",
        }
    )
    speech: List[Speech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    statement: List[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    verse_group: List[VerseGroup] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
        }
    )
    x: List[X] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    sec: List[Sec] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    notes: List[Notes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    fn_group: List[FnGroup] = field(
        default_factory=list,
        metadata={
            "name": "fn-group",
            "type": "Element",
        }
    )
    glossary: List[Glossary] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    ref_list: List[RefList] = field(
        default_factory=list,
        metadata={
            "name": "ref-list",
            "type": "Element",
        }
    )
    abstract_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "abstract-type",
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
