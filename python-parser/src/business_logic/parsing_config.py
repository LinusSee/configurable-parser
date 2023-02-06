class ParsingConfig:
    def __init__(self, input_filename, output_filename, configured_parsers):
        self.input_filename = input_filename
        self.configured_parsers = configured_parsers
        self.output_filename = output_filename