from collections import defaultdict
def eval():
    n , k , d =map(int, input().split())
    a = list(map(int, input().split()))
    cnt = defaultdict(int)
    res = float("inf")
    for i in range(d):
        cnt[a[i]] +=1
    if d == len(a):
        return len(cnt)
    res = min(res,len(cnt))
    for i in range(d, n):
        cnt[a[i]] +=1
        cnt[a[i-d]] -=1
        # res = min(res,len(cnt))
        if cnt[a[i - d]] == 0:
            del cnt[a[i - d]]
        res = min(res,len(cnt))
    return res
t = int(input())
for _ in range(t):
    ans =eval()
    print(ans)


