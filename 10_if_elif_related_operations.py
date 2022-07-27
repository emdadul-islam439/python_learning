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