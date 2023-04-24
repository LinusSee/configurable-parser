import unittest

import test.test_utils as test_utils
import src.business_logic.api.parsing as Parsing
import src.business_logic.until_end_parser as UntilEndParser



class GivenParserTest(unittest.TestCase):
    def test_matches_the_entire_line(self):
        expected = [(('ItsTheEndOfTheLine', 'just some line ending'), )]

        until_end_parser = UntilEndParser.UntilEndParser('ItsTheEndOfTheLine')

        actual = Parsing.parse_text('just some line ending\n', [until_end_parser])

        self.assertEqual(expected, actual)


    def test_matches_multiple_lines_with_different_content_and_windows_style_newlines(self):
        expected = [(('ItsTheEndOfTheLine', 'just some line ending'),),
                    (('ItsTheEndOfTheLine', 'another line ending'),),
                    (('ItsTheEndOfTheLine', 'this is the last one'),)
                    ]

        until_end_parser = UntilEndParser.UntilEndParser('ItsTheEndOfTheLine')

        actual = Parsing.parse_text('just some line ending\nanother line ending\nthis is the last one', [until_end_parser])

        self.assertEqual(expected, actual)


    def test_matches_multiple_lines_with_different_content_and_unix_style_newlines(self):
        expected = [(('ItsTheEndOfTheLine', 'just some line ending'),),
                    (('ItsTheEndOfTheLine', 'another line ending'),),
                    (('ItsTheEndOfTheLine', 'this is the last one'),)
                    ]

        until_end_parser = UntilEndParser.UntilEndParser('ItsTheEndOfTheLine')

        actual = Parsing.parse_text('just some line ending\r\nanother line ending\r\nthis is the last one', [until_end_parser])

        self.assertEqual(expected, actual)