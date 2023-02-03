import unittest

import test.test_utils as test_utils
import src.orchestration as OC



class GivenParserTest(unittest.TestCase):
    def test_matchesString_Loglevel_AndHasHeader_IntroString(self):
        expected = [('IntroString', 'Loglevel: ')]
        result = OC.parse_text('Loglevel: ')
        actual = test_utils.remove_eol_eof_column(result)

        self.assertEqual(expected, actual)


    def test_matchesString_MultipleTimesWithWindowsStyleNewlines(self):
        expected = [('IntroString', 'Loglevel: '),
                    ('IntroString', 'Loglevel: '),
                    ('IntroString', 'Loglevel: ')
                    ]
        result = OC.parse_text('Loglevel: \r\nLoglevel: \r\nLoglevel: ')
        actual = test_utils.remove_eol_eof_column(result)

        self.assertEqual(expected, actual)

    def test_matchesString_MultipleTimesWithUnixStyleNewlines(self):
        expected = [('IntroString', 'Loglevel: '),
                    ('IntroString', 'Loglevel: '),
                    ('IntroString', 'Loglevel: ')
                    ]
        result = OC.parse_text('Loglevel: \nLoglevel: \nLoglevel: ')
        actual = test_utils.remove_eol_eof_column(result)

        self.assertEqual(expected, actual)




if __name__ == "__main__":
    unittest.main()