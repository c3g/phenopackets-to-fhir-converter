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
   "uri":"https://data.example/genomes/germline_wgs.vcf.gz",
   "description":"Matched normal germline sample",
   "htsFormat":"VCF",
   "genomeAssembly":"GRCh38",
   "individualToSampleIdentifiers":{
      "patient:1":"NA12345"
   }
}
