import inflect

p = inflect.engine()

def main():

    greeting = "Adieu, adieu, to "
    names = []
    while True:
        try:
            names.append(input("Name: ").strip().lower().title())
        except EOFError:
            greeting = greeting + p.join(names)

            print()
            print(greeting)
            break

main()
