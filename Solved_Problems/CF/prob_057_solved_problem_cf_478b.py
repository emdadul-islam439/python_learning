n, m = map(int, input().split())

mx_formations = n - m
# print(f'mx_formations = {mx_formations}')
mx_pair = int((mx_formations * mx_formations + mx_formations)/2)

mn_formations = int(n/m) - 1 
md = int(n%m)

mn_pair = int((mn_formations * mn_formations + mn_formations)/2)
# print(f'mn_pair = {mn_pair}')
mn_pair *= m 
mn_pair += (mn_formations + 1) * md

print(f'{mn_pair} {mx_pair}')