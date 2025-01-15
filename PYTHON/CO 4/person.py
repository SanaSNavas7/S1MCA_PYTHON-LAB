class Person:
    def __init__(self, name, code):
        self.name = name
        self.code = code

class Account(Person):
    def __init__(self, name, code, pay):
        Person.__init__(self, name, code)
        self.pay = pay

class Admin(Person):
    def __init__(self, name, code, experience):
        Person.__init__(self, name, code)
        self.experience = experience

class Employee(Account, Admin):
    def __init__(self, name, code, pay, experience):
        Account.__init__(self, name, code, pay)
        Admin.__init__(self, name, code, experience)

    def display(self):
        print(f"Name: {self.name}")
        print(f"Code: {self.code}")
        print(f"Pay: {self.pay}")
        print(f"Experience: {self.experience}")

# Example usage
emp = Employee("John Doe", "E123", 50000, 5)
emp.display()
