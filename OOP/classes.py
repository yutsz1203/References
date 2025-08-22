class Employee:

    # Constructor
    def __init__(self, first, last, pay):
        # these are instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

    # Class method
    def getName(self):
        print(f"{self.first} {self.last}")
    
   

# These are instances
emp_1 = Employee("Mervin","Yu", 50000)
emp_2 = Employee("Corey", "Schafer", 60000)

emp_1.getName()
emp_2.getName()

# We can pass instances to class methods
Employee.getName(emp_1)

