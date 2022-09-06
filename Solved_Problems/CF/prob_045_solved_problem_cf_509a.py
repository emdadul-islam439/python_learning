n = int(input())

arr = [[1]*n]*n

for i in range(1, n):
    for j in range(1, n):
        arr[i][j] = arr[i][j-1] + arr[i-1][j]

print(arr[n-1][n-1])