import parsec as parsec

import src.given_parser as GivenParser
import src.eol_parser as EolParser


def parseText(text):
    stringParser = GivenParser.matchString('Loglevel: ', 'IntroString')
    stringAndEolParser = parsec.joint(stringParser, EolParser.eolOrEofParser)

    finalParser = parsec.many(stringAndEolParser)

    return parsec.parse(finalParser, text, 0)