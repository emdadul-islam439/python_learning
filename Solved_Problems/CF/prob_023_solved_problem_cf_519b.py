n = int(input())
arr = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr.sort()
arr1.sort()
arr2.sort()

for i in range(len(arr1)):
    if arr[i] != arr1[i]:
        print(arr[i])
        break
    elif i == len(arr1) - 1:
        print(arr[i+1])

for i in range(len(arr2)):
    if arr2[i] != arr1[i]:
        print(arr1[i])
        break
    elif i == len(arr2) - 1:
        print(arr1[i+1])