for _ in range (int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    one_count = arr.count(1)
    two_count = arr.count(2)

    can_be_divided = False
    if sum(arr) % 2 == 0:
        if (one_count % 2 == 0 and two_count % 2 ==0):
            can_be_divided = True
        if (one_count >= 2 and two_count % 2 == 1):
            can_be_divided = True
    if(can_be_divided):
        print('YES')
    else:
        print('NO')