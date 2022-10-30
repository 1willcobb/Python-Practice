import json
import 

class Person:

    def __init__(self, name: str, age: int, weight: int) -> None:
        self.name = name
        self.age = age
        self.weight = weight

    def print_info(self):
        print(self.name, self.age, self.weight)

    def get_older(self, years):
        self.age += years

    def save_to_json(self, filename):
        person_dict = {'name': self.name, 'age': self.age, 'weight': self.weight}
        with open(filename, 'w') as f:
            f.write(json.dumps(person_dict, indent=2))

    def load_from_json(self, filename):
        with open(filename, 'r') as f:
            data = json.loads(f.read())

        self.name = data['name']
        self.age = data['age']
        self.weight = data['weight']

p1 = Person(None, None, None)
p1.load_from_json('./test/test.json')
p1.print_info()
