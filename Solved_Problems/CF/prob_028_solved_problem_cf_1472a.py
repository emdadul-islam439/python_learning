t = int(input())
while t:
    t -= 1
    w, h, n = map(int, input().split())
    
    total_w = 1
    total_h = 1
    while w % 2 == 0:
        total_w += total_w
        w /= 2
        
    while h % 2 == 0:
        total_h += total_h
        h /= 2
    
    if  total_w * total_h >= n:
        print("YES")
    else:
        print("NO")
    