# New machine readable document structure

## Folder structure

```
<bb>/
    index.md
    description.md
    data_structures.md
    internal_workflows.md
    terminology.yml
    cfr.md
    other.md
    functionalities/
        <index.md>?
        01. <Functionality title 1>.md
        02. <Functionality title 2>.md
        ...
    tests/
```

### Definitions

* `bb` is a building block machine code, like `wallet`.
* `chapter` is a chapter identifier, like `kdf`.
* `2N. Functionality title` is a 0-padded number that gives order to functionalities within building blocks and a human-readable title for the functionality
* Index files (`index.md`) may be used to introduce each folder:
    + at the building block level
    + at the chapter level

### Index file structure

See [Parsing Specification Metadata](#parsing-specification-metadata) for machine-readibility details.


```
---
publication_identifier: # provided by GovStack GovSpecs Team (Ali, Kristo, etc). Example: govstack-bb-wallet
publication_name: # ex. Wallet Building Block Specification
publication_description: # Optional; is used to render cards for the publication and for SEO. 
version: # ex. 1.0.0
previous_version: # ex. 0.9.0 ; this is used to build version chains. 
status: # Example: [latest, release, development] This is a machine-processed value, not to be filled by people. 
working_group: # provided by GovSpecs team. Ex: "working_group/cfid"
publish_date: # example: 2025-09-01, this is a machine-processed value, not to be filled by people. Use ISO 8601.
cover: # url for the cover
authors:
    - identifier: # example: "person/firstname_lastname" use ASCII characters only
      name: # utf-8 allowed. Example: "Jane Doe"
      affiliation:
        name: Name of Entity
        url: "https://url.com"
contributors:
    - identifier: # example: "person/firstname_lastname" use ASCII characters only
      name: # utf-8 allowed. Example: "Jane Doe"
      affiliation:
        name: Name of Entity
        url: "https://url.com"
reviewers:
    - identifier: # example: "person/firstname_lastname" use ASCII characters only
      name: # utf-8 allowed. Example: "Jane Doe"
      affiliation:
        name: Name of Entity
        url: "https://url.com"
editors:
    - identifier: # example: "person/firstname_lastname" use ASCII characters only
      name: # utf-8 allowed. Example: "Jane Doe"
      affiliation:
        name: Name of Entity
        url: "https://url.com"
original_authors:
    - identifier: # example: "person/firstname_lastname" use ASCII characters only
      name: # utf-8 allowed. Example: "Jane Doe"
      affiliation: # These values are optional
        name: # Example: "Name of Entity" 
        url: "https://url.com" 
---
```


## Terminology file structure

```
terms:
    some-term: <link>
```

## Functionality file structure

```
---
title: Section title
requirements:
    - level: RECOMMENDED
      observability: AUDITABLE
      mutability: ...
      title: ...
      content: |
        ...
     tests:
       - src: ...
---
Free-style content, charts, pictures, bullets that do not embed
requirements in them.
```

## CFR file structure

```
---
title: Section title
requirements:
    - level: RECOMMENDED
      observability: AUDITABLE
      mutability: ...
      parent: <link to some cfr>
      title: ...
      content: |
        ...
    tests:
       - src: ...
---
Free-style content, charts, pictures, bullets that do not embed requirements in them.
```

## Implications

* Currently the requirements and free-style content are mixed. This is no longer possible.
* Heading level of each section is fixed: currently some requirements and sections differ in heading level (sometimes 3rd, sometimes 4th)
* Subsection is possible in the free-style content, but not grouping of requirements in subsections.

## Further work

* requirement-level ID needs to be defined.
* make sure that subsectioning of requirements is not necessary.

## Parsing Specification Metadata

The following vocabularies are used for the data model:

- BIBO (`bibo:`): Primary vocabulary to describe Specification metadata
- Dublin Core (`dcterms:`): Fallback vocabulary for properties that are not directly available on BIBO.
- FoaF: To denote entities and metadata about authors, working groups and affiliation information of authors (what organization they belong to).
- MARC Relators `marcrel:`: Are used to denote relation of authors or groups to the specification. 

We choose to use BIBO as the primary vocabulary to denote metadata related to specifications. BIBO was designed specifically for describing bibliographic resources such as documents, standards, and specifications on the Semantic Web, and provides precise types and properties for this use case. In fact, GovStack Building Blocks are a type of the [bibo:specification](https://dcmi.github.io/bibo/#:Specification) class. 

BIBO is maintained by the Dublin Core Metadata Initiative, which is in itself widely adopted; and since each bibo property is formally declared as a subproperty of its Dublin Core equivalent, it maps cleanly to Dublin Core vocabulary, so processors can map metadata correctly through RDF inference without any data loss. 

Usage of FoaF and MARC relators is best described by section [Denoting Attribution](#denoting-attribution) below.

You can map GovStack's vocabulary through the following equivalency table:

| GovStack Vocab | DCAT Vocab |
| --- | --- |
| publication_identifier | [bibo:identifier](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/terms/identifier/) | 
| publication_name | [bibo:title](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/terms/title/) |
| publication_description | [bibo:abstract](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/terms/abstract/) |
| cover | [foaf:depiction](https://xmlns.com/foaf/spec/#term_depiction) |
| version | [bibo:edition](https://dcmi.github.io/bibo/#:edition). We are using bibo vocabulary because Dublin Core does not have a native `version` property. Furthermore, bibo has a [Specification](https://dcmi.github.io/bibo/#:Specification) class, so it is more appropriate for this metadatum. | 
| previous_version | [bibo:replaces](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#replaces) While we are not using DCAT, it has a good example on [version chains and hierarchies](https://www.w3.org/TR/vocab-dcat-3/#version-relationships). |
| status | [bibo:status](https://dcmi.github.io/bibo/#:status) |
| working_group | [dcterms:creator](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_creator) [foaf:Group](https://xmlns.com/foaf/spec/#term_Group) |
| author, contributor, reviewer, editor, original_author | [dcterms:creator](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_creator) as a property relation and [foaf:Person](https://xmlns.com/foaf/spec/#term_Person) as the content. See the  [Denoting Attribution](#denoting-attribution). |


## Denoting attribution


The different roles of `author`, `contributor`, `reviewer`, `editor` and `original_author` all use FoaF vocabulary to store the attributes. The current data model is minimalistic and self-contained, so that it works without requiring a backend implementation (i.e. a database or an API to store authors). However, the `identifier` property allows it to be expandable so that a backend implementation is possible and we can support the use case of storing author relations to their publications or to update their attributes (example, when a person switches jobs, you can update the relation on all linked documents.)

This implementation allows the `identifier` attribute to future-proof the entry for when a database of authors is available. In the initial stage, the data for each author can be added manually (name, affiliation) with identifier value `dcterms:identifier` following the pattern `person/firstname_lastname` using ASCII lowercase characters only. Once the backend is available, the existing data can be used to create the entries. 

Verbose example:

```
    - "@type": "foaf:Person"
      "dcterms:identifier": "person/alice_smith"
      "foaf:name": "Alice Smith"
      "org:memberOf": 
        "@type": "foaf:Organization"
        "foaf:name": "GovStack"
        "foaf:homepage":
            "@id": "https://govstack.global/"
    - "@type": "foaf:Person"
      "dcterms:identifier": "person/alice_smith"
      "foaf:name": "Bob Jones"
      "org:memberOf": 
        "@type": "foaf:Organization"
        "foaf:name": "GovStack"
        "foaf:homepage":
            "@id": "https://govstack.global/"
```

When a backend is available, only the identifier is required to insert:

```
marcrel:aut:
  - "@type": "foaf:Person"
    "dcterms:identifier": "person/alice_smith"
```

To denote the different roles we will use MARC relators which are subproperties of `dcterms:contributor` within Library of Congress vocabulary, hence allowing backwards compatibility to Dublin Core. Here are the MARC relators:

| GovStack Vocab | MARC relator | URI |
| --- | --- | --- |
| authors | `marcrel:aut` | http://id.loc.gov/vocabulary/relators/aut |
| editors | `marcrel:edt` | http://id.loc.gov/vocabulary/relators/edt | 
| reviewers | `marcrel:rev` | http://id.loc.gov/vocabulary/relators/rev | 
| contributors | `marcrel:ctb` | http://id.loc.gov/vocabulary/relators/ctb | 
| original_authors | `marcrel:originator` | http://id.loc.gov/vocabulary/relators/org |
