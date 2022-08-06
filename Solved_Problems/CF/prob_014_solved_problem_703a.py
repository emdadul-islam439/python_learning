mishka = 0
chris = 0

for _ in range(int(input())):
    m, c = map(int, input().split())
    if m > c:
        mishka += 1
    elif m < c:
        chris += 1

if mishka > chris:
    print('Mishka')
elif mishka == chris:
    print('Friendship is magic!^^')
else:
    print('Chris')