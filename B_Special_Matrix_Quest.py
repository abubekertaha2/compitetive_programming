t = int(input())
matr = []
for _ in range(t):
    row = list(map(int, input().split()))
    matr.append(row)

ans = 0
for i in range(len(matr)):
    ans +=matr[i][i]
    ans += matr[i][t-i-1]
n = t//2
for i in range(len(matr)):
    ans += matr[n][i]
    ans += matr[i][n]

print(ans - (matr[n][n]* 3))