t = int(input())

while t:
    t -= 1
    n = int(input())
    r1 = input()
    r2 = input()
    isSame = True
    i = 0
    
    while i < n:
        if r1[i] != r2[i] and (r1[i] == 'R' or r2[i] == 'R'):
            isSame = False
        i += 1
    
    if isSame:
        print("YES")
    else:
        print("NO")