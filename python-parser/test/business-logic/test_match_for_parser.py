import unittest

import src.business_logic.api.parsing as Parsing
import src.business_logic.match_for_parser as MatchForParser


class MatchForParserTest(unittest.TestCase):
    
    def test_matches_the_given_number_of_chars(self):
        expected = [(('FourChars', 'Four'),)]

        match_for_parser = MatchForParser.MatchForParser('FourChars', 4)

        actual = Parsing.parse_text('Four', [match_for_parser])

        self.assertEqual(expected, actual)