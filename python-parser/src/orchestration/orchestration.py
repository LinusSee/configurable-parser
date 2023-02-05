import parsec as parsec

import src.cli_arguments_as_parsers as ArgumentMapping
import src.business_logic.api.parsing as Parsing



def parse_file(parsing_config):
    filename = parsing_config.input_filename
    parser_configs = parsing_config.configured_parsers

    parsing_result =  Parsing.parse_file(filename, parser_configs)

    # Save <parsing_result>

    # Return currently only for debugging, will not be necessary once it is written to a file
    return parsing_result