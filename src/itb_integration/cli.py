#!/usr/bin/env python
import os
import sys
import argparse
from pathlib import Path
from zipfile import ZipFile

from yaml import load as load_yaml, Loader
from tempfile import TemporaryDirectory


def req_as_test(requirement: dict, *, id: str, name: str):
    optional = "true" if requirement["level"] != "REQUIRED" else "false"

    interact_id = id.replace(":", '_') + '_interact'

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<testcase
  xmlns="http://www.gitb.com/tdl/v1/" xmlns:gitb="http://www.gitb.com/core/v1/"
  id="{id}"
  optional="{optional}"
>
  <metadata>
    <gitb:name>{requirement["title"]}</gitb:name>
    <gitb:version>1.0</gitb:version>
  </metadata>
  <actors>
    <gitb:actor id="Provider" role="SUT"/>
  </actors>
  <steps>
    <interact id="{interact_id}" inputTitle="{requirement["title"]}">
      <request
        name="fulfillment"
        inputType="SELECT_SINGLE"
        options="true,false"
        optionLabels="Fulfilled,Not Fulfilled"
        required="true"
        desc="Select your fulfillment status"
      />
    </interact>
    <verify handler="ExpressionValidator" desc="Validate test result">
      <input name="expression">${interact_id}{{fulfillment}} = "true"</input>
      <input name="successMessage">"Test fulfilled"</input>
      <input name="failureMessage">"Not fulfilled"</input>
    </verify>
  </steps>
</testcase>
"""


def make_suite(*, id, name, description, ids):
    test_cases = "\n".join(map(lambda id: f'<testcase id="{id}"/>', ids))

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<testsuite id="{id}" xmlns="http://www.gitb.com/tdl/v1/" xmlns:gitb="http://www.gitb.com/core/v1/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <metadata>
    <gitb:name>{name}</gitb:name>
    <gitb:description>{description}</gitb:description>
    <gitb:version>1.0</gitb:version>
  </metadata>

  <actors>
    <gitb:actor id="Provider">
      <gitb:name>Provider</gitb:name>
      <gitb:desc>The software provider under test</gitb:desc>
    </gitb:actor>
  </actors>

  {test_cases}
</testsuite>
"""


def zip_functionality(path, *, id=None, name=None, description=None, output=None):
    """takes the path to a functionality yaml and creates the corresponding test
    suite """
    with open(path) as yamlfile:
        data = load_yaml(yamlfile, Loader=Loader)

    with TemporaryDirectory(delete=False) as tmpdir:
        path = Path(tmpdir)

        ids = []

        # test cases
        for i, requirement in enumerate(data["requirements"]):
            index = i + 1
            case_id = f"{id}:{index:02d}"
            ids.append(case_id)
            test_case_data = req_as_test(
                requirement,
                id=case_id,
                name=case_id,
            )

            with open(path / (case_id + ".xml"), "w") as casefile:
                casefile.write(test_case_data)

        func_id = data["id"]

        # test suite file
        suite_data = make_suite(id=f"{id}:{func_id}", name=name, description=description, ids=ids)
        with open(path / "testSuite.xml", "w") as suitefile:
            suitefile.write(suite_data)

        os.makedirs(output, exist_ok=True)

        with ZipFile(output / f"{func_id}.zip", "w") as zipfile:
            zipfile.write(path / "testSuite.xml", arcname="testSuite.xml")
            zipfile.mkdir("testCases")

            for id in ids:
                zipfile.write(path / (id + ".xml"), arcname=f"testCases/{id}.xml")


def main(args):
    metadata_path = args.path / "metadata.yaml"
    print(f"reading {metadata_path}")

    with open(metadata_path) as metadatafile:
        metadata = load_yaml(metadatafile, Loader=Loader)

    functionalities = filter(
        lambda dir: dir.endswith(".yaml"),
        os.listdir(args.path / "functionalities")
    )

    for yaml in functionalities:
        zip_functionality(
            args.path / "functionalities" / yaml,
            id=metadata["urn"],
            name=metadata["name"],
            description=metadata["abstract"],
            output=args.output,
        )
        print(f"\tProcessed {yaml}")


def cli():
    parser = argparse.ArgumentParser(
        prog="itbload",
        description="Bundles test descriptions and uploads them to a target "
            "ITB instance."
    )

    parser.add_argument(
        "path", type=Path,
        help="Path to the folder containing the metadata.yaml of the building block",
    )
    parser.add_argument(
        "-o", "--output", type=Path, required=True,
        help="Path to a directory where all the archives will be put",
    )

    args = parser.parse_args()

    main(args)
