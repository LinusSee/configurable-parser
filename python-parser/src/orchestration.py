import parsec as parsec

import src.given_parser as GivenParser
import src.eol_parser as EolParser



def parse_file(filename, parser_configs):
    with open(filename) as file:
        file_content = file.read()
    print('----file contents start')
    print(file_content)
    print('----file contents end')

    return parse_text(file_content, parser_configs)



def parse_text(text, parser_configs):
    string_parser = GivenParser.match_string(parser_configs[0].target_string, parser_configs[0].header)
    string_and_eol_parser = parsec.joint(string_parser, EolParser.eol_or_eof_parser)

    final_parser = parsec.many(string_and_eol_parser)

    return parsec.parse(final_parser, text, 0)