m, s = map(int, input().split())

if s == 0:
    if m > 1:
        print("-1 -1")
    else:
        print("0 0")
else:
    i = 0
    result = []
    last_idx = -1
    last_digit = -1
    
    while i < m - 1:
        if s > 9:
            result.append(str(9))
            s -= 9
        else:
            result.append(str(s))
            if s > 0:
                last_idx = i
                last_digit = s
            s -= s
        i += 1
            
    if s >= 10:
        print("-1 -1")
    else:
        result.append(str(s))
        mx_str = ''
        for chr in result:
            mx_str += chr
        
        if last_idx > -1:
            result[last_idx] = f'{last_digit - 1}'
            result[len(result)-1] = '1'
            
        tmp_str = result[::-1]
        mn_str = ''
        for chr in tmp_str:
            mn_str += chr
        print(f'{mn_str} {mx_str}')