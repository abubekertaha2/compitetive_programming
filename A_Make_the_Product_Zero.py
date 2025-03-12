t = int(input())
matr = [[0]*t for _ in range()]
for i in range(t):
    for j in range(t):
        matr[i][j] = int(input())
ans = 0
j = (t-1)/2
for i in range(t):
    if i  == j:
        continue
    ans +=matr[i][j]
i = (t- 1)/2 
for j in range(t):
    if j == i :
        continue
    ans += matr[i][j]
for i in range(t):
    for j in range(t):
        if i == j:
            ans +=matr[i][j]
for i in range(t):
    for j in range(t):
        if j == i+1:
            ans += matr[i][j]
for i in range(i):
    for j in range(t):
        if i == j+ 1:
            ans += matr[i][j]
print(ans)