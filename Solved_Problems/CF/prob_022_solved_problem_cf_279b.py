n, t = map(int, input().split())
arr = list(map(int, input().split()))
# arr.sort()

start_idx = 0
time_count = 0
max_book_read = 0

for i in range(n):
    if arr[i] > t:
        time_count = 0
        start_idx = i+1
    else:
        time_count += arr[i]
        if(time_count <= t):
            dif = i - start_idx + 1
            max_book_read = max(max_book_read, dif)
        else:
            while(time_count > t):
                time_count -= arr[start_idx]
                start_idx += 1

    print(f"i = {i}  arr[i]= {arr[i]}  start_idx = {start_idx}  time_count = {time_count}  max_book_read = {max_book_read}")
print(max_book_read)