INDIVIDUAL = {
    "id": "ind:HG00096",
    "taxonomy": {
        "id": "NCBITaxon:9606",
        "label": "Homo sapiens"
    },
    "age": {
        "age": "P70Y"
    },
    "dateOfBirth": "1949-02-20",
    "sex": "MALE",
    "karyotypicSex": "XY",
    "created": "2019-12-20T21:50:28.583082Z",
    "updated": "2019-12-17T20:46:36.228304Z"
}

PHENOTYPIC_FEATURE = {
    "type": {
        "id": "HP:0000520",
        "label": "Proptosis"
    },
    "severity": {
        "id": "HP: 0012825",
        "label": "Mild"
    },
    "onset": {
        "id": "HP:0003577",
        "label": "Congenital onset"
    },
    "evidence": {
        "reference": {
            "id": "test",
            "description": "test"
        },
        "evidenceCode": {
            "id": "12323",
            "label": "Evidence code 12"
        }
    },
    "description": "Human-readable verbiage NOT for structured text",
    "negated": True,
    "modifier": [
        {
            "id": "HP: 0012825 ",
            "label": "Mild"
        },
        {
            "id": "HP: 0012823 ",
            "label": "Semi-mild"
        }
    ]
}

BIOSAMPLE = {
    "id": "biosample:test01",
    "sampledTissue": {
        "id": "UBERON_0004228",
        "label": "urinary bladder smooth muscle"
    },
    "individualAgeAtCollection": {
        "age": "P47Y"
    },
    "histological_diagnosis": {
        "id": "NCIT:C39853",
        "label": "Infiltrating Urothelial Carcinoma"
    },
    "tumorProgression": {
        "id": "NCIT:C84509",
        "label": "Primary Malignant Neoplasm"
    },
    "tumorGrade": {
        "id": "NCIT:C28076",
        "label": "Disease Grade Qualifier"
    },
    "diagnosticMarkers": [
        {
            "id": "NCIT:C68748",
            "label": "HER2/Neu Positive"
        },
        {
            "id": "NCIT:C131711",
            "label": "Human Papillomavirus-18 Positive"
        }
    ],
    "procedure": {
        "code": {
            "id": "NCIT:C5189",
            "label": "Radical Cystoprostatectomy"
        },
        "bodySite": {
            "id": "UBERON_0001556",
            "label": "lower urinary tract"
        }
    }
}

HTS_FILE = {
    "uri": "https://data.example/genomes/germline_wgs.vcf.gz",
    "description": "Matched normal germline sample",
    "htsFormat": "VCF",
    "genomeAssembly": "GRCh38",
    "individualToSampleIdentifiers": {
        "patient:1": "NA12345"
    }
}

GENE = {
    "id": "HGNC:2621",
    "symbol": "CYP2C19"
}

VARIANT = {
    "alleleType": "spdiAllele",
    "allele": {
        "id": "clinvar:13294",
        "seqId": "NC_000010.10",
        "position": 123256214,
        "deletedSequence": "T",
        "insertedSequence": "G"
    },
    "zygosity": {
        "id": "NCBITaxon:9606",
        "label": "human"
    }
}

DISEASE = {
    "term": {
        "id": "OMIM:164400",
        "label": "Spinocerebellar ataxia 1"
    },
    "onset": {
        "age": "P25Y3M2D"
    },
    "diseaseStage": [
        {
            "id": "NCIT:C28091",
            "label": "Gleason Score 7"
        }
    ],
    "extraProperties": {
        "comment": "test data"
    }
}

PHENOPACKET = {
    "id": "29f24cd0-0c4f-48b2-889c-dff43d2b132d",
    "subject": {
        "id": "ind:NA19648",
        "taxonomy": {
            "id": "NCBITaxon:9606",
            "label": "Homo sapiens"
        },
        "dateOfBirth": "1991-09-29",
        "sex": "FEMALE",
        "karyotypicSex": "XX"
    },
    "metaData": {
        "resources": [
            {
                "id": "ncbi_taxonomy",
                "name": "NCBI Taxonomy OBO Edition",
                "namespacePrefix": "NCBITaxon",
                "url": "http://purl.obolibrary.org/obo/ncbitaxon.owl",
                "version": "2018-07-27",
                "iriPrefix": "http://purl.obolibrary.org/obo/NCBITaxon_"
            },
            {
                "id": "uberon",
                "name": "Uber-anatomy ontology",
                "namespacePrefix": "UBERON",
                "url": "http://purl.obolibrary.org/obo/uberon.owl",
                "version": "2019-06-27",
                "iriPrefix": "http://purl.obolibrary.org/obo/UBERON"
            },
            {
                "id": "nci_thesaurus",
                "name": "NCI Thesaurus",
                "namespacePrefix": "NCIT",
                "url": "https://ncit.nci.nih.gov",
                "version": "2015-09-01",
                "iriPrefix": "https://ncit.nci.nih.gov"
            }
        ],
        "created": "2020-02-13T16:30:21.724329Z",
        "createdBy": "David Lougheed",
        "submittedBy": "Ksenia Zaytseva",
        "phenopacketSchemaVersion": "1.0.0-RC3",
        "updated": "2020-02-13T16:30:21.724329Z"
    },
    "biosamples": [
        {
            "id": "NA19648",
            "sampledTissue": {
                "id": "UBERON_0000178",
                "label": "blood"
            },
            "individualAgeAtCollection": {
                "age": "P28Y"
            },
            "phenotypicFeatures": [
                {
                    "type": {
                        "id": "HP:0012219",
                        "label": "Erythema nodosum"
                    },
                    "severity": {
                        "id": "HP: 0012825",
                        "label": "Mild"
                    },
                    "onset": {
                        "id": "HP:0003577",
                        "label": "Congenital onset"
                    },
                    "evidence": {
                        "reference": {
                            "id": "PMID:30962759",
                            "description": "Recurrent Erythema Nodosum in a Child with a SHOC2 Gene Mutation"
                        },
                        "evidenceCode": {
                            "id": "ECO:0006017",
                            "label": "author statement from published clinical study used in manual assertion"
                        }
                    },
                    "negated": True,
                    "modifier": [
                        {
                            "id": "HP: 0012825 ",
                            "label": "Mild"
                        },
                        {
                            "id": "HP: 0012823 ",
                            "label": "Semi-mild"
                        }
                    ]
                }
            ],
            "procedure": {
                "code": {
                    "id": "NCIT_C15189",
                    "label": "Biopsy"
                }
            },
            "description": "Biosample for patient NA19648"
        }
    ],
    "genes": [
        {
            "id": "HGNC:2621",
            "symbol": "CYP2C19"
        }
    ],
    "diseases": [
        {
            "term": {
                "id": "NCIT:C4872",
                "label": "Breast Carcinoma"
            },
            "onset": {
                "age": "P28Y"
            }
        }
    ],
    "variants": [

    ],
    "htsFiles": [

    ]
}
