"""def palindrom(num):
    str_num=str(num)
    return str_num==(str_num[::-1])

num = int(input("Enter The number: "))
print(palindrom(num))
print("Hello")
def second_method_pali(num):
    original_num=num
    lst=[]
    while num :
        atten= num%10
        lst.append(str(atten))
        num=num//10
    return str(original_num)==''.join(lst)
num = int(input("Enter num: "))
print(second_method_pali(num))
"""
"""def common_pre():
    strs = ["flower","flow","floght","floo"]
    new_strs=sorted(strs)
    res=""
    length=min(len(new_strs[0]),len(new_strs[-1]))
    for i in range(length):
        if new_strs[0][i] != new_strs[-1][i]:
            return res
        res+=new_strs[0][i]
print(common_pre())"""
from collections import defaultdict
from collections import Counter
d = defaultdict(int)
L = [1, 2, 3, 4, 2, 4, 1,1, 2, 2, 2] 
for i in L: 
    d[i] += 1
print("Occurrences:", dict(d))
sorted_d_asc = sorted(L, key=lambda el: d[el])
sorted_d_desc = sorted(d.items(), key=lambda el: el[1], reverse=True)
print("Sorted by occurrence (ascending):", sorted_d_asc)
print("Sorted by occurrence (descending):", sorted_d_desc)
counter = Counter(L)
sorted_L= sorted(L, key = lambda x : (counter[x], x), reverse=True)
print(sorted_L)