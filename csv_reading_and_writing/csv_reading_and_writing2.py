"""for data analysis project_part 1"""

import csv

def read_csv_fieldnames(filename, separator, quote):
    """read filenames"""
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter = separator, quotechar = quote)
        csv_rows = list(reader)
    return list(csv_rows[0])

def read_csv_as_list_dict(filename, separator, quote):
    """read csv as list"""
    field = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter= separator, quotechar = quote)
        for row in reader:
            field.append(row)
    return field

def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """read csv as nested list"""
    table = {}
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter = separator, quotechar = quote)
        for row in reader:
            table[row[keyfield]] = row
    return table

def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):	
    """write files"""
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames = fieldnames,
                 delimiter = separator, quoting = csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for row in table:
            writer.writerow(row)
       
	



