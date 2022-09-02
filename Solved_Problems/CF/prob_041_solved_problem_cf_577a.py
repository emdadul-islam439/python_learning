n, x = map(int, input().split())

i = 1
pairs = 0
while i * i <= x and i <= n:
    if x % i == 0:
        no_of_times = int(x/i)
        if no_of_times <= n:
            pairs += 2
            if no_of_times == i:
                pairs -= 1
    i += 1

print(pairs)