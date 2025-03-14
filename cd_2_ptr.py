n,s=map(int, input().split())
lst =list(map(int, input().split()))
max_len=0
res=0
i,j=0,0
while j < len(lst):
    if lst[j] + res <=s :
        res += lst[j]
        j+=1
        max_len= max(max_len,j-i)
    else:
        res-=lst[i]
        i+=1
print(max_len)
#7 20
#2 6 4 3 6 8 9