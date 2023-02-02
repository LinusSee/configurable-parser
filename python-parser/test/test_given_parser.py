import unittest

import src.orchestration as OC


def remove_eol_column(actual: list[(any)]):
    ''' Remove the last field of each row containing eol/eof.
        It only causes the tests to break if the structure of the tuple changes
        without adding any value.
    '''
    removal_fn = lambda row: row[0]

    return list(map(removal_fn, actual))



class GivenParserTest(unittest.TestCase):
    def test_matchesString_Loglevel_AndHasHeader_IntroString(self):
        expected = [('IntroString', 'Loglevel: ')]
        result = OC.parseText('Loglevel: ')
        actual = remove_eol_column(result)

        self.assertEqual(expected, actual)


    def test_matchesString_MultipleTimesWithWindowsStyleNewlines(self):
        expected = [('IntroString', 'Loglevel: '),
                    ('IntroString', 'Loglevel: '),
                    ('IntroString', 'Loglevel: ')
                    ]
        result = OC.parseText('Loglevel: \r\nLoglevel: \r\nLoglevel: ')
        actual = remove_eol_column(result)

        self.assertEqual(expected, actual)

    def test_matchesString_MultipleTimesWithUnixStyleNewlines(self):
        expected = [('IntroString', 'Loglevel: '),
                    ('IntroString', 'Loglevel: '),
                    ('IntroString', 'Loglevel: ')
                    ]
        result = OC.parseText('Loglevel: \nLoglevel: \nLoglevel: ')
        actual = remove_eol_column(result)

        self.assertEqual(expected, actual)




if __name__ == "__main__":
    unittest.main()