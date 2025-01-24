def main():
    text = input("Please, provide some text to process: ")
    print(convert(text))

def convert(input):
    output = input.replace(":)", "🙂").replace(":(", "🙁")
    return output

main()
