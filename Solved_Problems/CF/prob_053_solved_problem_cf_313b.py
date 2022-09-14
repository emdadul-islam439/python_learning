str = input()
length = len(str)

n = int(input())
arr = [0]
i = 0

while i < length-1:
    if i != 0:
        arr.append(arr[i-1])
    
    if str[i] == str[i+1]:
        arr[i] += 1
    i += 1

if length > 1:
    arr.append(arr[length-2])

while n:
    n -= 1
    l, r = map(int, input().split())
    
    l -= 1
    r -= 2
    
    left = 0 if l == 0  else arr[l-1]
    right = arr[r]
    
    print(right - left)
    
    
    