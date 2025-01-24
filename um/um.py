import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    instances = re.findall(r"\bum\b", s, flags=re.IGNORECASE)
    return len(instances)

if __name__ == "__main__":
    main()
