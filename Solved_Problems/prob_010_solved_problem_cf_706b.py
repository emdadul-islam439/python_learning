from bisect import bisect


import bisect
n = input()
arr = list(map(int, input().split()))
arr.sort()

for _ in range(int(input())):
    x = int(input())
    print(bisect.bisect(arr, x))