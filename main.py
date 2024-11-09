operand1 = int(input("Enter first operand: \n"))
operation = input("Enter operation (+, -, *,/): \n")
operand2 = int(input("Enter second operand: \n"))

class Calculator:
    def add(operand1, operand2):
        result = operand1 + operand2
        print(f"{operand1} + {operand2} = {result}")
    def subtract(operand1, operand2):
        result = operand1 - operand2
        print(f"{operand1} - {operand2} = {result}")
    def multiply(operand1, operand2):
        result = operand1 * operand2
        print(f"{operand1} * {operand2} = {result}")
    def divide(operand1, operand2):
        result = operand1 / operand2
        print(f"{operand1} / {operand2} = {result}")

match operation:
    case "+":
        Calculator.add(operand1, operand2)
    case "-":
        Calculator.subtract(operand1, operand2)
    case "*":
        Calculator.multiply(operand1, operand2)
    case "/":
        Calculator.divide(operand1, operand2)
    case _:
        print("Invalid input, please enter one of the above mentioned operations.")






