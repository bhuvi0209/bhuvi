def calculator():
    num1 = float(input("enter the first number (num1): "))
    num2 = float(input("enter the second number (num2): "))
    operator = input("enter the operator ('+', '-', '*', '/' ): ")

    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"

result = calculator()
print(result)
