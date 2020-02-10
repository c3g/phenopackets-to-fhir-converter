import unittest
from converters.resources import fhir_observation
from .constants import PHENOTYPIC_FEATURE


class ObservationTestCase(unittest.TestCase):
    def test_phenotypic_feature(self):
        phenotypic_feature = fhir_observation(PHENOTYPIC_FEATURE)
        self.assertIsInstance(phenotypic_feature['extension'], list)
        self.assertEqual(phenotypic_feature['resourceType'], 'Observation')
        for i, extension in enumerate(phenotypic_feature['extension']):
            self.assertIsNotNone(extension['url'])
            if 'valueCodeableConcept' in extension:
                self.assertIsInstance(extension['valueCodeableConcept'], dict)
                self.assertIsInstance(extension['valueCodeableConcept']['coding'], list)


if __name__ == '__main__':
    unittest.main()
