import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file_name = sys.argv[1]

    if file_name.split(".")[-1] != "py":
        sys.exit("Not a Python file")

    try:
        with open(file_name) as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    line_count = 0

    for line in lines:
        line = line.strip()
        if line != "" and line[0] != "#":
            line_count += 1

    print(line_count)

main()
