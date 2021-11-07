ALLOWED_OPERATORS = ("+", "-", "/", "*")

class Calculator:
    def __init__(self) -> None:
        pass

    def calculate(self, operation: list):
        # sanitize input
        try:
            x, y = int(operation[0]), int(operation[2])
        except ValueError:
            return "Invalid operands"

        operator = operation[1]
        if operator not in ALLOWED_OPERATORS:
            return "Invalid operator"

        if operator == "+":
            # Do addition
            return f"{x + y:.2f}"

        if operator == "/":
            # Do division
            if y == 0:
                return "Can't divide by 0"
            return f"{x / y:.2f}"

        if operator == "-":
            # Do subtraction
            return f"{x - y:.2f}"

        if operator == "*":
            # Do mutliplication
            return f"{x * y:.2f}"

    def format_equation(self, equation: str):
        if " " in equation:
            return equation.split(" ")
        for x in equation:
            if x in ALLOWED_OPERATORS:
                equation = equation.split(x)
                return [equation[0], x, equation[1]]
