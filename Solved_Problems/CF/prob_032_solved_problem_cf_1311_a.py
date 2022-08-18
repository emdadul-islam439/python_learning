t = int(input())

while t:
    t -= 1
    a, b = map(int, input().split())
    
    if a == b:
        print(0)
    elif a > b:
        print(1) if (a-b) % 2 == 0 else print(2)
    else:
        print(1) if (a-b) % 2 == 1 else print(2)