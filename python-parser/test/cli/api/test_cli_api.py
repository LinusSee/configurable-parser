import os
import unittest

import src.cli.api.cli_api as CliApi
import test.test_utils as test_utils



testfiles_basepath = os.getcwd() + '\\test\\data'

class CliApiTest(unittest.TestCase):
    def test_input_file_is_required(self):
        cli_arguments = []
        
        with self.assertRaises(SystemExit):
            CliApi.parse_with_arguments(cli_arguments)



    def test_at_least_one_parser_must_be_configured(self):
        cli_arguments = ['--input-file', 'does_not_matter.txt']
        
        with self.assertRaises(SystemExit):
            CliApi.parse_with_arguments(cli_arguments)



    def test_applies_configured_parsers(self):
        expected = [('IntroString', 'Loglevel: '),
                    ('IntroString', 'Loglevel: ')
                    ]

        cli_arguments = ['--input-file', testfiles_basepath + '\\basic-multiline.txt',
                        '--parser-string', 'IntroString', 'Loglevel: ']

        result = CliApi.parse_with_arguments(cli_arguments)
        actual = test_utils.remove_eol_eof_column(result)

        self.assertEqual(expected, actual)