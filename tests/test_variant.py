import unittest
from converters.resources import variant_to_fhir
from .constants import VARIANT


class VariantTestCase(unittest.TestCase):
    def test_gene(self):
        observation_component_v = variant_to_fhir(VARIANT)
        self.assertIsInstance(observation_component_v['code'], dict)
        self.assertIsInstance(observation_component_v['code']['coding'], list)
        for item in observation_component_v['code']['coding']:
            self.assertIsNotNone(item['code'])
            self.assertEqual(item['display'], 'Structural variant [Length]')
            self.assertEqual(item['system'], 'https://loinc.org')
        self.assertIsInstance(observation_component_v['valueCodeableConcept']['coding'], list)
        for item in observation_component_v['valueCodeableConcept']['coding']:
            self.assertIsNotNone(item['code'])
            self.assertIsNotNone(item['display'])
            self.assertEqual(item['code'], item['display'])


if __name__ == '__main__':
    unittest.main()
