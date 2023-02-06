import unittest
import os as os

import test.test_utils as test_utils

import src.business_logic.parsing_config as ParsingConfig
import src.orchestration.orchestration as OC
import src.business_logic.given_parser as GivenParser



testfiles_basepath = os.getcwd() + '\\test\\data'


class OrchestrationTest(unittest.TestCase):

    def test_file_is_being_read_and_parsed(self):
        expected = [('IntroString', 'Loglevel: '),
                    ('IntroString', 'Loglevel: ')
                    ]

        target_path = testfiles_basepath + '\\basic-multiline.txt'
        given_parser = GivenParser.GivenParser('IntroString', 'Loglevel: ')

        parsing_config = ParsingConfig.ParsingConfig(target_path, [given_parser])
        result = OC.parse_file(parsing_config)
        actual = test_utils.remove_eol_eof_column(result)

        self.assertEqual(expected, actual)
        # TODO: Assert CSV File (#14)