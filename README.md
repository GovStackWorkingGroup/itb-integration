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
