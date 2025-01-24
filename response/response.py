from validator_collection import validators, checkers, errors

def main():
    print(validate(input("What's your email address? ")))

def validate(email):
    if checkers.is_email(email):
        return "Valid"
    return "Invalid"

if __name__ == "__main__":
    main()
