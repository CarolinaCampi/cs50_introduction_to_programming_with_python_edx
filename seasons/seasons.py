from datetime import date, datetime
import re
import sys
import inflect

p = inflect.engine()

def main():
    try:
        print(calculate(validate_input(input("Date of Birth: "))))
    except ValueError:
        sys.exit("Invalid date")

def calculate(user_date):
    user_date = datetime.strptime(user_date, '%Y-%m-%d').date()
    delta = int((date.today() - user_date).total_seconds() / 60)
    return f"{p.number_to_words(delta, andword="").capitalize()} minutes"

def validate_input(date):
    if re.search(r"^(?P<year>\d\d\d\d)\-(?P<month>0\d|1[012])\-(?P<day>0\d|[12]\d|3[01])$", date):
        return date
    else:
        raise ValueError("Invalid date")


if __name__ == "__main__":
    main()
