import unittest
from converters.resources import gene_to_fhir
from .constants import GENE


class GeneTestCase(unittest.TestCase):
    def test_gene(self):
        observation_component_g = gene_to_fhir(GENE)
        self.assertIsInstance(observation_component_g['code'], dict)
        self.assertIsInstance(observation_component_g['code']['coding'], list)
        for item in observation_component_g['code']['coding']:
            self.assertIsNotNone(item['code'])
            self.assertEqual(item['display'], 'Gene studied [ID]')
            self.assertEqual(item['system'], 'https://loinc.org')
        self.assertIsInstance(observation_component_g['valueCodeableConcept']['coding'], list)
        for item in observation_component_g['valueCodeableConcept']['coding']:
            self.assertIsNotNone(item['code'])
            self.assertIsNotNone(item['display'])
            self.assertEqual(item['system'], 'https://www.genenames.org/')


if __name__ == '__main__':
    unittest.main()
