def myfunc(a):
  return len(a)

x = map(myfunc, ('apple', 'banana', 'cherry', 'berry'))

print(x) #output: <map object at 0x.....>
print((x)) #output: <map object at 0x.....>

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

#assigning values with map()
a, b, c = map(int, input().split())
print(a, b, c)

#can we assign value to a list with map()?
string = '1 2 33 50 60 70' #experimenting with string line
emptyList = list(map(int, string.split()))
print(emptyList)

stringList = ['1', '2', '3', '55', '33'] #experimenting with map()?
stringToIntList = list(map(int, stringList))
print(stringToIntList)