def main():
    greeting = input("Greeting: ").lower().strip()
    first_five = greeting[:5]
    first_letter = greeting[0:1]
    if first_five == "hello":
        print("$0")
    elif first_letter == "h":
        print("$20")
    else:
        print("$100")

main()
