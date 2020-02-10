import unittest
from converters.resources import fhir_document_reference
from .constants import HTS_FILE


class DocumentReferenceTestCase(unittest.TestCase):
    def test_hts_file(self):
        hts_file = fhir_document_reference(HTS_FILE)
        self.assertIsInstance(hts_file['extension'], list)
        self.assertEqual(len(hts_file['extension']), 1)
        self.assertEqual(hts_file['resourceType'], 'DocumentReference')
        for i, extension in enumerate(hts_file['extension']):
            self.assertIsNotNone(extension['url'])
            self.assertIsNotNone(extension['valueString'])
            self.assertIsInstance(extension['valueString'], str)
        self.assertIsNotNone(hts_file['content'])
        self.assertIsInstance(hts_file['content'], list)
        for item in hts_file['content']:
            self.assertIsNotNone(item['attachment']['url'])
        self.assertEqual(hts_file['status'], 'current')
        self.assertIsInstance(hts_file['type'], dict)
        self.assertIsInstance(hts_file['type']['coding'], list)
        for code in hts_file['type']['coding']:
            self.assertIsNotNone(code['code'])
            self.assertIsNotNone(code['display'])
            self.assertEqual(code['code'], code['display'])


if __name__ == '__main__':
    unittest.main()
