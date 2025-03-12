from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    que = deque()
    que.append(a[0])  

    for i in range(1, len(a)):
        if a[i] < que[0]:
            que.appendleft(a[i])
        else:
            que.append(a[i])

    print(*que)