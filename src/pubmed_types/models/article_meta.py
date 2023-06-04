from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional
from .access_date import (
    Abstract2,
    Aff,
    AffAlternatives,
    ContribGroup,
    Email,
    ExtLink,
    Isbn,
    Issue,
    IssuePart,
    IssueTitle,
    KwdGroup,
    Permissions,
    Product,
    RelatedArticle,
    RelatedObject,
    Supplement,
    SupplementaryMaterial,
    Uri,
    Volume,
    VolumeId,
    VolumeSeries,
    X,
)
from .article_categories import ArticleCategories
from .article_id import ArticleId
from .article_version import ArticleVersion
from .article_version_alternatives import ArticleVersionAlternatives
from .author_notes import AuthorNotes
from .conference import Conference
from .counts import Counts
from .custom_meta_group import CustomMetaGroup
from .elocation_id import ElocationId
from .fpage import Fpage
from .funding_group import FundingGroup
from .history_2 import History2
from .issue_id import IssueId
from .issue_sponsor import IssueSponsor
from .issue_title_group import IssueTitleGroup
from .lpage import Lpage
from .page_range import PageRange
from .pub_date_2 import PubDate2
from .pub_date_not_available import PubDateNotAvailable
from .pub_history import PubHistory
from .self_uri import SelfUri
from .support_group import SupportGroup
from .title_group import TitleGroup
from .trans_abstract import TransAbstract
from .volume_issue_group import VolumeIssueGroup


@dataclass
class ArticleMeta:
    """
    <div> <h3>Article Metadata</h3> </div>
    """
    class Meta:
        name = "article-meta"

    article_id: List[ArticleId] = field(
        default_factory=list,
        metadata={
            "name": "article-id",
            "type": "Element",
        }
    )
    article_version: Optional[ArticleVersion] = field(
        default=None,
        metadata={
            "name": "article-version",
            "type": "Element",
        }
    )
    article_version_alternatives: Optional[ArticleVersionAlternatives] = field(
        default=None,
        metadata={
            "name": "article-version-alternatives",
            "type": "Element",
        }
    )
    article_categories: Optional[ArticleCategories] = field(
        default=None,
        metadata={
            "name": "article-categories",
            "type": "Element",
        }
    )
    title_group: Optional[TitleGroup] = field(
        default=None,
        metadata={
            "name": "title-group",
            "type": "Element",
        }
    )
    contrib_group: List[ContribGroup] = field(
        default_factory=list,
        metadata={
            "name": "contrib-group",
            "type": "Element",
        }
    )
    aff: List[Aff] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    aff_alternatives: List[AffAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "aff-alternatives",
            "type": "Element",
        }
    )
    x: List[X] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    author_notes: Optional[AuthorNotes] = field(
        default=None,
        metadata={
            "name": "author-notes",
            "type": "Element",
        }
    )
    pub_date: List[PubDate2] = field(
        default_factory=list,
        metadata={
            "name": "pub-date",
            "type": "Element",
        }
    )
    pub_date_not_available: Optional[PubDateNotAvailable] = field(
        default=None,
        metadata={
            "name": "pub-date-not-available",
            "type": "Element",
        }
    )
    volume: List[Volume] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    volume_id: List[VolumeId] = field(
        default_factory=list,
        metadata={
            "name": "volume-id",
            "type": "Element",
        }
    )
    volume_series: Optional[VolumeSeries] = field(
        default=None,
        metadata={
            "name": "volume-series",
            "type": "Element",
        }
    )
    issue: List[Issue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    issue_id: List[IssueId] = field(
        default_factory=list,
        metadata={
            "name": "issue-id",
            "type": "Element",
        }
    )
    issue_title: List[IssueTitle] = field(
        default_factory=list,
        metadata={
            "name": "issue-title",
            "type": "Element",
        }
    )
    issue_title_group: List[IssueTitleGroup] = field(
        default_factory=list,
        metadata={
            "name": "issue-title-group",
            "type": "Element",
        }
    )
    issue_sponsor: List[IssueSponsor] = field(
        default_factory=list,
        metadata={
            "name": "issue-sponsor",
            "type": "Element",
        }
    )
    issue_part: Optional[IssuePart] = field(
        default=None,
        metadata={
            "name": "issue-part",
            "type": "Element",
        }
    )
    volume_issue_group: List[VolumeIssueGroup] = field(
        default_factory=list,
        metadata={
            "name": "volume-issue-group",
            "type": "Element",
        }
    )
    isbn: List[Isbn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    supplement: Optional[Supplement] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fpage: Optional[Fpage] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    lpage: Optional[Lpage] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    page_range: Optional[PageRange] = field(
        default=None,
        metadata={
            "name": "page-range",
            "type": "Element",
        }
    )
    elocation_id: Optional[ElocationId] = field(
        default=None,
        metadata={
            "name": "elocation-id",
            "type": "Element",
        }
    )
    email: List[Email] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    ext_link: List[ExtLink] = field(
        default_factory=list,
        metadata={
            "name": "ext-link",
            "type": "Element",
        }
    )
    uri: List[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    product: List[Product] = field(
        default_factory=list,
        metadata={
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
    history: Optional[History2] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    pub_history: Optional[PubHistory] = field(
        default=None,
        metadata={
            "name": "pub-history",
            "type": "Element",
        }
    )
    permissions: Optional[Permissions] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    self_uri: List[SelfUri] = field(
        default_factory=list,
        metadata={
            "name": "self-uri",
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
    abstract: List[Abstract2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    trans_abstract: List[TransAbstract] = field(
        default_factory=list,
        metadata={
            "name": "trans-abstract",
            "type": "Element",
        }
    )
    kwd_group: List[KwdGroup] = field(
        default_factory=list,
        metadata={
            "name": "kwd-group",
            "type": "Element",
        }
    )
    funding_group: List[FundingGroup] = field(
        default_factory=list,
        metadata={
            "name": "funding-group",
            "type": "Element",
        }
    )
    support_group: List[SupportGroup] = field(
        default_factory=list,
        metadata={
            "name": "support-group",
            "type": "Element",
        }
    )
    conference: List[Conference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    counts: Optional[Counts] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    custom_meta_group: Optional[CustomMetaGroup] = field(
        default=None,
        metadata={
            "name": "custom-meta-group",
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
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
