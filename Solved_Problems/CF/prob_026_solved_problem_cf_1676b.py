t = int(input())
while t:
    t -= 1
    n = int(input())
    arr = list(map(int, input().split()))
    mn = min(arr)
    total = 0

    for item in arr:
        total += abs(item - mn)

    print(total)