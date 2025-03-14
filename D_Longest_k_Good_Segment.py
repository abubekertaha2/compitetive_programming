from collections import defaultdict
def longest_k():
    t , n= map(int, input().split())
    a = list(map(int, input().split()))
    dct = defaultdict(int)
    left ,max_len= 0 , 0
    l ,r =0,0
    for i in range (len(a)):
        dct[a[i]] += 1
        while len(dct) > n:
            dct[a[left]] -= 1
            if dct[a[left]] ==0:
                del dct[a[left]]
            left += 1
        if i - left > max_len:
            max_len = i - left
            l = left
            r = l + max_len
        max_len = max(max_len, i - left)
    return l +1 , r +1
res = longest_k()
print(*res)