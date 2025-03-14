def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a = []
        for _ in range(n):
            a.append(list(map(int, input().split())))

        def call(x, y, n, m):
            res = 0
            indx = 0
            while x - indx > -1 and y - indx > -1:
                res += a[x - indx][y - indx]
                indx += 1
            indx = 0
            while x - indx > -1 and y + indx < m:
                res += a[x - indx][y + indx]
                indx += 1
            indx = 0
            while x + indx < n and y + indx < m:
                res += a[x + indx][y + indx]
                indx += 1
            indx = 0
            while x + indx < n and y - indx > -1:
                res += a[x + indx][y - indx]
                indx += 1

            return res - 3 * a[x][y]

        ans = 0
        for i in range(n):
            for j in range(m):
                ans = max(ans, call(i, j, n, m))

        print(ans)

solve()