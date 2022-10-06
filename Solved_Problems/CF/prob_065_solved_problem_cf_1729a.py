t = int(input())
while t:
    t -= 1
    a, b, c = map(int, input().split())
    
    a_time = a - 1
    b_time = abs(c-b) + abs(c-1)
    
    if a_time < b_time:
        print(1)
    elif b_time < a_time:
        print(2)
    else:
        print(3)