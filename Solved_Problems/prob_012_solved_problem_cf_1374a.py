for _ in range(int(input())):
    x, y, n = map(int, input().split())

    normal_reminder = n % x
    if normal_reminder == y:
        print(n)
    elif normal_reminder > y:
        print(n - (normal_reminder - y))
    else:
        print(n - normal_reminder - x + y)