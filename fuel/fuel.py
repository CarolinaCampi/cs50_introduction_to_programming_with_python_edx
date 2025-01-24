def main():
    percentage = check_input()

    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(str(percentage) + "%")

def check_input():
    while True:
        user_fraction_parts = input("Fraction: ").strip().split("/")
        try:
            first_part = int(user_fraction_parts[0])
            second_part = int(user_fraction_parts[1])
            percentage = round(100 * float(first_part) / float(second_part))
            if percentage <= 100:
                return percentage
        except (ValueError, ZeroDivisionError):
            pass

main()
