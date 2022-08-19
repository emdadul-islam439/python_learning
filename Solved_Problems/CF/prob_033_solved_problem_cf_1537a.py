t = int(input())

while t:
    t-=1
    
    n = int(input())
    arr = list(map(int, input().split()))
    summation = sum(arr)
    
    if summation > n:
        print(summation - n)
    elif summation == n:
        print(0)
    else:
        print(1)
        