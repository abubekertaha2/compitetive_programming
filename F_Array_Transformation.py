from collections import Counter
t = int(input ())
for i in range(t):
    n = int(input())
    nums = map(int, input().split())
    num = Counter(nums)
    lst =[]
    for val, freq in num.items():
        lst.append(freq)
    lst.sort()
    print(lst)
    pr_sum= 0
    ans = float("inf")
    for i in range(len(lst)):
        left_ele= (len(lst)-i) * lst[i]
        removed = n -(left_ele + pr_sum )
        pr_sum+= lst[i] 
        ans = min(ans , removed)
    print(ans)
