import datetime


class Employee:
    # Class variables
    raise_amt = 1.04
    num_of_emps = 0

    # Constructor
    def __init__(self, first, last, pay):
        # these are instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

        Employee.num_of_emps += 1

    # Instance method
    # automatically takes the self, instance, as the argument
    # access to instance variables

    def getName(self):
        print(f"{self.first} {self.last}")

    def apply_raise(self):
        self.pay = int(
            self.pay * self.raise_amount
        )  # self.raise_amount or Employee.raise_amount works as well

    # Class method
    # automatically takes the cls, class, as the argument
    # access to class variables
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    # alternative constructor using classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    # don't take the class or instance as the first argument
    # no access to class or instance variables
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# These are instances
emp_1 = Employee("Mervin", "Yu", 50000)
emp_2 = Employee("Corey", "Schafer", 60000)

Employee.set_raise_amt(0.99)
print(Employee.raise_amt)
print(emp_1.raise_amt)

emp_1.set_raise_amt(1.05)  # this also changes the class variable
print(Employee.raise_amt)
print(emp_1.raise_amt)

emp_str_1 = "John-Doe-70000"
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)

my_date = datetime.date(2016, 7, 10)

print(Employee.is_workday(my_date))
