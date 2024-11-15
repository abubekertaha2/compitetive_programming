def solve():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    mx = 0
 
    for i in range(n):
        for j in range(m):
            now = 0
            ci, cj = i, j
 
            while 0 <= ci < n and 0 <= cj < m:
                now += a[ci][cj]
                ci -= 1
                cj -= 1
 
            ci, cj = i, j
            while 0 <= ci < n and 0 <= cj < m:
                now += a[ci][cj]
                ci += 1
                cj -= 1
 
            ci, cj = i, j
            while 0 <= ci < n and 0 <= cj < m:
                now += a[ci][cj]
                ci -= 1
                cj += 1
 
            ci, cj = i, j
            while 0 <= ci < n and 0 <= cj < m:
                now += a[ci][cj]
                ci += 1
                cj += 1
 
            now -= a[i][j] * 3
            mx = max(mx, now)
 
    print(mx)
 
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
