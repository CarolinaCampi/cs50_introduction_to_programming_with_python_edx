import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.search(r"^(?P<start_hour>\d\d?)(:?\:(?P<start_minutes>\d\d))? (?P<start_period>AM|PM) to (?P<end_hour>\d\d?)(:?\:(?P<end_minutes>\d\d))? (?P<end_period>AM|PM)$", s)
    if match is None or validate_minutes(match.group("start_minutes")) or validate_minutes(match.group("end_minutes")) or int(match.group("start_hour")) > 12 or int(match.group("end_hour")) > 12:
        raise ValueError

    return f"{convert_hour(match.group("start_hour"), match.group("start_period"))}:{convert_minutes(match.group("start_minutes"))} to {convert_hour(match.group("end_hour"), match.group("end_period"))}:{convert_minutes(match.group("end_minutes"))}"

def validate_minutes(minutes):
    if minutes == None or int(minutes) < 60:
        return False
    elif int(minutes) >= 60:
        return True

def convert_hour(hour, period):
    if period == "AM":
        if len(hour) < 2:
            return f"0{hour}"
        elif hour == "12":
            return "00"
        return hour
    elif hour == "12":
        return hour
    return str(int(hour) + 12)

def convert_minutes(minutes):
    if minutes:
        return minutes
    else:
        return "00"

if __name__ == "__main__":
    main()
