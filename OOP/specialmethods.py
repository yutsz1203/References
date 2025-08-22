class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

    def fullName(self):
        return(f"{self.first} {self.last}")
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # Special methods
    # This is weaker than __str__, if __str__ is not defined, then __repr__ will be used
    def __repr__(self):
        return f"Employee({self.first}, {self.last}, {self.pay})"

    # This will change the output when the user print out employee instance directly, see line 26
    def __str__(self):
        return f"{self.fullName()} - {self.email}"
    
    # Dunder methods
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullName())

emp_1 = Employee("Mervin","Yu", 50000)
emp_2 = Employee("Corey", "Schafer", 60000)

print(emp_1)
print(emp_1.__repr__())
print(emp_1.__str__())

# Only available if dunder methods are defined
print(emp_1 + emp_2)
print(len(emp_1))




