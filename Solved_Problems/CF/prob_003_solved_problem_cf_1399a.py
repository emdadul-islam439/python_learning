# helper function to type cast list 
# (source: https://www.geeksforgeeks.org/python-type-casting-whole-list-and-matrix/)
def cast_list(test_list, data_type):
    return list(map(data_type, test_list))

#number of test-cases
t = int(input())
i = 0

while(i < t):
    #size of the array
    n = int(input())

    #taking input: element of the array
    inputString = input()
    splitStringList = inputString.split()

    #type-casted the input string-list
    splitIntList = cast_list(splitStringList, int)
    splitIntList.sort()

    #initializing two variables
    j = 1
    difference_between_two_item = 0
    
    #main logic
    while(j < len(splitIntList)):
        difference_between_two_item = max(difference_between_two_item, splitIntList[j]-splitIntList[j-1])
        j += 1

    if(difference_between_two_item > 1): 
        print('NO')
    else: 
        print('YES')

    #increasing the i's value
    i += 1