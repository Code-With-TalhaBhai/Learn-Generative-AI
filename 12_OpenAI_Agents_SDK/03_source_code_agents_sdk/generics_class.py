from typing import Generic,TypeVar, List
from dataclasses import dataclass,field


T = TypeVar('T')

@dataclass
class MyContainer(Generic[T]):
    items : List[T] = field(default_factory=list)

    def add(self,item: T):
        self.items.append(item)

    def get_all(self)->List[T]:
        return self.items
    


ints = MyContainer[int]()
ints.add(1)
ints.add(2)
ints.add(3)
print(ints.get_all())


strs = MyContainer[str]()
strs.add('a')
strs.add('b')
strs.add('c')
print(strs.get_all())