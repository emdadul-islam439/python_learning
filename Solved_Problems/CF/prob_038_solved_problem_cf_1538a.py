t = int(input())

while t:
    t -= 1
    
    n = int(input())
    arr = list(map(int, input().split()))
    
    mx = max(arr)
    mn = min(arr)
    
    max_pos = arr.index(mx) + 1
    min_pos = arr.index(mn) + 1
    
    # max_pos, min_pos = max(max_pos, min_pos), min(max_pos, min_pos)
    if(max_pos < min_pos):
        max_pos, min_pos = min_pos, max_pos
    # print(f"max_pos = {max_pos}  min_pos={min_pos} ")
    
    optimal_result = n
    optimal_result = min(optimal_result, max_pos)
    optimal_result = min(optimal_result, n - min_pos + 1)
    optimal_result = min(optimal_result, min_pos + (n-max_pos+1))
    
    print(optimal_result)