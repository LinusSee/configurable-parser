import parsec as parsec

import src.given_parser as GivenParser
import src.eol_parser as EolParser



def parse_file(filename):
    with open(filename) as file:
        file_content = file.read()
    print('file contents')
    print(file_content)

    return parse_text(file_content)



def parse_text(text):
    string_parser = GivenParser.match_string('Loglevel: ', 'IntroString')
    string_and_eol_parser = parsec.joint(string_parser, EolParser.eol_or_eof_parser)

    final_parser = parsec.many(string_and_eol_parser)

    return parsec.parse(final_parser, text, 0)