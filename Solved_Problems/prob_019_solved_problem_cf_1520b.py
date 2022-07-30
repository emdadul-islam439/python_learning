import bisect

arr = []
str = ''

while len(str) <= 9:
    str += '1'
    to_add = int(str)
    for i in range(9):
        arr.append(to_add)
        to_add += int(str)

for _ in range(int(input())):
    n = int(input())
    print(bisect.bisect(arr, n))