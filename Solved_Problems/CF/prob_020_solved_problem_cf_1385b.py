for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    permutation = []

    for item in arr:
        if item in permutation:
            continue
        else:
            permutation.append(item)
    for item in permutation:
        print(item, end=' ')
    print()