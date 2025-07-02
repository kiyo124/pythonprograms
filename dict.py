dictionary={'a':'Apple','b':'Ball','c':'Cat','d':'Dog'}
print(dictionary)
print('After adding')
dictionary['e']='Elephant' #for adding element
print(dictionary)
print('after deleting')
del(dictionary['c'])  #for deleting element
print(dictionary)
print('all keys of dictionary')
print(dictionary.keys())
print('all values of dictionary')
print(dictionary.values())
print('b' in dictionary)
print(dictionary.get('g',"'g' not found"))