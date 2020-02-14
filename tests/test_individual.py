import unittest
from converters.resources import individual_to_fhir
from .constants import INDIVIDUAL


class IndividualTestCase(unittest.TestCase):
    def test_individual(self):
        patient = individual_to_fhir(INDIVIDUAL)
        self.assertIsInstance(patient['extension'], list)
        self.assertEqual(len(patient['extension']), 3)
        self.assertEqual(patient['resourceType'], 'Patient')
        for i, extension in enumerate(patient['extension']):
            self.assertIsNotNone(extension['url'])
            if 'valueCodeableConcept' in extension:
                self.assertIsInstance(extension['valueCodeableConcept'], dict)
                self.assertIsInstance(extension['valueCodeableConcept']['coding'], list)


if __name__ == '__main__':
    unittest.main()
