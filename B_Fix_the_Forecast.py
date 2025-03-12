t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    a  = list(map(int, input().split()))
    b = list(map(int, input().split()))
    dct  = {}
    for indx in range(len(a)):
        dct[indx] = a[indx]
    a.sort()
    b.sort()
    count = {}
    for i in range(n):
        count[a[i]] = b[i]
    lst = [0] * n
    for key , val in dct.items():
        lst[key] = count[val]
    print(*lst)
    #print(count)