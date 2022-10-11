t = int(input())

while t:
    t -= 1
    
    n = int(input())
    one_third = int(n/3)
    
    if n % 3 == 0:
        print(f'{one_third} {one_third + 1} {one_third -1}')
    elif n == 7:
        print('2 4 1')
    else:
        print(f'{one_third + 1} {one_third + 2} {n - one_third - one_third - 3}')