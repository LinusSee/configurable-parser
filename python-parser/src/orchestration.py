import parsec as parsec

import src.given_parser as GivenParser


def parseText(text):
    stringParser = GivenParser.matchString("Loglevel: ", "IntroString")

    return parsec.parse(stringParser, text, 0)