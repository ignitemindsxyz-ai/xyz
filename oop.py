# ENCAPLULATION

class Employee:
    def __init__(self, name, salary, employee_id):
        self.name = name
        self._department = "Unknown"
        self.__salary = salary
        self.__id = employee_id

    def get_salary(self):
        return self.__salary
    
    def give_raise(self, amount):
        if amount > 0:
            self.__salary += amount
        else:
            raise ValueError("Raise amount must be positive")
        
    def __repr__(self):
        return f"Employee({self.name}, ID = {self.__id})"
        
emp = Employee("Alice", 50000, "E001")

print(emp.name)

print(emp._department)

print(emp.get_salary())

print(emp._Employee__salary)

emp.give_raise(5000)
print(emp.get_salary())