# All fixed values provided by Phenopackets on FHIR Mapping guide

PHENOPACKETS_ON_FHIR_MAPPING = {
    "individual": {
        "title": "Individual",
        "url": "http://ga4gh.org/fhir/phenopackets/StructureDefinition/Individual",
        "age": "http://ga4gh.org/fhir/phenopackets/StructureDefinition/individual-age",
        "karyotypicSex": {
            "url": "http://ga4gh.org/fhir/phenopackets/StructureDefinition/individual-karyotypic-sex",
            "system": "http://ga4gh.org/fhir/phenopackets/CodeSystem/karyotypic-sex"
        },
        "taxonomy": "http://ga4gh.org/fhir/phenopackets/StructureDefinition/individual-taxonomy"
    },
    "phenopacket": {
        "title": "Phenopacket",
        "code": {
            "system": "http://ga4gh.org/fhir/phenopackets/CodeSystem/document-type",
            "code": "phenopacket"
        },
        "url": "http://ga4gh.org/fhir/phenopackets/StructureDefinition/Phenopacket",
        "phenotypic_features": {
            "title": "Phenotypic Features",
            "code": {
                "system": "http://ga4gh.org/fhir/phenopackets/CodeSystem/section-type",
                "version": "0.1.0",
                "code": "phenotypic-features",
                "display": "Phenotypic Features"
            }
        },
        "biosamples": {
                "title": "Biosamples",
                "code": {
                    "system": "http://ga4gh.org/fhir/phenopackets/CodeSystem/section-type",
                    "version": "0.1.0",
                    "code": "biosamples",
                    "display": "Biosamples"
                }
            },
        "variants": {
            "title": "Variants",
            "code": {
                "system": "http://ga4gh.org/fhir/phenopackets/CodeSystem/section-type",
                "version": "0.1.0",
                "code": "variants",
                "display": "Variants"
            }
        },
        "diseases": {
            "title": "Diseases",
            "code": {
                "system": "http://ga4gh.org/fhir/phenopackets/CodeSystem/section-type",
                "version": "0.1.0",
                "code": "diseases",
                "display": "Diseases"
            }
        },
        "hts_files": {
            "title": "HTS Files",
            "code": {
                "system": "http://ga4gh.org/fhir/phenopackets/CodeSystem/section-type",
                "version": "0.1.0",
                "code": "hts-files",
                "display": "HTS Files"
            }
        }
    },
    "biosample": {
        "title": "Biosample",
        "url": "http://ga4gh.org/fhir/phenopackets/StructureDefinition/Biosample",
        "individualAgeAtCollection": "http://ga4gh.org/fhir/phenopackets/StructureDefinition/biosample-individual-age-at-collection",
        "histologicalDiagnosis": "http://ga4gh.org/fhir/phenopackets/StructureDefinition/biosample-histological-diagnosis",
        "tumorProgression": "http://ga4gh.org/fhir/phenopackets/StructureDefinition/biosample-tumor-progression",
        "tumorGrade": "http://ga4gh.org/fhir/phenopackets/StructureDefinition/biosample-tumor-grade",
        "diagnosticMarkers": "http://ga4gh.org/fhir/phenopackets/StructureDefinition/biosample-diagnostic-markers",
        "isControlSample": "http://ga4gh.org/fhir/phenopackets/StructureDefinition/biosample-control"
    },
    "phenotypicFeature": {
        "title": "Phenotypic Feature",
        "url": "http://ga4gh.org/fhir/phenopackets/StructureDefinition/PhenotypicFeature",
        "severity": "http://ga4gh.org/fhir/phenopackets/StructureDefinition/phenotypic-feature-severity",
        "modifier": "http://ga4gh.org/fhir/phenopackets/StructureDefinition/phenotypic-feature-modifier",
        "onset": "http://ga4gh.org/fhir/phenopackets/StructureDefinition/phenotypic-feature-onset",
        "evidence": {
            "url": "http://ga4gh.org/fhir/phenopackets/StructureDefinition/evidence",
            # fixed value
            "evidenceCode": "evidenceCode"
        }
    },
    "externalReference": {
        "url": "http://ga4gh.org/fhir/phenopackets/StructureDefinition/external-reference",
        # fixed values
        "idUrl": "id",
        "descriptionUrl": "description"
    },
    "htsFile": {
        "url": "http://ga4gh.org/fhir/phenopackets/StructureDefinition/HtsFile",
        "genomeAssembly": "http://ga4gh.org/fhir/phenopackets/StructureDefinition/htsfile-genome-assembly",
        # fixed value
        "status": "current",
        "htsFormat": "http://ga4gh.org/fhir/phenopackets/CodeSystem/hts-format"
    },
    "disease": {
        "url": "http://ga4gh.org/fhir/phenopackets/StructureDefinition/Disease",
        "onset": "http://ga4gh.org/fhir/phenopackets/StructureDefinition/disease-onset",
        "disease_stage": "http://ga4gh.org/fhir/phenopackets/StructureDefinition/disease-tumor-stage",
    }
}