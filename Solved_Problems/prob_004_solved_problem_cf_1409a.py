#number of test cases
t = int(input())

i = 0
while(i < t):
    inputStringList = input().split()
    a,b = int(inputStringList[0]), int(inputStringList[1])

    difference = abs(a-b)

    result = int(difference/10)
    if(difference % 10): 
        result += 1
    
    print(result)

    i += 1
