from collections import deque
n, k = map(int, input().split())
a=list(map(int, input().split()))
que = deque()
Set = set()
for num in a:
    if num not in Set :
        if len(que) < k:
            que.append(num)
            Set.add(num)
        else:
            que.popleft()
            Set.remove(num)
print(len(que))
print(*que)
