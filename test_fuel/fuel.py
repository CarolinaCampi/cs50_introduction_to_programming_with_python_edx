def main():
    while True:
        fraction = input("Fraction: ").strip()
        if convert(fraction) != -1:
            break
    print(gauge(convert(fraction)))


def convert(fraction):
    fraction_parts = fraction.split("/")
    try:
        percentage = round(100 * float(fraction_parts[0]) / float(fraction_parts[1]))
        if percentage <= 100:
            return percentage
    except (ValueError, ZeroDivisionError):
        return -1


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
