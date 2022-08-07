t = int(input())
while t:
    t -= 1
    n = int(input())
    isOddFound = False

    while n > 1:
        if n%2:
            print("YES")
            isOddFound = True
            break
        n/=2
    
    if isOddFound == False:
        print("NO")
