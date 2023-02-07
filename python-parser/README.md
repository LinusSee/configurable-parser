# Python Parser

## Usage
To run the parser you need to configure 3 things:

1. `--input-file`: The filename specifying where the data to be parsed is coming from
2. `--output-file`: The filename to which the result should be written
3. A list of parsers that should be applied to the data, see [configuring parsers](#1-configuring-parsers)

### Configuring parsers
Configuring a parsers consist of 4 parts, and could look like this `--parser-string <parser-position>', '<header-name>', '<target-string>`.
- `--parser-string`: The flag indication what kind of parser you are configuring, here we simply want to match a fixed string
- `<parser-position>`: The position of the parser as a number. This is used to determine the order of execution, starting with the lowest value.
- `<header-name>`: A string describing the value being parsed, e.g. "Loglevel" when parsing "INFO/WARN/ERROR"
- `<target-string>`: The target value, in this case a fixed string. In some cases this is optional or takes a list of values