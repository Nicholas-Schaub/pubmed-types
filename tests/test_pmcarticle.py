import pytest
import gzip
import urllib.request as request
from contextlib import closing
from pathlib import Path

from pubmed_types import pubmed_article_set


@pytest.fixture
def article_set() -> Path:
    source = (
        "ftp://ftp.ncbi.nlm.nih.gov" + "/pubmed/updatefiles" + "/pubmed23n1367.xml.gz"
    )
    destination = Path("downloads").joinpath("pubmed23n1300.xml")
    destination.parent.mkdir(exist_ok=True)

    if not destination.exists():
        with closing(request.urlopen(source)) as url:
            with gzip.GzipFile(fileobj=url, mode="rb") as fr:
                with open(destination, mode="wb") as fw:
                    fw.write(fr.read())

    return destination


def test_parse(article_set):
    result = pubmed_article_set(article_set)
