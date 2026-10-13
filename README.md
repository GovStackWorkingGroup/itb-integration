# Scripts for integration into ITB

## Convert a building block into test-suites

The following script will ingest a directory with the contents of a building
block (requires at least a `metadata.yaml` file and a `functionalities`
directory) and will output one zip file per functionality with the test cases
corresponding to the requirements.

```shell
$ uv run itbload <bb-src-dir> -o build/
```

## Upload the generated test suites to an ITB instance

Set the following environment variables:

* `ITB_ORG_KEY` A community that has the domain assigned
* `ITB_GROUP_KEY` The spectification group where specifications will be uploaded
* `ITB_DOMAIN_KEY` The API key for the domain

Then run `itbupload`:

```shell
uv run itbupload --url "http://localhost:9000/api/rest" build/
```
