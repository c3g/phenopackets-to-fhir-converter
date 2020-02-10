import unittest
from converters.resources import fhir_obs_component_region_studied
from .constants import GENE


class ObservationComponentTestCase(unittest.TestCase):
    def test_gene(self):
        gene = fhir_obs_component_region_studied(GENE)
        self.assertIsInstance(gene['code'], dict)
        self.assertIsInstance(gene['code']['coding'], list)
        for item in gene['code']['coding']:
            self.assertIsNotNone(item['code'])
            self.assertEqual(item['display'], 'Gene studied [ID]')
            self.assertEqual(item['system'], 'https://loinc.org')
        self.assertIsInstance(gene['valueCodeableConcept']['coding'], list)
        for item in gene['valueCodeableConcept']['coding']:
            self.assertIsNotNone(item['code'])
            self.assertIsNotNone(item['display'])
            self.assertEqual(item['system'], 'https://www.genenames.org/')


if __name__ == '__main__':
    unittest.main()
