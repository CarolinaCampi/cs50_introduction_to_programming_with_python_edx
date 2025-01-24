import random


def main():
    level = get_level()

    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        for _ in range(3):
            try:
                user_answer = int(input(str(x) + " + " + str(y) + " = "))
            except ValueError:
                print("EEE")
                pass

            if user_answer == (x + y):
                score += 1
                break
            else:
                print("EEE")
        else:
            print(str(x) + " + " + str(y) + " = " + str(x + y))


    print("Score: " + str(score))

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
        except ValueError:
            pass

def generate_integer(level):
        while True:
            if level == 1:
                return random.randint(0, 9)
            elif level == 2:
                return random.randint(10, 99)
            elif level == 3:
                return random.randint(100, 999)


if __name__ == "__main__":
    main()
