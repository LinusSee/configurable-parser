# Python Parser

## Quick start
### Running the project
For a quick start with the example files run
```
python main.py --input-file sample-data/basic-multiline-two-values.txt --output-file result.csv --parser-string 1 "IntroString" "Loglevel: " --parser-string 2 "TestColumn" "Test"
```
and view the resulting `result.csv`.

For a full example containing all parsers run
```
python main.py --input-file sample-data/full-example.txt --output-file result.csv --parser-string 1 "IntroString" "Loglevel: " --parser-one-of 2 "Loglevel" "INFO,INCIDENT,ERROR" --parser-length 3 "FourChars" 4 --parser-until-end "ItsTheEndOfTheLine"
```

### Running the tests
Run `python -m unittest discover -v` to execute the tests.


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