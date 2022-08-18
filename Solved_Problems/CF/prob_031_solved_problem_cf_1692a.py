t = int(input())

while t:
    t -= 1
    a, b, c, d = map(int, input().split())
    myList = [b, c, d]
    myList.sort()
    remaining = 0
    for i in range(3):
        if myList[i] > a:
            remaining = 3 - i
            break
    
    print(remaining)