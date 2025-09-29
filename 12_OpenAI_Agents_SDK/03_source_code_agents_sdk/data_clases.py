from dataclasses import dataclass,field
from typing import ClassVar, List

@dataclass
class MyDataclass:
    name: str
    age: int
    language: ClassVar[str] = 'dual'
    # tags = []
    tags: List[str] = field(default_factory=list)


    def show(self):
        # print(f'My name is {self.name} and my age is {self.age} and my language is {self.language}')
        print(f'My name is {self.name} and my age is {self.age} and my language is {MyDataclass.language}')


    @staticmethod
    def show_profession(level):
        print(f'My profession is software engineering and level is {level}')

    



myclass = MyDataclass('Talha',22)
myclass.show()
myclass.tags.append('first')
myclass.tags.append('second')
myclass.tags.append('third')

print(MyDataclass.language)
MyDataclass.show_profession('hard')
print(myclass.tags)


myclass2 = MyDataclass('Amin',27)
print(myclass2.tags)




@dataclass
class Person:
    name: str
    age: int

@dataclass
class Employee(Person):
    employee_id: int

# The Employee class automatically inherits 'name' and 'age' from Person
# and adds its own 'employee_id' field [1, 3].
# Its __init__ method will take name, age, and employee_id as arguments.
emp1 = Employee(name="Alice", age=30, employee_id=123)
emp2 = Employee(name="Rax", age=31, employee_id=123)
emp3 = Employee(name="Wax", age=31, employee_id=123)
print(emp1)
print(emp2)
print(emp3)
# Output: Employee(name='Alice', age=30, employee_id=123)

