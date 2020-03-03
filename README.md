# phenopackets-to-fhir converter

## Introduction

**phenopackets-to-fhir** is a service to convert derived phenopackets objects to FHIR resources.
The service is a part of the ongoing work for [CHORD Metadata service](https://github.com/c3g/chord_metadata_service).
The phenopackets schemas are project-specific adaptations of [Phenopackets schema standard](https://phenopackets-schema.readthedocs.io/en/latest/).

The package contains:

- json schemas for Phenopacket and its elements derived/based on [Phenopackets schema standard](https://phenopackets-schema.readthedocs.io/en/latest/).

- functions to transform phenopackets objects to [FHIR](https://www.hl7.org/fhir/) resources.

- mappings derived from [Phenopackets on FHIR Implementation Guide](https://aehrc.github.io/fhir-phenopackets-ig/).

The conversion uses [Python SMART on FHIR client](https://github.com/smart-on-fhir/client-py) that provides validation of generated FHIR resources.