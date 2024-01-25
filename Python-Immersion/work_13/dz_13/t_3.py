class InvalidNameError(Exception):
    pass


class InvalidAgeError(Exception):
    pass


class InvalidIdError(Exception):
    pass


class Person:
    def __init__(self, last_name, first_name, middle_name, age):
        
        # if not isinstance(last_name, str) or last_name == "":
        #     raise InvalidNameError(f'Invalid name: . Name should be a non-empty string.')
        # if not isinstance(first_name, str) or first_name == "":
        #     raise InvalidNameError("Invalid name: . Name should be a non-empty string.")
        # if not isinstance(middle_name, str) or middle_name == "":
        #     raise InvalidNameError("Invalid name: . Name should be a non-empty string.")
        
        if last_name == "" or first_name == "" or middle_name == "":
            raise InvalidNameError("Invalid name: . Name should be a non-empty string.")
        
        if not isinstance(age, int) or age <= 0:
            raise InvalidAgeError(f"Invalid age: {age}. Age should be a positive integer.")
        
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name

        
        self.age = age

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}, {self.age} years old"

class Employee(Person):
    def __init__(self, last_name, first_name, middle_name, age, ID):
        super().__init__(last_name, first_name, middle_name, age)
        if not isinstance(ID, int) or ID <= 0 or ID > 999999:
            raise InvalidIdError("Invalid ID")
        self.ID = ID

    def get_level(self):
        return sum(int(digit) for digit in str(self.ID)) % 7

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}, {self.age} years old, ID: {self.ID}"

# person = Person("", "John", "Doe", 30)
# person = Person("Alice", "Smith", "Johnson", -5)  
# employee = Employee("Bob", "Johnson", "Brown", 40, 12345)

person = Person("Alice", "Smith", "Johnson", 25)
print(person.get_age())

print()