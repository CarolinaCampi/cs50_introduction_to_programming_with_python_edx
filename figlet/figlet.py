from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
all_fonts = figlet.getFonts()

def main():
    arg_count = len(sys.argv)

    # Check the amount of arguments
    if arg_count != 1 and arg_count != 3:
        sys.exit("Please, provide cero or two arguments.")

    elif arg_count == 1:
        # Ask for user input
        user_input = input("Input: ")

        # Get and set random font
        random_font = random.choice(all_fonts)

        figletify(user_input, random_font)

    # Check the validity of the two relevant arguments
    elif (sys.argv[1] != "-f" and sys.argv[1] != "--font") or (sys.argv[2] not in all_fonts):
        sys.exit("Please, change the arguments so that the first one is -f or --font and the second is a valid font.")

    else:
        # Ask for user input
        user_input = input("Input: ")

        # Get the user font
        user_font = sys.argv[2]

        figletify(user_input, user_font)

def figletify(user_input, f):
        # Set the font
        figlet.setFont(font = f)

        # Print output
        print("Output:")
        print(figlet.renderText(user_input))


main()
