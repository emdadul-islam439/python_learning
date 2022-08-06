# helper function to type cast list 
# (source: https://www.geeksforgeeks.org/python-type-casting-whole-list-and-matrix/)
def cast_list(test_list, data_type):
    return list(map(data_type, test_list))

#taking input
inputString = input()
splitStringList = inputString.split()

#type-casted the input string-list
splitIntList = cast_list(splitStringList, int)
splitIntList.sort()

#assigning four variables to their respective values
(a_plus_b, a_plus_c, b_plus_c, a_plus_b_plus_c) = (splitIntList[0], splitIntList[1], splitIntList[2], splitIntList[3])

c = a_plus_b_plus_c - a_plus_b
a = a_plus_c - c
b = b_plus_c - c

print(a, b, c)