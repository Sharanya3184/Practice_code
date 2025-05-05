class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Cannot divide by zero"

    def display_results(self):
        print("Addition       :", self.add())
        print("Subtraction    :", self.subtract())
        print("Multiplication :", self.multiply())
        print("Division       :", self.divide())


calc = Calculator(num1=10, num2=5)
calc.display_results()
 