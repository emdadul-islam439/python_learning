from curses.ascii import isalnum, isdigit
from operator import truediv

def is_int(given_input):
    try:
        int(given_input)
        return True
    except ValueError:
        return False

exampleList = ['he', 'she', 1, 3, 6, 'it', 10, 22]

#exercise: check if it is a number and then print if it is greater than 6
for item in exampleList:
    if is_int(item):
        if int(item) > 6:
            print(item)
