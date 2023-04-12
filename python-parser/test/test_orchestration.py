import unittest
import os as os
import shutil

import test.test_utils as test_utils

import src.business_logic.parsing_config as ParsingConfig
import src.orchestration.orchestration as OC
import src.business_logic.given_parser as GivenParser
import src.business_logic.until_end_parser as UntilEndParser



input_files_basepath = os.getcwd() + '\\test\\data'
output_files_basepath = os.getcwd() + '\\test\\data\\results'


class OrchestrationTest(unittest.TestCase):

    def setUp(self):
        os.makedirs(output_files_basepath, exist_ok=True)

    def tearDown(self):
        # Delete result directory including all files created
        shutil.rmtree(output_files_basepath)



    def test_file_is_being_read_and_parsed(self):
        expected = [(('IntroString', 'Loglevel: '), ('TestColumn', 'Test')),
                    (('IntroString', 'Loglevel: '), ('TestColumn', 'Test'))
                    ]

        input_file = input_files_basepath + '\\basic-multiline-two-values.txt'
        output_file = output_files_basepath + '\\parsing-result.csv'

        given_parser_loglevel = GivenParser.GivenParser('IntroString', 'Loglevel: ')
        given_parser_test = GivenParser.GivenParser('TestColumn', 'Test')
        parsers = [given_parser_loglevel, given_parser_test]

        parsing_config = ParsingConfig.ParsingConfig(input_file, output_file, parsers)
        result = OC.parse_file(parsing_config)
        actual = test_utils.remove_eol_eof_column(result)

        self.assertEqual(expected, actual)
        self.assertEqual(expected, test_utils.read_csv_as_parsing_data(output_file))

    

    def test_can_parse_full_example(self):
        expected = [(('IntroString', 'Loglevel: '), ('TestColumn', 'Test'), ('ItsTheEndOfTheLine', 'this is the end')),
                    (('IntroString', 'Loglevel: '), ('TestColumn', 'Test'), ('ItsTheEndOfTheLine', 'you know'))
                    ]
        
        input_file = input_files_basepath + '\\full_example.txt'
        output_file = output_files_basepath + '\\parsing-result.csv'

        given_parser_loglevel = GivenParser.GivenParser('IntroString', 'Loglevel: ')
        given_parser_test = GivenParser.GivenParser('TestColumn', 'Test')
        until_end_parser = UntilEndParser.UntilEndParser('ItsTheEndOfTheLine')
        parsers = [given_parser_loglevel, given_parser_test, until_end_parser]

        parsing_config = ParsingConfig.ParsingConfig(input_file, output_file, parsers)
        result = OC.parse_file(parsing_config)
        actual = test_utils.remove_eol_eof_column(result)

        self.assertEqual(expected, actual)
        self.assertEqual(expected, test_utils.read_csv_as_parsing_data(output_file))
