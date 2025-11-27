from dataclasses import dataclass

@dataclass
class person:
  name: str
  age: int
  email: str

person1 = Person("김철수", 30, "kim@example.com")
print(person)    # Person(name='김철수', age=30, email='kim@example.com')
print(person.name)    # 김철수
