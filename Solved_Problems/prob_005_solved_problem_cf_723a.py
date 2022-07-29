a, b, c = map(int, input().split())
minimum_step_needed = 300
for i in range(101):
    steps_needed = abs(i-a) + abs(i-b) + abs(i-c)
    minimum_step_needed = min(minimum_step_needed, steps_needed)
print(minimum_step_needed)