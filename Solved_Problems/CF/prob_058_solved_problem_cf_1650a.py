t = int(input())

while t:
    t -= 1
    str = input()
    chr = input()
    
    i = 0
    length = len(str)
    check = True
    
    while i < length:
        if str[i] == chr:
            print('YES')
            check = False
            break
        i += 2
    
    if check:
        print('NO')
    