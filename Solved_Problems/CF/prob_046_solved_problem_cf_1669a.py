t = int(input())

while t:
    t -= 1
    n = int(input())
    div = 0
    
    if n <= 1399:
        div = 4
    elif n <= 1599:
        div = 3
    elif n <= 1899:
        div = 2
    else:
        div = 1
        
    print(f'Division {div}')