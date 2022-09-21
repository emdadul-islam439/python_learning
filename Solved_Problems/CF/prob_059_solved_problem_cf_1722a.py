t = int(input())

while t:
    t -= 1
    n = int(input())
    str = input()
    
    if n == 5 and str.count('T') == 1 and str.count('i') == 1 and str.count('m') == 1 and str.count('u') == 1 and str.count('r') == 1:
        print('YES')
    else:
        print('NO')
    
    