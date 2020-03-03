from datetime import datetime
from mappings.phenopackets_on_fhir_mapping import PHENOPACKETS_ON_FHIR_MAPPING
from mappings.hl7_genomics_mapping import HL7_GENOMICS_MAPPING
from fhirclient.models import (observation as obs, patient as p, extension, age, coding as c,
                               codeableconcept, specimen as s, identifier as fhir_indentifier,
                               annotation as a, range, quantity, fhirreference,
                               documentreference, attachment, fhirdate, condition as cond,
                               composition as comp
                               )
from .validate import validate_schema, SCHEMA_PATH
import os
import jsonschema
import uuid

##################### Generic FHIR conversion functions #####################


def fhir_coding_util(obj):
    """Genenric function to convert object to FHIR Coding.
    """

    coding = c.Coding()
    coding.display = obj['label']
    coding.code = obj['id']
    if 'system' in obj:
        coding.system = obj['system']
    return coding


def fhir_codeable_concept(obj):
    """Generic function to convert object to FHIR CodeableConcept.
    """

    codeable_concept = codeableconcept.CodeableConcept()
    codeable_concept.coding = []
    if isinstance(obj, list):
        for item in obj:
            coding = fhir_coding_util(item)
            codeable_concept.coding.append(coding)
    else:
        coding = fhir_coding_util(obj)
        codeable_concept.coding.append(coding)
    return codeable_concept


def codeable_concepts_fields(field_list, profile, obj):
    """Converts a list of fields to FHIR CodeableConcepts and returns a list of extensions.

    :param field_list: fields to convert to codeable concepts
    :param profile: name of an object in phenopackets mappings
    :param obj: object to which fields belong to
    :return: list of extensions
    """

    concept_extensions = []
    for field in field_list:
        if field in obj:
            codeable_concepts_extension = extension.Extension()
            codeable_concepts_extension.url = PHENOPACKETS_ON_FHIR_MAPPING[profile][field]
            codeable_concepts_extension.valueCodeableConcept = fhir_codeable_concept(obj[field])
            concept_extensions.append(codeable_concepts_extension)
    return concept_extensions


def age_to_fhir(obj, mapping, field):
    """Generic function to convert Phenopackets Age or AgeRange to FHIR Age.

    :param obj: object to which field Age or AgeRange belongs to
    :param mapping: mapping from PHENOPACKETS_ON_FHIR
    :param field: name of the field that stores age
    :return: age extension object
    """

    age_extension = extension.Extension()
    age_extension.url = mapping
    if isinstance(obj[field]['age'], dict):
        age_extension.valueRange = range.Range()
        age_extension.valueRange.low = quantity.Quantity()
        age_extension.valueRange.low.unit = obj[field]['age']['start']['age']
        age_extension.valueRange.high = quantity.Quantity()
        age_extension.valueRange.high.unit = obj[field]['age']['end']['age']
    else:
        age_extension.valueAge = age.Age()
        age_extension.valueAge.unit = obj[field]['age']
    return age_extension


def check_disease_onset(disease):
    """Phenopackets schema allows age to be represented by ISO8601 string,
    whereis Pheno-FHIR guide requires it to be represented by CodeableConcept.
    This function checks how age is represented in data.

    :param disease: disease json object
    :return: True/False
    """
    if disease.get('onset'):
        if isinstance(disease.get('onset').get('age'), dict):
            if disease.get('onset').get('age').get('label') is not None:
                return True
    return False


##################### Class-based FHIR conversion functions #####################


