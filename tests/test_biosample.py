import unittest
from converters.resources import biosample_to_fhir
from .constants import BIOSAMPLE


class BiosampleTestCase(unittest.TestCase):
    def test_biosample_to_fhir(self):
        specimen = biosample_to_fhir(BIOSAMPLE)
        self.assertIsInstance(specimen['extension'], list)
        self.assertEqual(specimen['resourceType'], 'Specimen')
        for i, extension in enumerate(specimen['extension']):
            self.assertIsNotNone(extension['url'])
            if 'valueCodeableConcept' in extension:
                self.assertIsInstance(extension['valueCodeableConcept'], dict)
                self.assertIsInstance(extension['valueCodeableConcept']['coding'], list)
            if extension['url'] == "http://ga4gh.org/fhir/phenopackets/StructureDefinition/biosample-diagnostic-markers":
                self.assertIsInstance(extension['valueCodeableConcept']['coding'], list)
                self.assertEqual(len(extension['valueCodeableConcept']['coding']), 2)
        self.assertIsInstance(specimen['collection'], dict)
        self.assertIsNotNone(specimen['collection']['bodySite'])
        self.assertIsNotNone(specimen['type'])


if __name__ == '__main__':
    unittest.main()
