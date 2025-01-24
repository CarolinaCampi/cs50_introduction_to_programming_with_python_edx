def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    # Input: month-day-year order, formatted like 9/8/1636 or September 8, 1636
    # If the user’s input is not a valid date in either format, prompt the user again.
    # Output: same date in YYYY-MM-DD format
    
    while True:
        user_date = input("Date: ").strip()
        parts_slash = user_date.split("/")
        if len(parts_slash) == 3:
            try:
                if int(parts_slash[0]) <= 12 and int(parts_slash[1]) <= 31:
                    month = f"{int(parts_slash[0]):02}"
                    day = f"{int(parts_slash[1]):0>2}"
                    year = int(parts_slash[2])
                    print(str(year) + "-" + str(month) + "-" + str(day))
                    break
                else:
                    pass
            except ValueError:
                pass
        elif len(parts_slash) == 1:
            parts_space = user_date.split(" ")
            if len(parts_space) == 3:
                try:
                    if parts_space[1].endswith(",") and int(parts_space[1].replace(",", "")) <= 31:
                        month = f"{(months.index(parts_space[0].lower().title()) + 1):02}"
                        day = f"{int(parts_space[1].replace(",", "")):02}"
                        year = int(parts_space[2])
                        print(str(year) + "-" + str(month) + "-" + str(day))
                        break
                    else:
                        pass
                except (KeyError, ValueError):
                    pass

main()
