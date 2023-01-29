# configurable-parser
The goal is to write a configurable parser using the parsec library, that can be used to parse e.g. logfiles.

## Requirements

### MVP
- Runs and can be configured via a commandline
- Can process a single file
- Every parser has a header (to give the result a meaningful name)
- The result should be in the form of a csv

Required parsers:
- Parse a fixed number of chars
- Parse a given string
- Parse the rest of the line
- Parse a string out of a list of possibilities

### Future steps
- Can parse strings over multiple lines
- Can process multiple files at once

## Further info
- Use TDD whereever possible (but give TCR a shot first, just for the fun of it)
- Check how to write commits so a CHANGELOG could be generated