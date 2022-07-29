for _ in range(int(input())):
    n = input()
    arr = list( map(int, input().split()) )
    # print(arr)

    resultIdx = -1
    for i in range(len(arr)):
        if(resultIdx != -1):
            break
        if i == 0:
            if (arr[0]!=arr[1]) and (arr[0] != arr[2]) : resultIdx = 0
        elif i == len(arr)-1:
            if (arr[i]!=arr[i-1]) and (arr[i] != arr[i-2]): resultIdx = len(arr) - 1
        elif (arr[i] != arr[i-1]) and (arr[i] != arr[i+1]): resultIdx = i
            
    print(resultIdx + 1)