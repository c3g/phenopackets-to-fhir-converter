import unittest
from converters.resources import fhir_patient
from .constants import INDIVIDUAL


class PatientTestCase(unittest.TestCase):
    def test_individual(self):
        individual = fhir_patient(INDIVIDUAL)
        self.assertIsInstance(individual['extension'], list)
        self.assertEqual(individual['resourceType'], 'Patient')
        for i, extension in enumerate(individual['extension']):
            self.assertIsNotNone(extension['url'])
            if 'valueCodeableConcept' in extension:
                self.assertIsInstance(extension['valueCodeableConcept'], dict)
                self.assertIsInstance(extension['valueCodeableConcept']['coding'], list)


if __name__ == '__main__':
    unittest.main()
