n, t = map(int, input().split())
a = list(map(int, input().split()))
ans, count, l = 0, 0, 0
max_len = 0  

for r in range(len(a)):
    ans += a[r]
    max_len += 1 

    while ans > t:
        ans -= a[l]
        l += 1
        max_len -= 1 

    count = max(count, max_len)

print(count)