def individual_to_fhir(obj):
    """Converts Individual to FHIR Patient.

    :param obj: Individual json
    :return: FHIR Patient json
    """

    # first validate if phenopackets object is well-formed
    schema_path = os.path.join(SCHEMA_PATH, 'individual_schema.json')
    try:
        validate_schema(schema_path, obj)
    except jsonschema.exceptions.ValidationError:
        raise Exception("The individual object is not valid.")

    patient = p.Patient()
    patient.id = obj['id']
    patient.birthDate = fhirdate.FHIRDate(obj.get('dateOfBirth', None))
    patient.gender = obj.get('sex', None)
    patient.active = obj.get('active', None)
    patient.deceasedBoolean = obj.get('deceased', None)
    patient.extension = list()
    # age
    if 'age' in obj:
        age_extension = age_to_fhir(obj, PHENOPACKETS_ON_FHIR_MAPPING['individual']['age'], 'age')
        patient.extension.append(age_extension)
    # karyotypic_sex
    if 'karyotypicSex' in obj:
        karyotypic_sex_extension = extension.Extension()
        karyotypic_sex_extension.url = PHENOPACKETS_ON_FHIR_MAPPING['individual']['karyotypicSex']['url']
        karyotypic_sex_extension.valueCodeableConcept = codeableconcept.CodeableConcept()
        karyotypic_sex_extension.valueCodeableConcept.coding = list()
        coding = c.Coding()
        coding.display = obj.get('karyotypicSex', None)
        coding.code = obj.get('karyotypicSex', None)
        coding.system = PHENOPACKETS_ON_FHIR_MAPPING['individual']['karyotypicSex']['system']
        karyotypic_sex_extension.valueCodeableConcept.coding.append(coding)
        patient.extension.append(karyotypic_sex_extension)
    # taxonomy
    if 'taxonomy' in obj:
        taxonomy_extension = extension.Extension()
        taxonomy_extension.url = PHENOPACKETS_ON_FHIR_MAPPING['individual']['taxonomy']
        taxonomy_extension.valueCodeableConcept = codeableconcept.CodeableConcept()
        taxonomy_extension.valueCodeableConcept.coding = list()
        coding = c.Coding()
        coding.display = obj.get('taxonomy', None).get('label', None)
        coding.code = obj.get('taxonomy', None).get('id', None)
        taxonomy_extension.valueCodeableConcept.coding.append(coding)
        patient.extension.append(taxonomy_extension)
    return patient.as_json()


#TODO remove ?
def procedure_to_fhir(obj):
    """Converts Procedure to FHIR Specimen collection.
    """

    collection = s.SpecimenCollection()
    collection.id = str(obj['id'])
    collection.method = fhir_codeable_concept(obj['code'])
    if 'bodySite' in obj:
        collection.bodySite = fhir_codeable_concept(obj['bodySite'])
    return collection.as_json()


def phenotypic_feature_to_fhir(obj):
    """Converts Phenotypic feature to FHIR Observation.

    :param obj: PhenotypicFeature json
    :return: FHIR Observation json
    """

    schema_path = os.path.join(SCHEMA_PATH, 'phenotypic_feature_schema.json')
    try:
        validate_schema(schema_path, obj)
    except jsonschema.exceptions.ValidationError:
        raise Exception("The phenotypic feature object is not valid.")

    observation = obs.Observation()
    if 'description' in obj:
        observation.note = []
        annotation = a.Annotation()
        annotation.text = obj.get('description', None)
        observation.note.append(annotation)
    observation.code = fhir_codeable_concept(obj['type'])
    # required by FHIR specs but omitted by phenopackets, for now set for unknown
    observation.status = 'unknown'
    if 'negated' in obj:
        observation.interpretation = fhir_codeable_concept(
            {"label": "Positive", "id": "POS"}
        )
    else:
        observation.interpretation = fhir_codeable_concept(
            {"label": "Negative", "id": "NEG"}
        )
    observation.extension = []
    concept_extensions = codeable_concepts_fields(
        ['severity', 'modifier', 'onset'], 'phenotypicFeature', obj
    )
    for c in concept_extensions:
        observation.extension.append(c)
    if 'evidence' in obj:
        evidence = extension.Extension()
        evidence.url = PHENOPACKETS_ON_FHIR_MAPPING['phenotypicFeature']['evidence']['url']
        evidence.extension = []
        evidence_code = extension.Extension()
        evidence_code.url = PHENOPACKETS_ON_FHIR_MAPPING['phenotypicFeature']['evidence']['evidenceCode']
        evidence_code.valueCodeableConcept = fhir_codeable_concept(obj['evidence']['evidenceCode'])
        evidence.extension.append(evidence_code)
        if 'reference' in obj['evidence']:
            evidence_reference = extension.Extension()
            evidence_reference.url = PHENOPACKETS_ON_FHIR_MAPPING['externalReference']['url']
            evidence_reference.extension = []
            evidence_reference_id = extension.Extension()
            evidence_reference_id.url = PHENOPACKETS_ON_FHIR_MAPPING['externalReference']['idUrl']
            evidence_reference_id.valueUri = obj['evidence']['reference']['id']
            evidence_reference.extension.append(evidence_reference_id)
            if 'description' in obj['evidence']['reference']:
                evidence_reference_desc = extension.Extension()
                evidence_reference_desc.url = PHENOPACKETS_ON_FHIR_MAPPING['externalReference']['descriptionUrl']
                evidence_reference_desc.valueString = obj['evidence']['reference'].get('description', None)
                evidence_reference.extension.append(evidence_reference_desc)
            evidence.extension.append(evidence_reference)
        observation.extension.append(evidence)

    if 'biosample' in obj:
        observation.specimen = fhirreference.FHIRReference()
        observation.specimen.reference = obj.get('biosample', None)
    return observation.as_json()


