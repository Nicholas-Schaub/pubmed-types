# pubmed-types (v0.2.0)

<p align="center">
    <img src="https://img.shields.io/pypi/dm/pubmed-types?style=flat-square" />
    <img src="https://img.shields.io/pypi/l/pubmed-types?style=flat-square"/>
    <img src="https://img.shields.io/pypi/v/pubmed-types?style=flat-square"/>
    <a href="https://github.com/tefra/xsdata-pydantic">
        <img alt="Built with: xsdata-pydantic" src="https://img.shields.io/badge/Built%20with-xsdata--pydantic-blue">
    </a>
    <a href="https://github.com/dbrgn/coverage-badge">
        <img src="./images/coverage.svg">
    </a>
</p>

## Introduction

A complete implementation of the XML schema for PMC Open Access articles and Pubmed
article sets (citations).

This package helps to parse PubMed XML data into Pydantic models. This validates the
input xml data and provides typehints for working with the complex XML structures
present in PubMed data.

## Most Recent Changes

* **Breaking Change:** The `parse_pubmed_xml` is replaced by `pmc_article` and `pubmed_article_set`.
* More test coverage
* Pubmed Articles can now parse MathML
* Restructured code to separate out `jats` (pmc open access articles) and `pubmed` (pubmed article set)
* One unit test with 99% coverage
* Added [CHANGELOG.md](CHANGELOG.md)

## Why do I need this?

PubMed keeps track of 10s of millions of research data, and a complex XML structure is
used to store it. Parsing XML on its own is challenging enough. Add to it the feature
rich data inside of each citation, and you will find yourself with hours or days of
navigating the XML structure.

The approach here was to autogenerate Pydantic classes to parse the XML using the
`xsdata-pydantic` tool. This approach has the benefit of making sure every piece of data
is parsed properly, and an error is thrown is something is missing or incorrect. Instead
of using dictionaries to hold the data, Pydantic classes have the benefit of providing
type hints with tab completion for IDEs, making it easier to navigate the complex
structure of the citation data.

## How do I use it?

It is possible to use `xsdata-pydantic` and the autogenerated classes directly to parse
an XML file, but we provide a convenience function to easily open PubMed XMl citations
and PMC open access articles.

### Example 1: A PMC Open Access Article

```python
import tarfile
import urllib.request as request
from contextlib import closing
from pathlib import Path

from pubmed_types import pmc_article

# Input file source and output file destination
source = (
    "ftp://ftp.ncbi.nlm.nih.gov"
    + "/pub/pmc/oa_bulk/oa_comm/xml"
    + "/oa_comm_xml.incr.2023-03-21.tar.gz"
)
destination = Path("downloads")
destination.mkdir(exist_ok=True)

# 1. Get an open access article dataset from the FTP server
with closing(request.urlopen(source)) as url:
    with tarfile.open(fileobj=url, mode="r:gz") as fr:
        fr.extractall(destination)

# 2. Parse the file
file_path = destination.joinpath("PMC009xxxxxx").joinpath("PMC9970662.xml")
full_text = pmc_article(file_path)

# 3. Print out the article title
print(f"Title: {full_text.front.article_meta.title_group.article_title.content[0]}")
```

Output:

```bash
Title: Lactate as a myokine and exerkine: drivers and signals of physiology and metabolism
```

### Example 2: A Pubmed baseline citation file

```python
import gzip
import urllib.request as request
from contextlib import closing
from pathlib import Path

from pubmed_types import pubmed_article_set

# Input file source and output file destination
source = "ftp://ftp.ncbi.nlm.nih.gov" + "/pubmed/updatefiles" + "/pubmed23n1168.xml.gz"
destination = Path("downloads").joinpath("pubmed23n1168.xml")
destination.parent.mkdir(exist_ok=True)

# 1. Get a pubmed citation daily update file from the FTP server
with closing(request.urlopen(source)) as url:
    with gzip.GzipFile(fileobj=url, mode="rb") as fr:
        with open(destination, mode="wb") as fw:
            fw.write(fr.read())

# 2. Parse the file
article_set = pubmed_article_set(destination)

# 3. Get the number of citations in the file
print(f"Number of citations: {len(article_set.pubmed_article)}")
print(
    f"{article_set.pubmed_article[0].medline_citation.article.article_title.content[0]}"
)
```

Output:

```bash
Number of citations: 2543
A Patent and Pattern Mother.
```

## FAQ

### Why does it take so long to parse a pubmed citation set

There is a lot of data, and the schema is deep and complex.

### Why are the return structures so complicated?

The return structures are a direct reflection of the XML format defined by the NLM. In
the future some utility classes might be made for common components (title, authors,
etc), but for now this is intended to be an unbiased way of parsing the XML.
