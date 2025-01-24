def main():
    camel_case = input("camelCase: ").strip()
    snake_case = ""

    for letter in camel_case:
        if letter.isupper() == True:
            snake_case = snake_case + "_" + letter.lower()
        else:
            snake_case = snake_case + letter

    print(snake_case)

main()
