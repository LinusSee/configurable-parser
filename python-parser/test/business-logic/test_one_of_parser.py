import unittest

import test.test_utils as test_utils
import src.business_logic.api.parsing as Parsing
import src.business_logic.one_of_parser as OneOfParser



class GivenParserTest(unittest.TestCase):

    def test_matches_one_of_the_given_values(self):
        expected = [(('Loglevel', 'INFO'),)]

        one_of_parser = OneOfParser.OneOfParser('Loglevel', ['INFO', 'INCIDENT', 'ERROR'])

        result = Parsing.parse_text('INFO', [one_of_parser])
        actual = test_utils.remove_eol_eof_column(result)

        self.assertEqual(expected, actual)


    def test_matches_one_of_with_multiple_lines(self):
        expected = [(('Loglevel', 'INFO'),),
                    (('Loglevel', 'INCIDENT'),),
                    (('Loglevel', 'ERROR'),)
                    ]

        one_of_parser = OneOfParser.OneOfParser('Loglevel', ['INFO', 'INCIDENT', 'ERROR'])

        result = Parsing.parse_text('INFO\nINCIDENT\nERROR', [one_of_parser])
        actual = test_utils.remove_eol_eof_column(result)

        self.assertEqual(expected, actual)