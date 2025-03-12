n,t, c = map(int, input().split())
a = list(map(int, input().split()))
cnt =0
l,r =0,0
for i in range(len(a)):
    if a[i] <= t:
        if r-l+1 <c :
            r +=1
        else:
            cnt +=1
            r +=1
            l+=1
    elif a[i] > t:
        l=r+1
        r+=1
print(cnt)

