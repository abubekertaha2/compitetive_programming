n, m = map(int, input().split())
a = list(map(int, input().split()))

arr = [0] * (n - 1)
for i in range(n - 1):
    arr[i] = a[i + 1] - a[i]

prfx1 = [0] * (n + 1)
for i in range(n - 1):
    if arr[i] < 0:
        prfx1[i + 1] = prfx1[i] + abs(arr[i])
    else:
        prfx1[i + 1] = prfx1[i]

prfx2 = [0] * (n + 1)
for i in range(n - 1):
    if arr[i] > 0:
        prfx2[i + 1] = prfx2[i] + arr[i]
    else:
        prfx2[i + 1] = prfx2[i]

for _ in range(m):
    s, t = map(int, input().split())
    if s < t:
        print(prfx1[t - 1] - prfx1[s - 1])
    elif s > t:
        print(prfx2[s - 1] - prfx2[t - 1])

