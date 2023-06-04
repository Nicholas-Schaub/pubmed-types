from pathlib import Path

import nox


@nox.session
def generate_packages(session):
    session.install("requests", "xsdata-pydantic[cli,lxml,soap]")

    # Get the article schema
    import zipfile
    import requests

    base_path = Path("downloads")
    base_path.mkdir(exist_ok=True)

    URL = "https://ftp.ncbi.nih.gov/pub/jats/archiving/1.3/xsd/"
    package_name = "JATS-Archiving-1-3-MathML3-XSD.zip"
    with open(base_path.joinpath(package_name), "wb") as fw:
        fw.write(requests.get(URL + package_name).content)

    with zipfile.ZipFile(base_path.joinpath(package_name), "r") as zip_ref:
        zip_ref.extractall(base_path)

    with open(
        base_path.joinpath("JATS-Archiving-1-3-MathML3-XSD").joinpath("ali.xsd"), "w"
    ) as fw:
        fw.write(
            requests.get(
                "https://www.niso.org/schemas/ali/1.0/ali.xsd", verify=False
            ).text
        )

    session.run(
        "xsdata",
        "downloads/JATS-Archiving-1-3-MathML3-XSD/",
        "--output",
        "pydantic",
        "--package",
        "src.pubmed_types.models",
        "--recursive",
        "--relative-imports",
        "--structure-style",
        "namespace-clusters",
    )

    # Remove extraneous __init__ file
    Path("src/__init__.py").unlink()
