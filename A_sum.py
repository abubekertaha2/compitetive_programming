from collections import Counter
def comp(s,t):
    s1= Counter(s)
    t1 = Counter(t)
    ans = 0
    for i in s1:
        if i in t1:
            ans += abs(s1[i] - t1[i])
        else:
            ans += s1[i]
    return ans
s,t = map(str , input().split())
print(comp(s,t))
print("hello Abuki")
    
