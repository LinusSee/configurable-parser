import parsec as parsec

import src.business_logic.api.parsing as Parsing
import src.persistence.csv.csv_persistence_api as PersistenceApi



def parse_file(parsing_config):
    input_filename = parsing_config.input_filename
    output_filename = parsing_config.output_filename
    parser_configs = parsing_config.configured_parsers

    parsing_result =  Parsing.parse_file(input_filename, parser_configs)

    # Save <parsing_result>
    PersistenceApi.save_parsing_result(output_filename, parsing_result)

    # Return currently only for debugging, will not be necessary once it is written to a file
    return parsing_result