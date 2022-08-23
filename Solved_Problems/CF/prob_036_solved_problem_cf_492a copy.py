n = int(input())

level = 0
total_cubes_in_this_level = 0

while True:
    level += 1
    total_cubes_in_this_level += level
    
    if total_cubes_in_this_level < n:
        n -= total_cubes_in_this_level
    elif total_cubes_in_this_level == n:
        print(level)
        break
    else:
        print(level - 1)
        break