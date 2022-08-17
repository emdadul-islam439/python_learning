t = int(input())
while t:
    t -= 1
    a, b, c, n = map(int, input().split())
    coin_list = [a, b, c]
    coin_list.sort()
    
    initial_need = (2 * coin_list[2]) - coin_list[0] - coin_list[1]
    
    if n < initial_need:
        print("NO")
    else:
        n -= initial_need
        if n % 3 == 0:
            print("YES")
        else: 
            print("NO")