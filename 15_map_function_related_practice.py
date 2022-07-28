def myfunc(a):
  return len(a)

x = map(myfunc, ('apple', 'banana', 'cherry', 'berry'))

print(x) #output: <map object at 0x.....>

#convert the map into a list, for readability:
print(list(x))  #output: [5, 6, 6, 5]

#trying to convert into dictionary
print(dict(x)) #output: {}

#trying to convert into set
print(set(x)) #output: set()
print({x}) #output: {<map object at .....>}
print(type({x})) #output: <class 'set'>

#trying to convert into tuple
print(tuple(x)) #output: ()
print(str(x))