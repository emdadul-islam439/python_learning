t = int(input())

while t:
    t -= 1
    n, d = map(int, input().split())
    
    arr = list(map(int, input().split()))
    arr.sort()
    length = len(arr)
    
    if arr[length - 1] <= d or arr[0] + arr[1] <= d:
        print("YES")
    else:
        print("NO")