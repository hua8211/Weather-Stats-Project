"""Process a dataset stored in a CSV format."""


__author__ = "730389239"

import sys
from typing import List
from csv import DictReader

if len(sys.argv) != 4:
    print("Usage: python -m projects.pj01.weather [FILE] [COLUMN] [OPERATION]")
    exit()

FILE: str = sys.argv[1]
COLUMN: str = sys.argv[2]
OPERATION: str = sys.argv[3]


def main() -> None:
    """Evalute for the given operation."""
    if OPERATION == "list":
        print(list_values())
    elif OPERATION == "min":
        min_value()
    elif OPERATION == "max":
        max_value()
    elif OPERATION == "avg":
        avg_value()
    elif OPERATION == "chart":
        chart_data(list_values(), COLUMN, list_dates())
    else:
        print("Invalid operation: " + OPERATION)
        exit()
    

def list_values() -> List[float]:
    """List all the values for the given columen."""
    file_handle = open(FILE, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    result: List[float] = []
    column_exist: bool = False
    for row in csv_reader:
        for column in row:
            if column == COLUMN:
                column_exist = True
                if row[column] != '':
                    try:
                        result.append(float(row[column]))
                    except ValueError:
                        ...
    if column_exist:
        file_handle.close()
        return(result)
    else:
        print("Invalid column: " + COLUMN)
        exit()
    

def min_value() -> None:
    """Find the lowest values for the given column."""
    values: List[float] = list_values()
    smallest_value: float = 0
    i: int = 0
    while i < len(values):
        if i == 0:
            smallest_value = values[i]
            i += 1
        else:
            if values[i] < smallest_value:
                smallest_value = values[i]
                i += 1
            else:
                i += 1
    print(smallest_value)


def max_value() -> None:
    """Find the largest values for the given column."""
    values: List[float] = list_values()
    maximum_value: float = 0
    i: int = 0
    while i < len(values):
        if i == 0:
            maximum_value = values[i]
            i += 1
        else:
            if values[i] > maximum_value:
                maximum_value = values[i]
                i += 1
            else:
                i += 1
    print(maximum_value)


def avg_value() -> None:
    """Find the mean of all values for the given column."""
    values: List[float] = list_values()
    total: float = 0
    i: int = 0
    while i < len(values):
        total += values[i]
        i += 1
    average: float = total / len(values)
    print(average)


def chart_data(data: List[float], column: str, dates: List[str]) -> None:
    """Chart the dates on the x-axis and the values for the given column on the y-axis."""
    import matplotlib.pyplot as plt
    plt.plot(dates, data)
    plt.xlabel("Dates")
    plt.ylabel(column)
    plt.show()


def list_dates() -> List[str]:
    """Find the list of dates used."""
    file_handle = open(FILE, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    result: List[str] = []
    all_dates: List[str] = []
    for row in csv_reader:
        for column in row:
            if column == "REPORT_TYPE":
                if row[column] == "SOD  ":
                    all_dates.append(str(row["DATE"]))
    file_handle.close()
    i: int = 0
    while i < len(all_dates):
        date: str = all_dates[i]
        result.append(date[0:10])
        i += 1
    return result


if __name__ == "__main__":
    main()