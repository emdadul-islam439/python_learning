t = int(input())

while t:
    t -= 1
    n = int(input())
    
    i = 1
    while True:
        if i + i > n:
            break
        i += i
    print(i-1)