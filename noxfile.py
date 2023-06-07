import ssl
import urllib.request as request
import zipfile
from contextlib import closing
from pathlib import Path
from shutil import rmtree

import nox


@nox.session
def generate_packages(session):
    session.install("requests", "xsdata-pydantic[cli,lxml,soap]")

    # Get the article schema
    base_path = Path("downloads/schemas")
    base_path.mkdir(exist_ok=True, parents=True)

    jats_url = "https://ftp.ncbi.nih.gov/pub/jats/archiving/1.3/xsd/"
    jats = "JATS-Archiving-1-3-MathML3-XSD.zip"

    with closing(request.urlopen(jats_url + jats)) as url:
        with open(base_path.joinpath(jats), "wb") as fw:
            fw.write(url.read())

    with zipfile.ZipFile(base_path.joinpath(jats)) as fr:
        fr.extractall(base_path)

    # Get the citation schema
    pubmed_url = "http://dtd.nlm.nih.gov/ncbi/pubmed/out/180601/"
    pubmed = "pubmed_180601.zip"

    with closing(request.urlopen(pubmed_url + pubmed)) as url:
        with open(base_path.joinpath(pubmed), "wb") as fw:
            fw.write(url.read())

    with zipfile.ZipFile(base_path.joinpath(pubmed)) as fr:
        fr.extractall(base_path)

    # Modify module-ali.xsd because it has a bad group specifier
    modified = []
    remove_line = '<xsd:group ref="license-ref-model"/>'
    with open(
        "downloads/schemas/JATS-Archiving-1-3-MathML3-XSD/standard-modules/module-ali.xsd"
    ) as fr:
        for line in fr:
            if remove_line in line:
                continue
            else:
                modified.append(line)

    with open(
        "downloads/schemas/JATS-Archiving-1-3-MathML3-XSD/standard-modules/module-ali.xsd",
        "w",
    ) as fw:
        fw.writelines(modified)

    with open("downloads/schemas/180601/mathml-in-pubmed.mod", "w") as fw:
        fw.writelines(modified)

    # Get the latest pubmed dtd
    with closing(
        request.urlopen("https://dtd.nlm.nih.gov/ncbi/pubmed/out/pubmed_230101.dtd")
    ) as url:
        with open("downloads/schemas/180601/pubmed_230101.dtd", "wb") as fw:
            fw.write(url.read())

    # Generate the models
    session.run(
        "xsdata",
        "downloads/schemas/JATS-Archiving-1-3-MathML3-XSD/"
        + "JATS-archivearticle1-3-mathml3.xsd",
        "--output",
        "pydantic",
        "--package",
        "src.pubmed_types.models.jats",
        "--structure-style",
        "namespace-clusters",
        "--relative-imports",
    )

    session.run(
        "xsdata",
        "downloads/schemas/180601/pubmed_230101.dtd",
        "--output",
        "pydantic",
        "--package",
        "src.pubmed_types.models.pubmed",
        "--structure-style",
        "namespace-clusters",
        "--relative-imports",
    )

    # Modify the math reference
    with open("src/pubmed_types/models/pubmed/disp_formula.py") as fr:
        lines = fr.readlines()

    for line_no, line in enumerate(lines):
        if "Optional[str]" in line:
            lines[line_no] = line.replace("Optional[str]", "Optional[Math]")

    lines.insert(3, "from ..jats.org.w3.pkg_1998.math.math_ml.math import Math\n")
    lines.insert(13, '			"namespace": "http://www.w3.org/1998/Math/MathML",\n')

    with open("src/pubmed_types/models/pubmed/disp_formula.py", "w") as fw:
        fw.writelines(lines)

    # Remove extraneous __init__ file
    Path("src/__init__.py").unlink()
