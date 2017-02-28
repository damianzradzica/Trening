class Employee(object):
    def __init__(self, id, first_name, last_name, salary):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def raise_salary(self, value):
        if isinstance(value, float) and value > 0:
            self.salary += value * self.salary
            return self.salary
        else:
            raise ValueError('nieprawidłowa wartość')

mariusz = Employee(123, 'mariusz', 'kowalski', 1200)
mariusz.raise_salary(0.1)
print(mariusz.salary)
