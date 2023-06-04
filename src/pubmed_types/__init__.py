__version__ = "0.1.1"

from pathlib import Path
from typing import Union

from xsdata_pydantic.bindings import XmlParser

from .models.article_2 import Article2 as PMCArticle
from .models.pubmed_article_set import PubmedArticleSet


def parse_pubmed_xml(xml: Union[Path, str]) -> Union[PMCArticle, PubmedArticleSet]:
    parser = XmlParser()

    try:
        result = parser.parse(xml, PMCArticle)
    except:
        result = parser.parse(xml, PubmedArticleSet)

    return result
