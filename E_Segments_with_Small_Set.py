from collections import defaultdict
t , n= map(int, input().split())
a = list(map(int, input().split()))
dct = defaultdict(int)
left , res = 0 , 0
for i in range (len(a)):
    dct[a[i]] += 1
    while len(dct) > n:
        dct[a[left]] -= 1
        if dct[a[left]] ==0:
            del dct[a[left]]
        left += 1
    res += i - left + 1
print(res)
