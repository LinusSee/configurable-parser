import unittest

import test.test_utils as test_utils
import src.business_logic.api.parsing as Parsing
import src.business_logic.given_parser as GivenParser



class GivenParserTest(unittest.TestCase):


    def test_matchesString_Loglevel_AndHasHeader_IntroString(self):
        expected = [(('IntroString', 'Loglevel: '),)]

        given_parser = GivenParser.GivenParser('IntroString', 'Loglevel: ')

        result = Parsing.parse_text('Loglevel: ', [given_parser])
        actual = test_utils.remove_eol_eof_column(result)

        self.assertEqual(expected, actual)


    def test_matchesString_MultipleTimesWithWindowsStyleNewlines(self):
        expected = [(('IntroString', 'Loglevel: '),),
                    (('IntroString', 'Loglevel: '),),
                    (('IntroString', 'Loglevel: '),)
                    ]
        
        given_parser = GivenParser.GivenParser('IntroString', 'Loglevel: ')

        result = Parsing.parse_text('Loglevel: \r\nLoglevel: \r\nLoglevel: ', [given_parser])
        actual = test_utils.remove_eol_eof_column(result)

        self.assertEqual(expected, actual)

    def test_matchesString_MultipleTimesWithUnixStyleNewlines(self):
        expected = [(('IntroString', 'Loglevel: '),),
                    (('IntroString', 'Loglevel: '),),
                    (('IntroString', 'Loglevel: '),)
                    ]
        
        given_parser = GivenParser.GivenParser('IntroString', 'Loglevel: ')

        result = Parsing.parse_text('Loglevel: \nLoglevel: \nLoglevel: ', [given_parser])
        actual = test_utils.remove_eol_eof_column(result)

        self.assertEqual(expected, actual)




if __name__ == "__main__":
    unittest.main()