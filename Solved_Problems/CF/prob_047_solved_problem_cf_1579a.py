t = int(input())

while t:
    t -= 1
    str = input()
    
    count_a = str.count('A')
    count_b = str.count('B')
    count_c = str.count('C')
    
    if count_a + count_c == count_b:
        print("YES")
    else:
        print("NO")