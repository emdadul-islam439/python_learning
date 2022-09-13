t = int(input())

while t:
    t -= 1
    
    x, y, z = map(int, input().split())
    if (x == y and y == z):
        print("YES")
        print(f'{x} {x} {x}')
    elif  (x == y and y != z and x > z):
        print("YES")
        print(f'{x} {z} {z} ')
    elif  (x != y and y == z  and z > x):
        print("YES")
        print(f'{x} {x} {z} ')
    elif (x == z and x != y and x > y):
        print("YES")
        print(f'{y} {x} {y}')
    else:
        print("NO")