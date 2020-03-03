Introduction
============

**phenopackets-to-fhir** is a service to convert derived phenopackets objects to FHIR resources.
The service is a part of the ongoing work for `CHORD Metadata service <https://github.com/c3g/chord_metadata_service>`_.
The phenopackets schemas are project-specific adaptations of `Phenopackets schema standard <https://phenopackets-schema.readthedocs.io/en/latest/>`_.

The package contains:

- json schemas for Phenopacket and its elements derived/based on `Phenopackets schema standard <https://phenopackets-schema.readthedocs.io/en/latest/>`_.

- functions to transform phenopackets objects to `FHIR <https://www.hl7.org/fhir/>`_ resources.

- mappings derived from `Phenopackets on FHIR Implementation Guide <https://aehrc.github.io/fhir-phenopackets-ig/>`_.

The conversion uses `Python SMART on FHIR client <https://github.com/smart-on-fhir/client-py>`_ that provides validation of generated FHIR resources.