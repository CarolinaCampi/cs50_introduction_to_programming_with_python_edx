import random
import sys

def main():
    level = get_valid_input("Level: ")

    answer = random.randint(1, level)

    while True:
        guess = get_valid_input("Guess: ")

        if guess < answer:
            print("Too small!")
            pass
        elif guess > answer:
            print("Too large!")
            pass
        elif guess == answer:
            sys.exit("Just right!")

def get_valid_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input > 0:
                return user_input
        except ValueError:
            pass

main()
