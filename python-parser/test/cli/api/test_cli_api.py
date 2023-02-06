import os
import unittest

import src.cli.api.cli_api as CliApi
import test.test_utils as test_utils



testfiles_basepath = os.getcwd() + '\\test\\data'
output_files_basepath = os.getcwd() + '\\test\\data\\results'


class CliApiTest(unittest.TestCase):

    def setUp(self):
        os.makedirs(output_files_basepath, exist_ok=True)


    def test_input_file_parameter_is_required(self):
        cli_arguments = ['--output-file', testfiles_basepath + '\\results\\does-not-matter.csv',
                        '--parser-string', 'IntroString', 'Loglevel: ']
        
        with self.assertRaises(SystemExit):
            CliApi.parse_with_arguments(cli_arguments)


    def test_output_file_parameter_is_required(self):
        cli_arguments = ['--input-file', testfiles_basepath + '\\does-not-matter.txt',
                        '--parser-string', 'IntroString', 'Loglevel: ']
        
        with self.assertRaises(SystemExit):
            CliApi.parse_with_arguments(cli_arguments)



    def test_at_least_one_parser_must_be_configured(self):
        cli_arguments = ['--input-file', 'does_not_matter.txt',
                        '--output-file', testfiles_basepath + '\\results\\parsing-result.csv']
        
        with self.assertRaises(SystemExit):
            CliApi.parse_with_arguments(cli_arguments)



    def test_applies_configured_parsers(self):
        expected = [(('IntroString', 'Loglevel: '),),
                    (('IntroString', 'Loglevel: '),)
                    ]

        output_file = testfiles_basepath + '\\results\\parsing-result.csv'
        cli_arguments = ['--input-file', testfiles_basepath + '\\basic-multiline.txt',
                        '--output-file', output_file,
                        '--parser-string', 'IntroString', 'Loglevel: ']

        result = CliApi.parse_with_arguments(cli_arguments)
        actual = test_utils.remove_eol_eof_column(result)

        self.assertEqual(expected, actual)
        self.assertEqual(expected, test_utils.read_csv_as_parsing_data(output_file))