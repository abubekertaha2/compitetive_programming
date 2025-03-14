def longestSub(s):
    dct = {}
    start = 0 
    max_length = 0  

    for i in range(len(s)):
        cur_chr=s[i]
        if s[i] in dct and dct[s[i]] >= start:
            start = dct[s[i]] + 1 
            
        dct[cur_chr] = i 
        max_length = max(max_length, i - start + 1)  
    return [max_length , dct, start]
print(longestSub('abcbad'))