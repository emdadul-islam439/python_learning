t = int(input())
while t:
    t -= 1
    
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    
    total = sum(arr)
    avg = int(total/n)
    
    if avg * n != total:
        print("-1")
    else:
        i = 0
        while i < n:
            if arr[i] > avg:
                break
            i += 1
            
        print(n - i)