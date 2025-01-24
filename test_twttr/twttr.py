def main():
    twit = str(input("Input: ").strip())
    print("Output: " + shorten(twit))

def shorten(word):
    twt = ""
    for letter in word:
        if letter.lower() != "a" and letter.lower() != "e" and letter.lower() != "i" and letter.lower() != "o" and letter.lower() != "u":
            twt = twt + letter

    return twt


if __name__ == "__main__":
    main()
