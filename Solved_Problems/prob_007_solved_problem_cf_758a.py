n = int(input())
arr = list( map(int, input().split()) )

max_element = max(arr)
money_needed = 0

for money in arr:
    money_needed += (max_element - money)

print(money_needed)