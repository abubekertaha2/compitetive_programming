n=int(input())
def recursion(n):
    if n > 0:
        print("I love Recursion")
        recursion(n-1)
recursion(n)