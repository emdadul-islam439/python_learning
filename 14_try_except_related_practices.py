a = input('Enter a number: ')
b = input('Enter another number: ')

try:
    print('Sum of the two number is: ', int(a) + int(b))
except Exception as e:
    print('Exception: ', e)

print('program finished')