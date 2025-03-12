n = int(input())
a = list(map(int, input().split()))
ans = float("inf")
cum =0
pnt=0
for i in range(n-1):
    cum +=a[i+1] -a[i]
    if cum < ans:
        ans = min(ans, cum)
        pnt = a[i+1]
print(pnt)