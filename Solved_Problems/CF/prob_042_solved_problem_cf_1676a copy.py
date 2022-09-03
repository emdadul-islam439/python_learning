t = int(input())

while t:
    t -= 1
    str = input()
    
    first_half = 0
    i = 0
    while i < 3:
        first_half += int(str[i])
        i += 1
    
    second_half = 0
    while i < 6:
        second_half += int(str[i])
        i += 1
        
    if first_half == second_half:
        print("YES")
    else:
        print("NO")