t = int(input())

while t:
    t -= 1
    
    n = int(input())
    arr = list(map(int, input().split()))
    
    odd = 0
    even = 0
    
    for num in arr:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
            
    if odd % 2 == 1:
        print("YES")
    else:
        if odd > 0 and even > 0:
            print("YES")
        else:
            print("NO")