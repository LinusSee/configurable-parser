


def remove_eol_eof_column(actual: list[(any)]):
    ''' Remove the last field of each row containing eol/eof.
        The field doesn't add any value to the tests and only causes them to
        break if its structure were to change.
    '''
    removal_fn = lambda row: row[0]

    return list(map(removal_fn, actual))