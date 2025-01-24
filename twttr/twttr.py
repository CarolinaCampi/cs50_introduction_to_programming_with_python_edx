def main():
    twit = input("Input: ").strip()
    twt = ""

    for letter in twit:
        if letter.lower() != "a" and letter.lower() != "e" and letter.lower() != "i" and letter.lower() != "o" and letter.lower() != "u":
            twt = twt + letter

    print("Output: " + twt)

main()
