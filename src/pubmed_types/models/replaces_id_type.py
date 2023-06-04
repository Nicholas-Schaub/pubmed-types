from enum import Enum


class ReplacesIdType(Enum):
    DOI = "doi"
    PII = "pii"
    PMCPID = "pmcpid"
    PMPID = "pmpid"
    PUBMED = "pubmed"
    MEDLINE = "medline"
    PMCID = "pmcid"
