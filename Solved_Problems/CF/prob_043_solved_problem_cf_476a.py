n, m = map(int, input().split())

if n < m:
    print(-1)
else:
    half = int(n/2)
    half += int(n % 2)
    
    if m >= half:
        print(m)
    else:
        rem = int(half % m)
        ans = half - rem 
        if rem:
            ans += m
        print(ans)
    