def biosample_to_fhir(obj):
    """Converts Biosample to FHIR Specimen.

    :param obj: Biosample json
    :return: FHIR Specimen json
    """

    schema_path = os.path.join(SCHEMA_PATH, 'biosample_schema.json')
    try:
        validate_schema(schema_path, obj)
    except jsonschema.exceptions.ValidationError:
        raise Exception("The biosample object is not valid.")
    specimen = s.Specimen()
    specimen.identifier = []
    # id
    identifier = fhir_indentifier.Identifier()
    identifier.value = obj['id']
    specimen.identifier.append(identifier)
    # individual - subject property in FHIR is mandatory for a specimen
    specimen.subject = fhirreference.FHIRReference()
    specimen.subject.reference = obj.get('individual', 'unknown')
    # sampled_tissue
    specimen.type = codeableconcept.CodeableConcept()
    specimen.type.coding = []
    coding = c.Coding()
    coding.code = obj['sampledTissue']['id']
    coding.display = obj['sampledTissue']['label']
    specimen.type.coding.append(coding)
    # description
    if 'description' in obj:
        specimen.note = []
        annotation = a.Annotation()
        annotation.text = obj.get('description', None)
        specimen.note.append(annotation)
    # procedure
    specimen.collection = s.SpecimenCollection()
    specimen.collection.method = fhir_codeable_concept(obj['procedure']['code'])
    if 'bodySite' in obj['procedure']:
        specimen.collection.bodySite = fhir_codeable_concept(obj['procedure']['bodySite'])
    # Note on taxonomy from phenopackets specs:
    # Individuals already contain a taxonomy attribute so this attribute is not needed.
    # extensions
    specimen.extension = []
    # individual_age_at_collection
    if 'individualAgeAtCollection' in obj:
        ind_age_at_collection_extension = age_to_fhir(
            obj, PHENOPACKETS_ON_FHIR_MAPPING['biosample']['individualAgeAtCollection'],
            'individualAgeAtCollection'
        )
        specimen.extension.append(ind_age_at_collection_extension)
    concept_extensions = codeable_concepts_fields(
        ['histologicalDiagnosis', 'tumorProgression', 'tumorGrade', 'diagnosticMarkers'],
        'biosample', obj
    )
    for concept in concept_extensions:
        specimen.extension.append(concept)

    if 'isControlSample' in obj:
        control_extension = extension.Extension()
        control_extension.url = PHENOPACKETS_ON_FHIR_MAPPING['biosample']['isControlSample']
        control_extension.valueBoolean = obj['isControlSample']
        specimen.extension.append(control_extension)
    # TODO 2m extensions - references
    return specimen.as_json()


