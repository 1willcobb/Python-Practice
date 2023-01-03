from dataclasses import dataclass, field

@dataclass(order=True)
class Person:
	sort_index: int = field(init=False, repr=False)
	name: str
	job: str
	age: int
	attack: int = 50

	def __str__(self):
		return f'{self.name}, {self.job}, {self.age}'

person1 = Person("Will", "CEO", 32, 95)
person2 = Person("Sav", "Editor", 27)
person3 = Person("Dragon", "COO", 34, 95 )

print(person1)
print(person2)
