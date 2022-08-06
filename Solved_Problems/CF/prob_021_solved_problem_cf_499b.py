import string

def return_string(inputString):
    return inputString

n, m = map(int, input().split())
word_dictionary = dict()
for _ in range(m):
    a, b = map(return_string, input().split())
    word_dictionary[a] = a if(len(a) <= len(b)) else b

inputStringList = list(map(return_string, input().split()))
outputString = ''
for i in range(n):
    outputString += word_dictionary[inputStringList[i]] + ' '

print(outputString)