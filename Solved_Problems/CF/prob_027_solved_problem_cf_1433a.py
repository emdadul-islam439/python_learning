t = int(input())

mp = {
    1: 1,
    2: 3,
    3: 6,
    4: 10
}

while t:
    t -= 1
    n = input()
    total = (int(n[0]) - 1) * 10
    total += mp[len(n)]
    print(total)
