def main():
    expression = input("Expression: ").strip()
    parts = expression.split(" ")
    first_number = int(parts[0])
    operator = parts[1]
    second_number = parts[2]

    match operator:
        case "+":
            print("%.1f" % (float(first_number) + float(second_number)))
        case "-":
            print("%.1f" % (float(first_number) - float(second_number)))
        case "*":
            print("%.1f" % (float(first_number) * float(second_number)))
        case "/":
            print("%.1f" % (float(first_number) / float(second_number)))

main()
