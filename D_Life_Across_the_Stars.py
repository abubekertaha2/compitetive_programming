n = int(input())
lst = [0]*(10+ 2)
for _ in range(n):
    b,d = map(int, input().split())
    lst[b] +=1 
    lst[d] -=1
prfx = 0
max_pep=0
indx =0
for i in range(len(lst)):
    prfx +=lst[i]
    if prfx > max_pep:
        max_pep = max(prfx, max_pep)
        max_pep= prfx
        indx =i
print(indx,max_pep)