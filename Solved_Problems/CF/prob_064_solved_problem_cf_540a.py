n = int(input())
str1 = input()
str2 = input()
i = 0
total_dif = 0

while i < n:
    digit1 = int(str1[i])
    digit2 = int(str2[i])
    total_dif += min(abs(digit1-digit2), min((10-digit1 + digit2),(10-digit2+digit1)))
    
    i += 1
    
print(total_dif)