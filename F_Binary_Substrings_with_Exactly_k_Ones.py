from collections import defaultdict
def eval(k, s):
    n = len(s)
    count = 0
    cur_sum = 0
    dct = defaultdict(int)
    dct[0] =1
    for i in range(n):
        cur_sum += (1 if s[i] == '1' else 0)
        if cur_sum - k in dct :
            count += dct[cur_sum - k]
        dct[cur_sum] +=1

    return count

k = int(input())
s = input()
result = eval(k, s)
print(result)