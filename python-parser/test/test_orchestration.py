import unittest
import os as os
import shutil

import test.test_utils as test_utils

import src.business_logic.parsing_config as ParsingConfig
import src.orchestration.orchestration as OC
import src.business_logic.given_parser as GivenParser



input_files_basepath = os.getcwd() + '\\test\\data'
output_files_basepath = os.getcwd() + '\\test\\data\\results'


class OrchestrationTest(unittest.TestCase):

    def setUp(self):
        os.makedirs(output_files_basepath, exist_ok=True)

    def tearDown(self):
        # Delete directory including all files created
        shutil.rmtree(output_files_basepath)



    def test_file_is_being_read_and_parsed(self):
        expected = [(('IntroString', 'Loglevel: '),),
                    (('IntroString', 'Loglevel: '),)
                    ]

        input_file = input_files_basepath + '\\basic-multiline.txt'
        output_file = output_files_basepath + '\\parsing-result.csv'
        given_parser = GivenParser.GivenParser('IntroString', 'Loglevel: ')

        parsing_config = ParsingConfig.ParsingConfig(input_file, output_file, [given_parser])
        result = OC.parse_file(parsing_config)
        actual = test_utils.remove_eol_eof_column(result)

        self.assertEqual(expected, actual)
        self.assertEqual(expected, test_utils.read_csv_as_parsing_data(output_file))