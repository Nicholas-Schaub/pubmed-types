from enum import Enum


class ArticleIdIdType(Enum):
    DOI = "doi"
    PII = "pii"
    PMCPID = "pmcpid"
    PMPID = "pmpid"
    PMC = "pmc"
    MID = "mid"
    SICI = "sici"
    PUBMED = "pubmed"
    MEDLINE = "medline"
    PMCID = "pmcid"
    PMCBOOK = "pmcbook"
    BOOKACCESSION = "bookaccession"
