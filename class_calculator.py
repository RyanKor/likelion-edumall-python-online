class Calculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def subtract(self):
        result = self.first - self.second
        return result

    def multiplication(self):
        result = self.first * self.second
        return result

    def division(self):
        result = self.first / self.second
        return result

    def remainder(self):
        result = self.first % self.second
        return result


calculate = Calculator(5, 9)

print(calculate.subtract())
