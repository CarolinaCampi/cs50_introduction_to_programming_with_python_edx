import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_name = sys.argv[1]
    output_name = sys.argv[2]

    if input_name.split(".")[-1] != "csv":
        sys.exit("Not a CSV file")

    try:
        with open(input_name, "r") as input_file, open(output_name, "w") as output_file:
            reader = csv.DictReader(input_file)
            writer = csv.DictWriter(output_file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in reader:
                name = row["name"].split(", ")
                writer.writerow(
                    {
                        "first": name[1],
                        "last": name[0],
                        "house": row["house"],
                    }
                )
    except FileNotFoundError:
        sys.exit("File does not exist")

main()
