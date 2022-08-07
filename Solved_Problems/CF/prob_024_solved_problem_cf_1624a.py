t = int(input())
while(t):
    t -= 1
    n = int(input())
    arr = list(map(int, input().split()))
    mx = max(arr)
    mn = min(arr)

    ans = mx-mn
    print(ans)