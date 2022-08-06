from pydoc import ispackage


for _ in range(int(input())):
    year = int(input())

    i = 0
    is_possible = False
    while i <= year:
        if (year - i) % 2020 == 0:
            is_possible = True
            break
        i += 2021

    if is_possible:
        print('YES')
    else:
        print('NO')