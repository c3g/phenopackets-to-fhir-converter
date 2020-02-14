import unittest
from converters.resources import phenopacket_to_fhir
from .constants import PHENOPACKET


class PhenopacketTestCase(unittest.TestCase):
    def test_phenopacket_to_fhir(self):
        composition = phenopacket_to_fhir(PHENOPACKET)
        self.assertEqual(composition['resourceType'], 'Composition')
        self.assertIsInstance(composition['author'], list)
        self.assertEqual(composition['subject']['reference'], 'ind:NA19648')
        self.assertEqual(composition['section'][0]['code']['coding'][0]['code'], 'biosamples')


if __name__ == '__main__':
    unittest.main()
