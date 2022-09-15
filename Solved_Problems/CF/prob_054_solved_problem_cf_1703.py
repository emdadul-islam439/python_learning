t = int(input())

while t:
    t -= 1
    n = int(input())
    str = input()
    
    mp = dict()
    i = 0
    res = 0
    
    while i < n:
        if str[i] not in mp:
            res += 1
            mp[str[i]] = 1
        res += 1
        i += 1
        
    print(res)