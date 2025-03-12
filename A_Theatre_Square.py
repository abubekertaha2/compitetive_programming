n,m,a= map(int, input().split())
if n % a != 0 :
    n1 = (n//a) +1
else:
    n1 = n//a
if (m %a) != 0:
    n2 = (m //a) +1
else:
    n2 = m//a
print(n1 * n2)
