# Scripts for integration into ITB

## Convert a building block into test-suites

The following script will ingest a directory with the contents of a building
block (requires at least a `metadata.yaml` file and a `functionalities`
directory) and will output one zip file per functionality with the test cases
corresponding to the requirements.

```shell
$ uv run itbload <bb-src-dir> -o build/
```
