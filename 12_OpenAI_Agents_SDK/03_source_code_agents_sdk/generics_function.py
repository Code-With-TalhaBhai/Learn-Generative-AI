from typing import TypeVar,List

T = TypeVar('T')


def get_first_element(arr: list[T])->T:
    return arr[0]

K = TypeVar('K')
V = TypeVar('V')
def get_key_element(my_dict: dict[K,V],key:K)->V:
    return my_dict[key]



ints : List[int] = [1,2,3,4,5,6]
strs = ['a','b','c','d','e']
my_dict = {'a':1,'b':2,'c':3}


print(get_first_element(ints))
print(get_first_element(strs))
print()
print(get_key_element(my_dict,'a'))
print(get_key_element(my_dict,'c'))




