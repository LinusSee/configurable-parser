import parsec as parsec


def __match_char():
    return parsec.none_of('\r\n')


''' Matches every character except:
        - \\r
        - \\n
'''
char_parser = __match_char()