def hts_file_to_fhir(obj):
    """Converts HTS file to FHIR DocumentReference.

    :param obj: HTS file json
    :return: FHIR DocumentReference json
    """

    schema_path = os.path.join(SCHEMA_PATH, 'hts_file_schema.json')
    try:
        validate_schema(schema_path, obj)
    except jsonschema.exceptions.ValidationError:
        raise Exception("The hts file object is not valid.")
    doc_ref = documentreference.DocumentReference()
    doc_ref.type = fhir_codeable_concept({"label": obj['htsFormat'], "id": obj['htsFormat']})
    # GA4GH requires status with the fixed value
    doc_ref.status = PHENOPACKETS_ON_FHIR_MAPPING['htsFile']['status']
    doc_ref.content = []
    doc_content = documentreference.DocumentReferenceContent()
    doc_content.attachment = attachment.Attachment()
    doc_content.attachment.url = obj['uri']
    if 'description' in obj:
        doc_content.attachment.title = obj['description']
    doc_ref.content.append(doc_content)
    doc_ref.indexed = fhirdate.FHIRDate()
    doc_ref.indexed.date = datetime.now()
    doc_ref.extension = []
    genome_assembly = extension.Extension()
    genome_assembly.url = PHENOPACKETS_ON_FHIR_MAPPING['htsFile']['genomeAssembly']
    genome_assembly.valueString = obj['genomeAssembly']
    doc_ref.extension.append(genome_assembly)
    return doc_ref.as_json()


def gene_to_fhir(obj):
    """Convert Gene to Observation.component:gene property.
    GA4GH Phenopackets Implementation Guide provides a link to Genomics Reporting Implementation Guide (STU1) mapping
    http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/region-studied .

    :param obj: gene json
    :return: Observation.component:gene json
    """

    schema_path = os.path.join(SCHEMA_PATH, 'gene_schema.json')
    try:
        validate_schema(schema_path, obj)
    except jsonschema.exceptions.ValidationError:
        raise Exception("The gene object is not valid.")
    component = obs.ObservationComponent()
    component.code = fhir_codeable_concept(HL7_GENOMICS_MAPPING['gene']['geneStudied_Code'])
    component.valueCodeableConcept = fhir_codeable_concept({
        "id": obj['id'],
        "label": obj['symbol'],
        "system": HL7_GENOMICS_MAPPING['gene']['geneStudiedValue']['system']
    })
    return component.as_json()


def variant_to_fhir(obj):
    """Variant corresponds to Observation.component:variant.
    GA4GH Phenopackets Implementation Guide provides a link to Genomics Reporting Implementation Guide (STU1) mapping
    http://hl7.org/fhir/uv/genomics-reporting/STU1/variant.html.

    :param obj: Variant json
    :return: Observation.component:variant json
    """

    schema_path = os.path.join(SCHEMA_PATH, 'variant_schema.json')
    try:
        validate_schema(schema_path, obj)
    except jsonschema.exceptions.ValidationError:
        raise Exception("The variant object is not valid.")
    component = obs.ObservationComponent()
    component.code = fhir_codeable_concept(HL7_GENOMICS_MAPPING['variant']['variantLengthCode'])
    component.valueCodeableConcept = fhir_codeable_concept(
        {"id": obj.get('alleleType'), "label": obj.get('alleleType')}
    )
    return component.as_json()


