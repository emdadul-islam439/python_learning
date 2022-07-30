for _ in range(int(input())):
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    a_min = min(a_list)
    b_min = min(b_list)

    result = 0
    for i in range(n):
        a_temp = a_list[i] - a_min
        b_temp = b_list[i] - b_min
        for_minus = min(a_temp, b_temp)
        result += a_temp + b_temp - for_minus
    
    print(result)