def main():

    grocery_list = {}

    while True:
        try:
            item = input().strip().lower().upper()
            grocery_list[item] += 1
        except KeyError:
            grocery_list[item] = 1
        except EOFError:
            break
        except KeyboardInterrupt:
            pass

    print()
    for item in sorted(grocery_list):
        print(grocery_list[item], item)

main()
