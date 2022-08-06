for _ in range(int(input())):
    input()
    str = input()

    charList = []
    is_result_found = False
    for i in range(len(str)):
        if i==0:
            charList.append(str[i])
        elif str[i] != str[i-1]:
            if str[i] not in charList:
                charList.append(str[i])
            else:
                print('NO')
                is_result_found = True
                break
    
    if(is_result_found == False):
        print('YES')
        

