from enum import Enum


class PubDatePubStatus(Enum):
    RECEIVED = "received"
    ACCEPTED = "accepted"
    EPUBLISH = "epublish"
    PPUBLISH = "ppublish"
    REVISED = "revised"
    AHEADOFPRINT = "aheadofprint"
    ECOLLECTION = "ecollection"
    PMC = "pmc"
    PMCR = "pmcr"
    PUBMED = "pubmed"
    PUBMEDR = "pubmedr"
    PREMEDLINE = "premedline"
    MEDLINE = "medline"
    MEDLINER = "medliner"
