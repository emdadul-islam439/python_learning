i = 0
while(i < 40):
    if(i > 30):
        break
    if i % 2:
        i = i+1
        continue
    print(i)
    i = i+1

while(True):
    inputNumber = int(input('Enter a number: '))
    if inputNumber > 10:
        print("Input is more than 100.")
        break
    else:
        print('Enter again')


