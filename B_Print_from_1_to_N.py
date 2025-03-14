n = int(input())
def recursion(n, curr=1):
    if curr <= n:
        print(curr)
        recursion(n, curr+1)
recursion(n)
