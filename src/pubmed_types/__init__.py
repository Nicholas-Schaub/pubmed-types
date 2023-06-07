__version__ = "0.2.0-dev0"

from pathlib import Path
from typing import Union

from xsdata_pydantic.bindings import XmlParser

from .models.jats.article import Article as PMCArticle
from .models.pubmed.pubmed_article_set import PubmedArticleSet


def pmc_article(xml: Union[Path, str]) -> PMCArticle:
    parser = XmlParser()

    result = parser.parse(xml, PMCArticle)

    return result


def pubmed_article_set(xml: Union[Path, str]) -> PubmedArticleSet:
    parser = XmlParser()

    result = parser.parse(xml, PubmedArticleSet)

    return result
