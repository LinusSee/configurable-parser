import unittest

import src.business_logic.api.parsing as Parsing
import src.business_logic.given_parser as GivenParser



class GivenParserTest(unittest.TestCase):


    def test_matchesString_Loglevel_AndHasHeader_IntroString(self):
        expected = [(('IntroString', 'Loglevel: '),)]

        given_parser = GivenParser.GivenParser('IntroString', 'Loglevel: ')

        actual = Parsing.parse_text('Loglevel: ', [given_parser])

        self.assertEqual(expected, actual)


    def test_matchesString_MultipleTimesWithWindowsStyleNewlines(self):
        expected = [(('IntroString', 'Loglevel: '),),
                    (('IntroString', 'Loglevel: '),),
                    (('IntroString', 'Loglevel: '),)
                    ]
        
        given_parser = GivenParser.GivenParser('IntroString', 'Loglevel: ')

        actual = Parsing.parse_text('Loglevel: \r\nLoglevel: \r\nLoglevel: ', [given_parser])

        self.assertEqual(expected, actual)


    def test_matchesString_MultipleTimesWithUnixStyleNewlines(self):
        expected = [(('IntroString', 'Loglevel: '),),
                    (('IntroString', 'Loglevel: '),),
                    (('IntroString', 'Loglevel: '),)
                    ]
        
        given_parser = GivenParser.GivenParser('IntroString', 'Loglevel: ')

        actual = Parsing.parse_text('Loglevel: \nLoglevel: \nLoglevel: ', [given_parser])

        self.assertEqual(expected, actual)




if __name__ == "__main__":
    unittest.main()