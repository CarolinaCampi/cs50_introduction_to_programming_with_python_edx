import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))

# expects an IPv4 address as input as a str and then returns True or False,
# respectively, if that input is a valid IPv4 address or not.
def validate(ip):
    # Format: #.#.#.#
    # # should be a number between 0 and 255, inclusive
    ip = ip.strip()
    return re.fullmatch(r"^(\d|\d\d|1\d\d|2([0-4]\d|5[0-5]))\.(\d|\d\d|1\d\d|2([0-4]\d|5[0-5]))\.(\d|\d\d|1\d\d|2([0-4]\d|5[0-5]))\.(\d|\d\d|1\d\d|2([0-4]\d|5[0-5]))$", ip) is not None

if __name__ == "__main__":
    main()
