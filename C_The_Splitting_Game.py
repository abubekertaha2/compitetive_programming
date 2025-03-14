
from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    Set = set()
    dct = defaultdict(int)
    for i in range(len(s)):
        dct[s[i]] +=1
    max_val = 0
    
    for i in range(n-1):
        Set.add(s[i])
        dct[s[i]] -= 1
        
        if dct[s[i]] == 0:
            del dct[s[i]]
        
        max_val = max(max_val, len(Set) + len(dct))
    
    print(max_val)