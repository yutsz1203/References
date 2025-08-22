# A child class (subclass) inherits attributes and methods from a parent class (superclass)
# Polymorphism, overriding, overloading

class Employee:
    # Class variables
    raise_amt = 1.04

    # Constructor
    def __init__(self, first, last, pay):
        # these are instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

    def fullName(self):
        return(f"{self.first} {self.last}")
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt) # self.raise_amt or Employee.raise_amt works as well

# Subclass of Employee
class Developer(Employee):
    raise_amt = 1.1

    # Constructor of subclass
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay) this also works
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def addEmployee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def removeEmployee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print(f"-->{emp.fullName()}")

# These are instances
dev_1 = Developer("Mervin","Yu", 50000, "Python")
dev_2 = Developer("Corey", "Schafer", 60000, "cpp")

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print(dev_1.prog_lang)

mng_1 = Manager("Mervin","Yu", 50000, [dev_1])
mng_2 = Manager("Corey", "Schafer", 60000)

mng_1.print_emps()
mng_1.removeEmployee(dev_1)
mng_1.addEmployee(dev_2)
mng_1.print_emps()

print(isinstance(mng_1, Employee))
print(issubclass(Manager, Employee))