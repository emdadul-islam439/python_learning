n, t = map(int, input().split())
arr = list(map(int, input().split()))

i=0
is_result_found = False
while(i<t):
    if i < len(arr): 
        i += arr[i]
        if i == t-1:
            print('YES')
            is_result_found = True
            break
if is_result_found == False:
    print('NO')