import src.given_parser as GivenParser



def map_cli_arguments_to_parsers(cli_arguments):
    return list(map(__map_cli_argument_to_parser, cli_arguments))



def __map_cli_argument_to_parser(cli_argument):
    given_parser = GivenParser.GivenParser(cli_argument[0], cli_argument[1])

    return given_parser