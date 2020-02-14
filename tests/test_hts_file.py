import unittest
from converters.resources import hts_file_to_fhir
from .constants import HTS_FILE


class HtsFileTestCase(unittest.TestCase):
    def test_hts_file_to_fhir(self):
        document_reference = hts_file_to_fhir(HTS_FILE)
        self.assertIsInstance(document_reference['extension'], list)
        self.assertEqual(len(document_reference['extension']), 1)
        self.assertEqual(document_reference['resourceType'], 'DocumentReference')
        for i, extension in enumerate(document_reference['extension']):
            self.assertIsNotNone(extension['url'])
            self.assertIsNotNone(extension['valueString'])
            self.assertIsInstance(extension['valueString'], str)
        self.assertIsNotNone(document_reference['content'])
        self.assertIsInstance(document_reference['content'], list)
        for item in document_reference['content']:
            self.assertIsNotNone(item['attachment']['url'])
        self.assertEqual(document_reference['status'], 'current')
        self.assertIsInstance(document_reference['type'], dict)
        self.assertIsInstance(document_reference['type']['coding'], list)
        for code in document_reference['type']['coding']:
            self.assertIsNotNone(code['code'])
            self.assertIsNotNone(code['display'])
            self.assertEqual(code['code'], code['display'])


if __name__ == '__main__':
    unittest.main()
