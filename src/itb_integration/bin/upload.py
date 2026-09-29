import os
import sys
import argparse
from pathlib import Path

import requests


def main(args):
    archives = filter(lambda x: x.endswith(".zip"), os.listdir(args.path))

    group_key = os.getenv("ITB_GROUP_KEY")
    org_key = os.getenv("ITB_ORG_KEY")
    domain_key = os.getenv("ITB_DOMAIN_KEY")

    if not group_key or not org_key or not domain_key:
        print("Please set all of ITB_ORG_KEY, ITB_GROUP_KEY and ITB_DOMAIN_KEY env vars")
        sys.exit(1)

    res = requests.get(f"{args.url}/group/{group_key}/specifications", headers={
        "ITB-API-KEY": org_key,
    })

    specs = dict()

    for spec in res.json():
        specs[spec["shortName"]] = spec["apiKey"]

    for archive in archives:
        archive_short = archive.split(".")[0]

        if archive_short in specs:
            # This archive was already created in ITB, replace it
            spec_key = specs[archive_short]
        else:
            # Create the specification in ITB
            res = requests.put(f"{args.url}/specification", headers={
                "ITB-API-KEY": org_key,
            }, json={
                "shortName": archive_short,
                "fullName": archive_short,
                "group": group_key,
                "domain": domain_key,
            })
            spec_key = res.json()["apiKey"]
            res.raise_for_status()
        # Then upload the file
        res = requests.post(f"{args.url}/testsuite/deploy", headers={
            "ITB-API-KEY": org_key,
        }, data={
            "specification": spec_key,
            "updateSpecification": True,
        }, files={
            "testSuite": open(args.path / archive, "rb"),
        })
        print(res.text)
        res.raise_for_status()


def cli():
    parser = argparse.ArgumentParser(
        prog="itbupload",
        description="Uploads test cases into a ITB instance."
    )

    parser.add_argument(
        "path", type=Path,
        help="Path to the folder containing the archives to upload",
    )
    parser.add_argument(
        "-u", "--url", required=True,
        help="The url of the root API endpoint",
    )

    args = parser.parse_args()

    main(args)
