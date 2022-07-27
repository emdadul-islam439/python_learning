#dictionary is nothing but key,value pairs

#empty dictionary
dictionary1 = {}
print(type(dictionary1))

#adding value
dictionary1['hello'] = 'hi'
print(dictionary1)


#dictionary with some items
dictionary2 = {'ami' : 'tumi', 'he':'she','this':'that'}
print(dictionary2)

#printing key-values
print(dictionary2['ami'])

##don't know how to print a value's respective key


#dictionary under dictionary
dictionaryUnderDictionary = {'school':'madrasah', 'bbc':'cnn', 'hello':'world', 'keyValues':{1:2, 3:5, 6:8}}
print(dictionaryUnderDictionary) 
print(dictionaryUnderDictionary['keyValues'][1]) #printing values' value



##copy dictionary with reference (changing one will affect another)
# dictionary1 = dictionary2
# print(dictionary1)
# print(dictionary2)

# dictionary1.clear()
# print(dictionary1)
# print(dictionary2)


##copy dictionary without reference (changing one will not affect other)
# dictionary1 = dictionary2.copy()
# print(dictionary1)
# print(dictionary2)

# dictionary1.clear()
# print(dictionary1)
# print(dictionary2)


#different functions
print(dictionary1.items())
print(dictionary1.items())
