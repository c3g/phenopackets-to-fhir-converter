import unittest
from converters.resources import phenotypic_feature_to_fhir
from .constants import PHENOTYPIC_FEATURE


class PhenotypicFeatureTestCase(unittest.TestCase):
    def test_phenotypic_feature_to_fhir(self):
        observation = phenotypic_feature_to_fhir(PHENOTYPIC_FEATURE)
        self.assertIsInstance(observation['extension'], list)
        self.assertEqual(observation['resourceType'], 'Observation')
        for i, extension in enumerate(observation['extension']):
            self.assertIsNotNone(extension['url'])
            if 'valueCodeableConcept' in extension:
                self.assertIsInstance(extension['valueCodeableConcept'], dict)
                self.assertIsInstance(extension['valueCodeableConcept']['coding'], list)


if __name__ == '__main__':
    unittest.main()