def disease_to_fhir(obj):
    """Converts Disease to FHIR Condition.

    :param obj: Disease json
    :return: FHIR Condition json
    """

    schema_path = os.path.join(SCHEMA_PATH, 'disease_schema.json')
    try:
        validate_schema(schema_path, obj)
    except jsonschema.exceptions.ValidationError:
        raise Exception("The disease object is not valid.")
    condition = cond.Condition()
    if 'id' in obj:
        condition.id = str(obj['id'])
    condition.code = fhir_codeable_concept(obj['term'])
    # subject is required by Pheno-FHIR mapping Guide and by FHIR, set to 'unknown'
    condition.subject = fhirreference.FHIRReference()
    condition.subject.reference = 'unknown'
    condition.extension = []
    # only adds disease-onset if it's ontology term
    # NOTE it is required element by Phenopackets IG but not Phenopackets
    # what do to if it's AGE string?
    if check_disease_onset(obj):
        onset_extension = extension.Extension()
        onset_extension.url = PHENOPACKETS_ON_FHIR_MAPPING['disease']['onset']
        onset_extension.valueCodeableConcept = fhir_codeable_concept(obj['onset']['age'])
        condition.extension.append(onset_extension)

    if 'diseaseStage' in obj:
        for item in obj['diseaseStage']:
            disease_stage_extension = extension.Extension()
            disease_stage_extension.url = PHENOPACKETS_ON_FHIR_MAPPING['disease']['disease_stage']
            disease_stage_extension.valueCodeableConcept = fhir_codeable_concept(item)
            condition.extension.append(disease_stage_extension)

    return condition.as_json()


def _get_section_object(nested_obj, title):
    """Internal function to convert phenopacket m2m objects to Composition section.

    :param nested_obj: m2m relationship object
    :param title: field name that holds m2m relationship
    :return: section content object
    """

    section_content = comp.CompositionSection()
    section_values = PHENOPACKETS_ON_FHIR_MAPPING['phenopacket'][title]
    section_content.title = section_values['title']
    section_content.code = codeableconcept.CodeableConcept()
    section_content.code.coding = []
    coding = c.Coding()
    coding.system = section_values['code']['system']
    coding.version = section_values['code']['version']
    coding.code = section_values['code']['code']
    coding.display = section_values['code']['display']
    section_content.code.coding.append(coding)

    section_content.entry = []
    for item in nested_obj:
        entry = fhirreference.FHIRReference()
        if item.get('id'):
            entry.reference = str(item['id'])
        elif item.get('uri'):
            entry.reference = item['uri']
        else:
            # generate uuid when no 'id' or 'uri' present
            entry.reference = str(uuid.uuid1())
        section_content.entry.append(entry)
    return section_content


def phenopacket_to_fhir(obj):
    """Converts Phenopacket to FHIR Composition.

    :param obj: Phenopacket json
    :return: FHIR Composition json
    """

    schema_path = os.path.join(SCHEMA_PATH, 'phenopacket_schema.json')
    try:
        validate_schema(schema_path, obj)
    except jsonschema.exceptions.ValidationError:
        raise Exception("The disease object is not valid.")
    composition = comp.Composition()
    if 'id' in obj:
        composition.id = obj['id']
    composition.subject = fhirreference.FHIRReference()
    if 'subject' in obj:
        composition.subject.reference = str(obj['subject']['id'])
    composition.title = PHENOPACKETS_ON_FHIR_MAPPING['phenopacket']['title']
    # elements in Composition required by FHIR spec
    composition.status = 'preliminary'
    composition.author = []
    author = fhirreference.FHIRReference()
    author.reference = obj['metaData']['createdBy']
    composition.author.append(author)
    composition.date = fhirdate.FHIRDate(obj['metaData']['created'])
    composition.type = fhir_codeable_concept({
        "id": PHENOPACKETS_ON_FHIR_MAPPING['phenopacket']['code']['code'],
        "label": PHENOPACKETS_ON_FHIR_MAPPING['phenopacket']['title'],
        "system": PHENOPACKETS_ON_FHIR_MAPPING['phenopacket']['code']['system']
    })

    composition.section = []
    # TODO add htsFiles to the list and fix inconsistency in mappings
    sections = ['biosamples', 'variants', 'diseases']
    for section in sections:
        if obj[section]:
            section_content = _get_section_object(obj.get(section, None), section)
            composition.section.append(section_content)

    return composition.as_json()
