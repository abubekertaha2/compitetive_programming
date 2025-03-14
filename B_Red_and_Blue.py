t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    ans = 0
    cur = 0
    for i in range(n):
        cur +=a[i]
        ans= max(ans, cur)
    ans1 = 0
    cur1 = 0
    for i in range(m):
        cur1 +=b[i]
        ans1 = max(ans1, cur1)
    print(ans1+ ans)

    
