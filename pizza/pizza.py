import sys
from tabulate import tabulate
import csv

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file_name = sys.argv[1]

    if file_name.split(".")[-1] != "csv":
        sys.exit("Not a CSV file")

    table = []

    try:
        with open(file_name) as file:
            reader = csv.reader(file)
            for row in reader:
                table.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(table[1:], table[0], tablefmt="grid"))

main()
