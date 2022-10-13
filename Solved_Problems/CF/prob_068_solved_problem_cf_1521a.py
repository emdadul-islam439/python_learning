t = int(input())

while t:
    t -= 1
    a, b = map(int, input().split())
    
    if b == 1: 
        print('NO')
        continue
    
    z = 2 * a * b
    x = a
    y = z - a 
    
    print(f'YES\n{x} {y} {z}')