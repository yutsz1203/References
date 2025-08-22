class Employee:
    # Class variables
    raise_amount = 1.04
    num_of_emps = 0

    # Constructor
    def __init__(self, first, last, pay):
        # these are instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

        Employee.num_of_emps += 1
    # Class method
    def getName(self):
        print(f"{self.first} {self.last}")
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # self.raise_amount (per instance) or Employee.raise_amount (same across instances) works as well


# These are instances
emp_1 = Employee("Mervin","Yu", 50000)
emp_2 = Employee("Corey", "Schafer", 60000)


print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

Employee.raise_amount = 1.05 # this change all instances of employee
emp_1.raise_amount = 1.06 # this only changes emp1

print(Employee.raise_amount)
print(emp_1.raise_amount)

print(Employee.num_of_emps)
