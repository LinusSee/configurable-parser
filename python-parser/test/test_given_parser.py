import unittest

import src.orchestration as OC


class GivenParserTest(unittest.TestCase):
    def test_matchesString_Loglevel_AndHasHeader_IntroString(self):
        expected = ('IntroString', 'Loglevel: ')
        actual = OC.parseText("Loglevel: asdf")

        self.assertEqual(expected, actual)




if __name__ == "__main__":
    unittest.main()