"""Some helpful utility functions for working with CSV files."""

from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table' (table is a list of dictionaries)."""
    # The parameter is how we load in our data. Input a .csv file.

    result: list[dict[str, str]] = []
    # This is our output list of dictionaries.

    # Open a handle to the data file.
    file_handle = open(filename, "r", encoding="utf8")
    
    # Prepare to read the data file as a CSV rather than just strings.
    # "r" parameter means read in file from disk; encoding="utf8" is a keyword parameter.
    csv_reader = DictReader(file_handle)  # Read that file into a dictionary row by row using python's csv package. Row will be assigned a dictionary of string to string where key is column name (first line of .csv) and value is value for that particular row within the key column (values taken from subsequent lines of .csv).
    # Looping through rows of dictreader. Read each row of the CSV line-by-line. 
    for row in csv_reader:
        result.append(row)  #Save results into new dict [str, str]

    # Close the file when done to free its resources.
    file_handle.close()

    return result

read_csv_rows(str("weather.csv"))

# Function that takes a data table and column and returns a list of values for a particular column.
def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all the values in a single column."""
    # Column is the name of the column from which we want values.
    result: list[str] = []
    for row in table: # For each list in the dictionary of lists.
        item: str = row[column] # Accessing a key within each list.
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]

    for fieldname in first_row:
        result[fieldname] = column_values(row_table, fieldname)

    # TODO: More work!
    return result