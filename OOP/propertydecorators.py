class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    # property allows us to access methods as attributes
    @property
    def email(self):
        return(f"{self.first}.{self.last}@email.com")

    @property
    def fullName(self):
        return(f"{self.first} {self.last}")

    # Setter for property
    @fullName.setter
    def fullName(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last
    
    @fullName.deleter
    def fullName(self):
        print("Delete Name!")
        self.first = None
        self.last = None

    
emp_1 = Employee("Mervin","Yu")
emp_1.fullName = "Corey Schafer" # this line only works when there is a setter property

print(emp_1.first)
print(emp_1.email) # here we can access email without calling it
print(emp_1.fullName)

del emp_1.fullName # this line only works when there is a delete property