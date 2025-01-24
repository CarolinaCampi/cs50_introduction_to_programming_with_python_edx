def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting):
    greeting = str(greeting).lower()

    first_five = greeting[:5]
    first_letter = greeting[0:1]

    if first_five == "hello":
        return 0
    elif first_letter == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
