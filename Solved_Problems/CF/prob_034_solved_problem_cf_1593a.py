t = int(input())
while t:
    t -= 1
    
    a, b, c = map(int, input().split())
    vote_list = [a,b,c]
    vote_list.sort()
    
    if vote_list[2] > vote_list[1]:
        aa = 0 if a == vote_list[2] else vote_list[2] - a + 1
        bb = 0 if b == vote_list[2] else vote_list[2] - b + 1
        cc = 0 if c == vote_list[2] else vote_list[2] - c + 1
    else:
        aa = vote_list[2] - a + 1
        bb = vote_list[2] - b + 1
        cc = vote_list[2] - c + 1
    
    print(f"{aa} {bb} {cc}")
