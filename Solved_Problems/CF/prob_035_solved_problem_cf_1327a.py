t = int(input())
while t:
    t-=1
    n, k = map(int, input().split())
    
    if (n % 2 == 0 and k % 2) or (n % 2 and k % 2 == 0) or (k*k > n):
        print("NO")
    else:
        print("YES")