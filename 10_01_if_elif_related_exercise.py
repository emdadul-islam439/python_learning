#output wrong answers for certain type of input, otherwise print right values
print("Enter the first variable: ", end = "")
var1 = int(input())

print("Enter the operator: ", end = "")
operator = input()

print("Enter the second variable: ", end = "")
var2 = int(input())

if var1 == 45 and operator == '*' and var2 == 3:
    print('555')
elif var1 == 56 and operator == '+' and var2 == 9:
    print('77')
elif var1 == 56 and operator == '/' and var2 == 6:
    print('4')
elif operator == '+':
    print(var1 + var2)
elif operator == '-':
    print(var1 - var2)
elif operator == '*':
    print(var1 * var2)
elif operator == '/':
    print(var1 / var2)
else:
    print('Something went wrong...')
