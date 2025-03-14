def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    count = 0
    import itertools
    for p in itertools.permutations(a):
        valid = True
        for i in range(n):
            if p[i] <= b[i]:
                valid = False
                break
        if valid:
            count += 1

    print(count % (10**9 + 7))
solve()