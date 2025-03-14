def sort():
    n = int(input())
    a = list(map(int, input().split()))

    odds = []
    evens = []
    for x in a:
        if x % 2 == 0:
            evens.append(x)
        else:
            odds.append(x)

    if len(odds) > 0 and len(evens) > 0:
        a.sort()
        print(*a)
    else:
        print(*a)



sort()