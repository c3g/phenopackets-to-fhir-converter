import unittest
from converters.resources import fhir_specimen
from .constants import BIOSAMPLE


class SpecimenTestCase(unittest.TestCase):
    def test_individual(self):
        biosample = fhir_specimen(BIOSAMPLE)
        self.assertIsInstance(biosample['extension'], list)
        self.assertEqual(biosample['resourceType'], 'Specimen')
        for i, extension in enumerate(biosample['extension']):
            self.assertIsNotNone(extension['url'])
            if 'valueCodeableConcept' in extension:
                self.assertIsInstance(extension['valueCodeableConcept'], dict)
                self.assertIsInstance(extension['valueCodeableConcept']['coding'], list)
            if extension['url'] == "http://ga4gh.org/fhir/phenopackets/StructureDefinition/biosample-diagnostic-markers":
                self.assertIsInstance(extension['valueCodeableConcept']['coding'], list)
                self.assertEqual(len(extension['valueCodeableConcept']['coding']), 2)
        self.assertIsInstance(biosample['collection'], dict)
        self.assertIsNotNone(biosample['collection']['bodySite'])
        self.assertIsNotNone(biosample['type'])


if __name__ == '__main__':
    unittest.main()
