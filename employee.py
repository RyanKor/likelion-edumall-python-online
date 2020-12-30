from class_calculator import Calculator


class Salary(object):
    # class Salary():
    # class Salary(Không đặt giá trị tùy tiện):
    def __init__(self, salary, name, raise_amount):
        self.salary = salary
        self.name = name
        self.raise_amount = raise_amount

    def apply_raise(self):
        self.pay = int(self.salary * self.raise_amount)
        return self.pay

    def full_name(self):
        return '{}'.format(self.name)

    def get_pay(self):
        return "Mức lương hiện tại của '{}' là '{}' ".format(self.full_name(), self.apply_raise())

    def percentage(self):
        self.percent = self.apply_raise() - self.salary
        return "Mức lương của '{}' năm nay đã tăng lên '{}' đồng".format(self.full_name(), self.percent)


emp_2 = Salary(60000, 'Khan', 1.3)
print(emp_2.get_pay())
print(emp_2.percentage())

calculate = Calculator(5, 9)
print(calculate.add())
