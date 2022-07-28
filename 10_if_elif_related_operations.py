#normal if-elif-else statements
var1 = 6
var2 = 12
# var3 = int(input()) #can typecast while taking input

if var1 > var2:
    print('var1 is greater than var2')
elif var1 == var2:
    print('var1 and var2 are equal')
else:
    print('var1 is smaller than var2')


#different approaches
st = ({1, 2, 3, 4})
print(st)

if 3 in st:
    print('3 is in st')
else:
    print('3 is not in st')


#short-hand if-else related operation
a = 5
b = 6
print('a is greater than b') if(a>b) else print('a is smaller or equal to b')

## can't add elif between short-hand if-else
# print('a is greater than b') if(a>b) elif(a==b) print('a and b are equal')  else print('a is smaller or equal to b')
