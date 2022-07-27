#some basic string related operation
myString = "Hello How are you?"
print('myStr len :', len(myString))
print(myString[0:6])
print(myString[0:10])
print(myString[0:100]) #range can be 'out of bound'


print('1 -------------------------------- 1')
print(myString[5:]) #print all starting from 5th index
print(myString[:]) #print all
print(myString[::]) #print all


print('2 -------------------------------- 2')
print(myString[-7:-1]) #1-based reverse index (7th character from last to last character)
print(myString[-1:-7])


print('3 -------------------------------- 3')
#print every odd positioned character
print(myString[0:10:2])
#print every even positioned character
print(myString[1:10:2])


print('4 -------------------------------- 4')
#print every 3rd character starting from index-1
print(myString[1:100:3])
#print every 4th character starting from index-0
print(myString[0:100:4])
