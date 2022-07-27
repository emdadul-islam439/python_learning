#list of one type of items (though its type is only 'list', not 'string list' or anything else.)
sameTypeListItems = ['ami', 'tumi', 'she', 'sutut', 'hteh']
print(sameTypeListItems)
print(type(sameTypeListItems))


#list of different types of items
differentTypeListItems = ['ami', 'tumi', 'he', 'she', 1, 2, 3]
print(differentTypeListItems)
print(type(differentTypeListItems))


# accessing diffrent individual items
print(sameTypeListItems[1])
print(sameTypeListItems[3])

print(differentTypeListItems[0])
print(differentTypeListItems[4])


#sort list
print(sameTypeListItems.sort())
#print(differentTypeListItems.sort()) #can't sort different data-typed items


#print range
print(sameTypeListItems[1:4])
print(differentTypeListItems[2:5])

#different library functions
sameTypeListItems.reverse()
differentTypeListItems.append(8)
sameTypeListItems.insert(0, 'hi') #added 'hi' into 0th-index
sameTypeListItems.remove('hi')
sameTypeListItems[0] = 'hi'

