# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os

DATADIR = ""
DATAFILE = "beatles-diskography.csv"


def parse_file(datafile):
    """this method reads a csv file and return a list o f dictionaries"""
    data = []
    delimiter = ","
    with open(datafile, "r") as file:
        header = file.readline().split(delimiter)
        line_counter = 0
        for line in file:
            if line_counter == 10:
                break

            fields = line.split(delimiter)
            register = {}
            for i, value in enumerate(fields):
                register[header[i].strip()] = value.strip()

            data.append(register)
            line_counter += 1

    return data


def test():
    """test   parse_file """
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    data = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1',
                 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1',
                 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert data[0] == firstline
    assert data[9] == tenthline


test()
