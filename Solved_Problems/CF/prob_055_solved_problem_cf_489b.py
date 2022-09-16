n = int(input())
n_arr = list(map(int, input().split()))

m = int(input())
m_arr = list(map(int, input().split()))

n_mp = dict()
m_mp = dict()
i = -1
while i <= 101:
    n_mp[i] = m_mp[i] = 0
    i += 1

len_n = len(n_arr)
len_m = len(m_arr)

i = 0
while i < len_n:
     n_mp[n_arr[i]] += 1
     i += 1
     
i = 0
while i < len_m:
     m_mp[m_arr[i]] += 1
     i += 1


n_arr.sort()
result = 0
for num in n_arr:
    if m_mp[num-1] > 0:
        result += 1
        m_mp[num-1] -= 1
    elif m_mp[num] > 0:
        result += 1
        m_mp[num] -= 1
    elif m_mp[num+1] > 0:
        result += 1
        m_mp[num+1] -= 1
        
print(result)