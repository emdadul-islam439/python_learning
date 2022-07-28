list1 = ['ami', 'tumi', 'he', 'she', 'it']

#normal for loop
for str in list1:
    print(str)
##can iterate TUPLE in the same way...



listOfList = [['ami','tumi'], ['he', 'she'], ['this', 'those']]
for item in listOfList:
    print(item)

#can customize the 'item' section
for key, value in listOfList:
    print(key)

for key, value in listOfList:
    print(key, value)


#casting the listOfList to DICTIONARY
dictionary1 = dict(listOfList)
print(dictionary1)
print(dictionary1.items())
for key, value in dictionary1.items():
    print(value)

##won't work in this way (can't access to dictionary, don't know why)
# for key, value in dictionary1:
#     print(value)

#can only access the keys with traditional iteration
for keys in dictionary1:
    print(keys)
