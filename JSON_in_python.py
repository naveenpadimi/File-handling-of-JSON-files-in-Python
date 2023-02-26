import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

employee_list = []

with open('employee.json', 'r') as f:
    data = json.load(f)
    for employee_data in data['employees']:
        employee = Employee(employee_data['name'], employee_data['dob'], employee_data['height'], employee_data['city'], employee_data['state'])
        employee_list.append(employee)

for employee in employee_list:
    print(f"Name: {employee.name}, DOB: {employee.dob}, Height: {employee.height}, City: {employee.city}, State: {employee.state}")


import json

states_dict = {
    'Maharashtra': 'Mumbai',
    'Gujarat': 'Gandhinagar',
    'Tamil Nadu': 'Chennai',
    'Karnataka': 'Bengaluru',
    'Punjab': 'Chandigarh',
    'Rajasthan': 'Jaipur',
    'Uttar Pradesh': 'Lucknow'
}

with open('states.json', 'w') as f:
    json.dump(states_dict, f)


# Assignment 2
class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
        
    def description(self):
        print(f"{self.name} is {self.age} years old.")
        
    def get_info(self):
        print(f"{self.name} has a {self.coat_color} coat.")

class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)
        
    def chase(self):
        print(f"{self.name} loves to chase things!")

class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)
        
    def snore(self):
        print(f"{self.name} snores really loudly!")

# Create objects and implement functionalities
dog1 = Dog("Fido", 3, "brown")
dog1.description()
dog1.get_info()

dog2 = JackRussellTerrier("Jack", 2, "white")
dog2.description()
dog2.get_info()
dog2.chase()

dog3 = Bulldog("Rocky", 5, "black")
dog3.description()
dog3.get_info()
dog3.snore()
