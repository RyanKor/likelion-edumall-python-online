class Calculator:
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result = self.result + num
        return self.result


cal1 = Calculator()
cal2 = Calculator()

print(cal1.adder(5) + cal2.adder(2134))
