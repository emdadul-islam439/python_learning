#At first didn't get a library function like this. So, wrote my own function
#(reference: question of https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float)
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


print('--------------------')
## another library function based solution:
for item in exampleList:
    if str(item).isnumeric() and item > 6:
        print(item)
