from enum import Enum


class MedlineCitationStatus(Enum):
    COMPLETED = "Completed"
    IN_PROCESS = "In-Process"
    PUB_MED_NOT_MEDLINE = "PubMed-not-MEDLINE"
    IN_DATA_REVIEW = "In-Data-Review"
    PUBLISHER = "Publisher"
    MEDLINE = "MEDLINE"
    OLDMEDLINE = "OLDMEDLINE"
