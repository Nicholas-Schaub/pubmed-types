from enum import Enum


class PubMedPubDatePubStatus(Enum):
    RECEIVED = "received"
    ACCEPTED = "accepted"
    EPUBLISH = "epublish"
    PPUBLISH = "ppublish"
    REVISED = "revised"
    AHEADOFPRINT = "aheadofprint"
    RETRACTED = "retracted"
    ECOLLECTION = "ecollection"
    PMC = "pmc"
    PMCR = "pmcr"
    PUBMED = "pubmed"
    PUBMEDR = "pubmedr"
    PREMEDLINE = "premedline"
    MEDLINE = "medline"
    MEDLINER = "medliner"
    ENTREZ = "entrez"
    PMC_RELEASE = "pmc-release"
