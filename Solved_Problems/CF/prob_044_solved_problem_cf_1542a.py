t = int(input())

while t:
    t -= 1
    
    n = int(input())
    arr = map(int, input().split())
    
    even = 0
    odd = 0
    
    for num in arr:
        if num % 2:
            odd += 1
        else:
            even += 1
            
    if odd == even:
        print("Yes")
    else:
        print("No")