n = int(input())
l=[]
def recursion(n):
    if n >0:
        #recursion(n-1)
        l.append(n)
        recursion(n-1)
recursion(n)
print(*l)