def main():
    user_time = input("What time is it? ")
    decimal_time = convert(user_time)
    if decimal_time >= 7 and decimal_time <= 8:
        print("breakfast time")
    elif decimal_time >= 12 and decimal_time <= 13:
        print("lunch time")
    elif decimal_time >= 18 and decimal_time <= 19:
        print("dinner time")


def convert(time):
    # converts time, a str in 24-hour format, to the corresponding number of hours as a float
    parts = time.split(":")
    hours = float(parts[0])
    minutes = float(parts[1])
    decimal_time = hours + (minutes / 60)
    return decimal_time

if __name__ == "__main__":
    main()
