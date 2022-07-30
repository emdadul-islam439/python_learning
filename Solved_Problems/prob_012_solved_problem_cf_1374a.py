arr = []
for i in range (10000):
    if(len(arr) > 1000):
        break;
    if i % 3 == 0 or i % 10 == 3:
        continue
    else:
        arr.append(i)
# print(arr)

for _ in range(int(input())):
    k = int(input())
    print(arr[k-1])
