n = int(input())
str = input()

present_x_count: int = 0
i = 0
ans = 0

for chr in str:
    if chr == 'x':
        present_x_count += 1
    else:
        present_x_count = 0
    
    if present_x_count >= 3:
        ans += 1

print(ans)