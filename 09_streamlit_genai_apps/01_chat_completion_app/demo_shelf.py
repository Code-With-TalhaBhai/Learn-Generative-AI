# In Python, the `shelve` module provides a simple interface for persistent storage of Python objects. It acts as a persistent dictionary where Python objects can be stored and retrieved using keys. The data is stored in a file on the disk.
import shelve


shelf = shelve.open('mydata')

shelf['key1'] = {'name':'talha','age':21}
shelf['key2'] = [1,2,3,5,35,3]

shelf['key3'] = 'string is good'

print('dict',shelf['key1'])
print('list',shelf['key2'])
print('list',shelf['key3'])

shelf.close()
