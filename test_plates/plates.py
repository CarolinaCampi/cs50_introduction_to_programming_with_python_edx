def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # “All vanity plates must start with at least two letters.”
    # “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    if not (s[:2].isalpha()) or not (len(s) <= 6) or not (len(s) >= 2):
        return False
    else:
        for i in range(len(s[2:]) - 1):
            # “Numbers cannot be used in the middle of a plate; they must come at the end.
            if s[2 + i].isnumeric():
                if not s[2 + i + 1].isnumeric():
                    return False
                # The first number used cannot be a ‘0’.”
                elif s[2 + i] == "0" and s[2 + i - 1].isalpha():
                    return False
            # “No periods, spaces, or punctuation marks are allowed.”
            # Using ASCII order or characters
            elif s[2 + i] < "A":
                return False
    return True


if __name__ == "__main__":
    main()
