# 'hello world' will be printed 10 times
from re import A


print(10 * 'hello world ')

#this time it will actually multiply the numbers
print(10 * int('79') + int('89'))

#but this time the calculation will be printed 10 times
print(10 * str(int('79') + int('89')))



#out of the box SWAP FEATURE!
a = 1
b = 2
print('(a,b) = ', '(', a, ',', b, ')')

a,b = b,a 
print('(a,b) = ', '(', a, ',', b, ')')\


#getting integer result of division
print(15//6) #will return 2
print(50//7) #will return 7


#get true-false from ampersand operator
checkVar = 10 % 2
print(checkVar)
if(checkVar):
    print('work like True')
else:
    print('work like False')

checkVar = 11 % 2
if(checkVar):
    print('work like True')
else:
    print('work like False')