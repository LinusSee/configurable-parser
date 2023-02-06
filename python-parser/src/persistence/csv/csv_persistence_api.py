import csv



def save_parsing_result(filename, parsing_result):
    # Map parsing_result
    result_without_newlines = __remove_eol_eof_column(parsing_result)
    data_rows = __map_to_csv_data(result_without_newlines)

    # Call CSV writing module
    __save_as_csv(filename, data_rows)



def __map_to_csv_data(parsing_result):
    if len(parsing_result) <= 0:
        return []

    headers = list(map(lambda x: x[0], parsing_result[0]))
    values = list(map(__extract_values_for_row, parsing_result))
    print('Headers: ', headers)
    print('Values: ', values)

    return [headers] + values



def __extract_values_for_row(row):
    extract_fn = lambda tuple: tuple[1]

    return list(map(extract_fn, row))



def __save_as_csv(filename, data_rows):
    with open(filename, 'w+', newline='') as csvfile:
       rowwriter = csv.writer(csvfile, delimiter=';') 
       rowwriter.writerows(data_rows)



def __remove_eol_eof_column(actual: list[(any)]):
    removal_fn = lambda row: row[:-1]

    return list(map(removal_fn, actual))