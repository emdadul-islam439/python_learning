t = int(input())
while t:
    t -= 1
    h, m = map(int, input().split())
    print(1440 - (h*60 + m))