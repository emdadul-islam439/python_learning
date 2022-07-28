inputString = input()
splitStringList = inputString.split()
(a_plus_b, a_plus_c, b_plus_c, a_plus_b_plus_c) = (int(splitStringList[0]), int(splitStringList[1]), int(splitStringList[2]), int(splitStringList[3]))

c = a_plus_b_plus_c - a_plus_b
a = a_plus_c - c
b = b_plus_c - c

print(a, b, c)