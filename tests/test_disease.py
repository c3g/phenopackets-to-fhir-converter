import unittest
from converters.resources import disease_to_fhir
from .constants import DISEASE


class DiseaseTestCase(unittest.TestCase):
    def test_disease_to_fhir(self):
        condition = disease_to_fhir(DISEASE)
        self.assertEqual(condition['resourceType'], 'Condition')
        self.assertIsInstance(condition['code'], dict)
        self.assertIsInstance(condition['code']['coding'], list)
        for item in condition['code']['coding']:
            self.assertIsNotNone(item['code'])
            self.assertIsNotNone(item['display'])
        self.assertEqual(condition['subject']['reference'], 'unknown')
        self.assertEqual(condition['extension'][0]['url'],
                         'http://ga4gh.org/fhir/phenopackets/StructureDefinition/disease-tumor-stage')
        self.assertIsInstance(condition['extension'][0]['valueCodeableConcept'], dict)
        self.assertEqual(condition['extension'][0]['valueCodeableConcept']['coding'][0]['code'], 'NCIT:C28091')
        self.assertEqual(condition['extension'][0]['valueCodeableConcept']['coding'][0]['display'], 'Gleason Score 7')


if __name__ == '__main__':
    unittest.main()
