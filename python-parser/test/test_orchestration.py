import unittest
import os as os

import test.test_utils as test_utils
import src.orchestration as OC



testfiles_basepath = os.getcwd() + '\\test\\data'


class OrchestrationTest(unittest.TestCase):

    def test_file_is_being_read_and_parsed(self):
        expected = [('IntroString', 'Loglevel: '),
                    ('IntroString', 'Loglevel: ')
                    ]

        target_path = testfiles_basepath + '\\basic-multiline.txt'
        result = OC.parse_file(target_path)
        actual = test_utils.remove_eol_eof_column(result)

        self.assertEqual(expected, actual)