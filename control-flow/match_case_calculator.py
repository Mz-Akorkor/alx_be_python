num1 = num1 = float(input("Enter the first number: "))

num2 = float(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")

match operation:

    case "+":
        addition = num1 + num2
        print(f"The result is {addition}")

    case "-":
        subtraction = num1 - num2
        print(f"The result is {subtraction}")

    case "*":
        multiplication = num1 * num2
        print(f"The result is {multiplication}")

    case "/":
        if num2 != 0:
            division = num1 / num2
            print(f"The result is {division}")
        else:
            print("Cannot divide by zero.")

