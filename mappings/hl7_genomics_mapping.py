# All fixed values provided by Phenopackets on FHIR Mapping guide
# Mappings from http://build.fhir.org/ig/HL7/genomics-reporting/index.html

HL7_GENOMICS_MAPPING = {
    "gene": {
        "url": "http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/region-studied",
        "geneStudied_Code": {
            "system": "https://loinc.org",
            "id": "48018-6",
            "label": "Gene studied [ID]"
        },
        "geneStudiedValue": {
            "system": "https://www.genenames.org/"
        }
    },
    "variant": {
        "url": "http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/variant",
        "variantLengthCode": {
            "system": "https://loinc.org",
            "id": "81300-6",
            "label": "Structural variant [Length]"
        }
    }
}