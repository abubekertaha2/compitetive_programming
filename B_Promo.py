# n, q= map(int, input().split())
# a=list(map(int, input().split()))
# a.sort(reverse=True)
# for _ in range(q):
#     x,y = map(int, input().split())
#     ans=0
#     for i in range(x):
#         ans += a[i]
#     for j in range((x-y)):
#         ans -=a[j]
#     print(ans)
def solve():
    n, q = map(int, input().split())  
    p = list(map(int, input().split())) 

    p.sort(reverse=True)
    
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + p[i - 1]
    
    for _ in range(q):
        x, y = map(int, input().split()) 
        print(prefix_sum[x] - prefix_sum[x-y])
solve()